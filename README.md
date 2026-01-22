# Proyecto RAG - Sistema de Recomendación de Productos

Un sistema inteligente de búsqueda y recomendación de productos basado en **Retrieval-Augmented Generation (RAG)** que utiliza embeddings vectoriales y un modelo de lenguaje (LLM) para proporcionar recomendaciones personalizadas.

## 🎯 ¿Qué es este proyecto?

Este proyecto implementa un asistente de IA para una tienda que:

1. **Entiende preguntas en lenguaje natural** - No necesita palabras clave exactas
2. **Busca productos relevantes** - Utiliza embeddings para encontrar similitudes semánticas
3. **Genera respuestas conversacionales** - Un LLM proporciona recomendaciones personalizadas

**Ejemplo:**
```
Usuario: "Busco ropa para hacer deporte cuando hace sol"
Sistema: Encuentra la Gorra Running y la Camiseta Eco
LLM: "Te recomiendo la Gorra Running porque tiene material transpirable 
que mantiene tu cabeza fresca. La Camiseta Eco es perfecta porque..."
```

## 🔧 Tecnologías Utilizadas

- **Embeddings**: `sentence-transformers` (all-MiniLM-L6-v2)
- **Base de Datos Vectorial**: ChromaDB
- **Framework**: LangChain
- **LLM**: Ollama (Llama2)
- **Datos**: Pandas

## 📋 Requisitos Previos

- Python 3.9+
- Ollama instalado (para el LLM)
- Homebrew (opcional, pero recomendado en macOS)

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/ProyectoRAG.git
cd ProyectoRAG
```

### 2. Crear un entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate  # En macOS/Linux
# o
.venv\Scripts\activate  # En Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Instalar Ollama

En macOS con Homebrew:
```bash
brew install ollama
```

O descárgalo desde: https://ollama.ai

### 5. Descargar el modelo Llama2

Abre una terminal y ejecuta:
```bash
ollama pull llama2
```

Luego inicia el servidor de Ollama (en otra terminal):
```bash
ollama serve
```

## 💻 Uso

Ejecuta el script principal:

```bash
python ia_tienda.py
```

El script hará una búsqueda de ejemplo y mostrará:
- Los productos encontrados
- Una recomendación generada por el LLM

## 📁 Estructura del Proyecto

```
ProyectoRAG/
├── ia_tienda.py          # Script principal con el sistema RAG
├── setup_db.py           # Script para inicializar la BD (si aplica)
├── requirements.txt      # Dependencias del proyecto
├── ecommerce.db          # Base de datos SQLite (generada)
├── data/                 # Carpeta con datos de productos
└── README.md             # Este archivo
```

## 🔍 ¿Cómo funciona?

### Paso 1: Embeddings
Las descripciones de productos se convierten a vectores numéricos usando `sentence-transformers`

### Paso 2: Búsqueda Vectorial
ChromaDB busca los `k` productos más similares al query del usuario usando similitud coseno

### Paso 3: LLM
Ollama (Llama2) toma los productos encontrados y genera una respuesta natural y personalizada

## 📝 Ejemplo de Uso

```python
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Crear embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Crear base de datos vectorial
textos = ["Producto 1", "Producto 2", "Producto 3"]
vectorstore = Chroma.from_texts(textos, embeddings)

# Buscar productos similares
pregunta = "Tu pregunta aquí"
resultados = vectorstore.similarity_search(pregunta, k=2)

# Generar respuesta con LLM
llm = Ollama(model="llama2")
# ... crear prompt y chain ...
respuesta = chain.run(...)
```

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Siéntete libre de hacer fork del proyecto y enviar pull requests.

---

**Nota**: Este es un proyecto educativo para entender cómo funcionan los sistemas RAG con LLMs.
EOF
