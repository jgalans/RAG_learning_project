import sqlite3
import pandas as pd
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 1. Cargamos el modelo de "traducción" a números
model_name = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=model_name)

# 2. Nuestras frases (que vendrán de tu DataFrame de Pandas)
#textos = [
#    "Camiseta Eco: Algodón 100% orgánico, fresca para el verano.",
#    "Botas Trekking: Cuero resistente, impermeables y cálidas.",
#    "Gorra Running: Material técnico transpirable, color neón."]

# Conectamos a la DB relacional
conn = sqlite3.connect('ecommerce.db')

# Traemos todo: nombre, descripción y el precio
query = "SELECT nombre, descripcion, precio FROM productos"
df = pd.read_sql(query, conn)

# Creamos la "super-descripción" para el RAG
# Ejemplo: "Camiseta Eco: Algodón orgánico. Precio: 25.0€"
df['texto_para_ai'] = (
    df['nombre'] + ": " + 
    df['descripcion'] + 
    ". Precio: " + df['precio'].astype(str) + "€"
)

textos_finales = df['texto_para_ai'].tolist()
textos = textos_finales

conn.close()

# 3. Creamos la base de datos de vectores en memoria
vectorstore = Chroma.from_texts(textos, embeddings)

# 4. Hacemos una pregunta "conceptual"
pregunta = "ropa para hacer deporte y correr cuando hace sol"

# 5. Buscamos los 2 productos más parecidos
productos = vectorstore.similarity_search(pregunta, k=2)

# 6. AQUÍ ENTRA EL LLM: Procesamos los resultados con un modelo de lenguaje
llm = OllamaLLM(model="llama2")

# Creamos un prompt que le dice al LLM qué hacer con los productos encontrados
prompt_template = PromptTemplate(
    input_variables=["productos", "pregunta"],
    template="""Basándote en estos productos encontrados: {productos}
                Y la pregunta del usuario: "{pregunta}"
                Proporciona una recomendación amable y personal explicando por qué estos productos son adecuados."""
)

# Formateamos los productos encontrados
productos_formateados = "\n".join([f"- {res.page_content}" for res in productos])

# Creamos una cadena que une el prompt + LLM
chain = prompt_template | llm

# 7. Ejecutamos el LLM
# Pasamos las variables dentro de un diccionario {}
input_data = {"productos": productos_formateados, "pregunta": pregunta}
respuesta = chain.invoke(input_data)

print("=== RESPUESTA DEL LLM ===")
print(respuesta)