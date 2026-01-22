🤖 ProyectoRAG: Recomendador Inteligente para E-commerce
Este proyecto implementa un sistema de Generación Aumentada por Recuperación (RAG) que permite consultar un catálogo de productos mediante lenguaje natural. A diferencia de una búsqueda tradicional por palabras clave, este sistema entiende la intención del usuario y genera una respuesta amable y personalizada.

🎯 Capacidades del Sistema
Memoria Semántica: Convierte las descripciones de productos y precios en vectores numéricos.

Búsqueda Contextual: Encuentra productos no solo por su nombre, sino por su utilidad (ej: "algo para el calor").

Razonamiento con LLM: Utiliza Llama2 para explicar por qué esos productos específicos encajan con la duda del usuario.

🛠️ Tecnologías Utilizadas
LangChain (v0.3+): Orquestador del pipeline de IA (usando sintaxis LCEL).

Ollama: Servidor local para correr modelos de lenguaje (LLM).

ChromaDB: Base de datos vectorial persistente.

HuggingFace: Modelo de embeddings all-MiniLM-L6-v2.

SQLite & Pandas: Gestión de la base de datos relacional original.

🚀 Instalación y Configuración
1. Clonar y Preparar el Entorno
Bash

git clone https://github.com/TU_USUARIO/ProyectoRAG.git
cd ProyectoRAG

# Crear entorno virtual
python3 -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Instalar dependencias actualizadas
pip install -r requirements.txt
2. Configurar el "Cerebro" (Ollama)
Asegúrate de tener Ollama instalado y ejecutándose:

Bash

ollama pull llama2
3. Preparar los Datos
Si es la primera vez que lo usas, crea la base de datos de productos:

Bash

python setup_db.py
🎮 Funcionamiento
Ejecuta el recomendador:

Bash

python ia_tienda.py
¿Cómo funciona internamente?
El sistema sigue la nueva sintaxis de LangChain (LCEL):

Retrieval: Busca los k productos más cercanos en la base de datos vectorial chroma_db/.

Augment: Inyecta esos productos y el precio en un PromptTemplate.

Generate: Envía todo a Llama2 mediante chain.invoke() para obtener la respuesta final.

📂 Estructura del Proyecto
Plaintext

ProyectoRAG/
├── ia_tienda.py         # Lógica RAG con LCEL e Invoke
├── setup_db.py          # Script de creación de DB SQLite
├── ecommerce.db         # Base de datos relacional de productos
├── chroma_db/           # Carpeta de persistencia vectorial (auto-generada)
├── requirements.txt     # Dependencias (versiones bloqueadas)
└── .gitignore           # Archivo para ignorar .venv y bases de datos
📝 Notas de Versión (v2.0)
Migración de Librerías: Se ha actualizado de langchain_community a paquetes específicos como langchain-huggingface y langchain-ollama.

Cambio a Invoke: Se eliminó el método depreciado .run() en favor de .invoke().

Persistencia: La base de datos vectorial ahora se guarda localmente para evitar regenerar embeddings en cada ejecución.

💡 ¿Qué sigue?
Si te gusta este proyecto, puedes probar a:

Aumentar el valor de k en similarity_search para dar más opciones al LLM.

Cambiar el modelo en Ollama (ej: mistral o llama3) para comparar respuestas.
