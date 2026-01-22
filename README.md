# ProyectoRAG - Sistema de Recomendación de Productos con IA

Un sistema inteligente de búsqueda y recomendación de productos basado en **RAG (Retrieval-Augmented Generation)** que utiliza embeddings vectoriales y modelos de lenguaje para entender consultas naturales.

## 🎯 ¿Qué es este proyecto?

Este proyecto implementa un **sistema RAG** que:

1. **Convierte productos a vectores** usando embeddings de `sentence-transformers`
2. **Busca productos similares** a la consulta del usuario usando búsqueda vectorial con ChromaDB
3. **Genera recomendaciones personalizadas** usando un LLM (Llama2 con Ollama)

### Flujo completo:

```
Pregunta del usuario
    ↓
Embeddings (texto → números)
    ↓
Búsqueda vectorial (encontrar productos similares)
    ↓
LLM (generar respuesta natural)
    ↓
Recomendación personalizada
```

## 🚀 Requisitos

- Python 3.9+
- Ollama (para el LLM)
- Las librerías en `requirements.txt`

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/ProyectoRAG.git
cd ProyectoRAG
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate  # En macOS/Linux
# o
.venv\Scripts\activate  # En Windows
```

### 3. Instalar librerías

```bash
pip install -r requirements.txt
```

### 4. Instalar Ollama

Descarga Ollama desde: https://ollama.ai

Luego, inicia el servidor:

```bash
ollama serve
```

En otra terminal, descarga el modelo Llama2:

```bash
ollama pull llama2
```

## 🎮 Uso

### Ejecutar el script

```bash
python ia_tienda.py
```

### Modificar la pregunta

Edita la línea en `ia_tienda.py`:

```python
pregunta = "ropa para hacer deporte y correr cuando hace sol"
```

Cambia el texto a tu consulta deseada.

## 📂 Estructura del proyecto

```
ProyectoRAG/
├── ia_tienda.py          # Script principal con RAG
├── setup_db.py           # Script para crear la BD de productos
├── requirements.txt      # Dependencias
├── ecommerce.db          # Base de datos (SQLite)
├── data/                 # Datos del proyecto
└── README.md             # Este archivo
```

## 🔧 Componentes principales

### `ia_tienda.py`

- **HuggingFaceEmbeddings**: Convierte texto a vectores usando `sentence-transformers`
- **ChromaDB**: Base de datos vectorial en memoria para búsqueda rápida
- **Ollama (Llama2)**: LLM que genera respuestas naturales
- **LLMChain**: Cadena que une prompt + LLM

### `setup_db.py`

Script para crear y poblar la base de datos de productos.

## 🤔 ¿Qué es `k=2`?

En `vectorstore.similarity_search(pregunta, k=2)`:

- **k=2** → devuelve los 2 productos más similares a la pregunta
- **k=1** → devuelve solo 1 resultado
- **k=5** → devuelve los 5 más similares

Los resultados se ordenan por **relevancia** (de mayor a menor similitud).

## 📊 Ejemplo de uso

**Entrada:**
```
Pregunta: "ropa para hacer deporte y correr cuando hace sol"
```

**Proceso:**
1. Se convierte la pregunta a vector
2. Se buscan los 2 productos más similares
3. El LLM genera una recomendación personalizada

**Salida:**
```
=== RESPUESTA DEL LLM ===
Para correr cuando hace sol, te recomiendo la Gorra Running porque 
tiene material transpirable que mantiene tu cabeza fresca. La Camiseta 
Eco es perfecta porque el algodón orgánico es cómodo y respirable...
```

## 🛠️ Tecnologías utilizadas

- **Python 3.9+**
- **LangChain** - Framework para IA
- **sentence-transformers** - Embeddings de texto
- **ChromaDB** - Base de datos vectorial
- **Ollama + Llama2** - LLM local gratuito
- **pandas** - Manipulación de datos

## 📝 Licencia

Este proyecto es de código abierto.

## 🤝 Contribuciones

Si quieres mejorar el proyecto, ¡adelante! Puedes:

1. Hacer un fork del repositorio
2. Crear una rama con tu mejora
3. Hacer un commit con tus cambios
4. Hacer push y crear una Pull Request

## ❓ Preguntas frecuentes

**¿Por qué tarda en la primera ejecución?**

Porque descarga el modelo de embeddings (~100MB) la primera vez.

**¿Puedo usar otro LLM?**

Sí, puedes cambiar `Ollama(model="llama2")` por:
- `OpenAI()` (requiere API key)
- `HuggingFaceLLM()` (otros modelos open-source)

**¿Funciona sin internet?**

Sí, una vez que tengas Ollama y los modelos descargados.

