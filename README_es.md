
Asistente conversacional de preguntas y respuestas sobre datos de facturas, construido con la API de OpenAI modelo gpt 5-mini. Fase 1 de un proyecto en dos fases: esta versión responde preguntas usando el Excel estructurado que genera invoice-extractor (el proyecto complementario — número, fecha, emisor, total). La fase 2 lo ampliará a búsqueda de texto completo sobre los PDF originales con embeddings, para tener RAG de verdad.

Qué hace
Lee el Excel de facturas (data/factures.xlsx) y convierte cada fila en una línea de texto claramente etiquetada (Número: ... | Fecha: ... | Emisor: ... | Total: ... | Formato: ...)
Construye un system prompt que le da al modelo estos datos como única fuente de verdad, con la instrucción explícita de no inventar información y de copiar literalmente cualquier valor que cite, sin reordenarlo ni reformatearlo.
Ejecuta un bucle de conversación: el usuario hace preguntas en lenguaje natural desde la terminal; el modelo responde basándose solo en los datos de las facturas; el historial de la conversación se mantiene entre preguntas (para que funcionen preguntas de seguimiento como "¿y su fecha?"), hasta que el usuario escribe exit o salir.
Estructura del proyecto
chatbot/
├── data/
│   └── factures.xlsx     # copia del resultado de invoice-extractor (no se genera aquí)
├── src/
│   ├── config.py           # rutas base + carga de la clave de OpenAI desde .env
│   ├── excel_reader.py      # filas del Excel → contexto de texto etiquetado
│   └── main.py               # construye el prompt, llama a la API y ejecuta el chat
├── .env.example
├── requirements.txt
└── README.es.md

Uso
Asegúrate de que data/factures.xlsx contiene tus datos de facturas (generado por invoice-extractor, o en el mismo formato de 5 columnas: Fecha, Formato, Emisor, Total, Numero).
Ejecuta desde la raíz del proyecto:
bash
python src/main.py
Haz preguntas en la terminal. Escribe exit o salir para terminar.
Limitaciones conocidas
Depende de un proyecto aparte para su fuente de datos — este repo no extrae PDFs por sí mismo, solo lee un Excel ya generado.
El orden de las columnas está fijado para coincidir con el formato de salida de invoice-extractor; un Excel con las columnas en otro orden produciría respuestas incorrectas sin avisar, a menos que se detecte el desajuste.
Sin búsqueda semántica — esto es la fase 1, trabajando sobre una tabla pequeña y estructurada que se manda completa en cada petición. No escala a un corpus grande de PDFs; de eso se encarga la fase 2.
Usa gpt-5-mini por defecto, por eficiencia de coste durante el desarrollo; el modelo todavía no es configurable vía .env.
Próximos pasos
Fase 2 — RAG de verdad: ampliar el asistente para buscar en el texto completo de los PDF originales (reutilizando extract_invoice de invoice-extractor) con embeddings y una base de datos vectorial, permitiendo preguntas abiertas sobre el contenido de las facturas más allá de los 5 campos estructurados.
Hacer el modelo de chat configurable por variable de entorno.
Añadir un paso de validación ligero que marque cuando un valor citado no coincide con la línea de origen, para detectar automáticamente errores de parafraseo del modelo.
Stack

Python 3.12 · openai · openpyxl · python-dotenv
