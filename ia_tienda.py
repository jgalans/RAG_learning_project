from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 1. Cargamos el modelo de "traducción" a números
model_name = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=model_name)

# 2. Nuestras frases (que vendrán de tu DataFrame de Pandas)
textos = [
    "Camiseta Eco: Algodón 100% orgánico, fresca para el verano.",
    "Botas Trekking: Cuero resistente, impermeables y cálidas.",
    "Gorra Running: Material técnico transpirable, color neón."]

# 3. Creamos la base de datos de vectores en memoria
vectorstore = Chroma.from_texts(textos, embeddings)

# 4. Hacemos una pregunta "conceptual"
pregunta = "ropa para hacer deporte y correr cuando hace sol"

# 5. Buscamos los 2 productos más parecidos
resultados = vectorstore.similarity_search(pregunta, k=2)

# 6. AQUÍ ENTRA EL LLM: Procesamos los resultados con un modelo de lenguaje
llm = Ollama(model="llama2")

# Creamos un prompt que le dice al LLM qué hacer con los productos encontrados
prompt_template = PromptTemplate(
    input_variables=["productos", "pregunta"],
    template="""Basándote en estos productos encontrados:
{productos}

Y la pregunta del usuario: "{pregunta}"

Proporciona una recomendación amable y personal explicando por qué estos productos son adecuados."""
)

# Formateamos los productos encontrados
productos_formateados = "\n".join([f"- {res.page_content}" for res in resultados])

# Creamos una cadena que une el prompt + LLM
chain = LLMChain(llm=llm, prompt=prompt_template)

# 7. Ejecutamos el LLM para generar una respuesta natural
respuesta = chain.run(productos=productos_formateados, pregunta=pregunta)

print("=== RESPUESTA DEL LLM ===")
print(respuesta)