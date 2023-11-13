# Taller Sainapsis
Organizadores:
+ David Esteban Useche – Líder técnico - david.useche@sainapsis.com
+ Santiago Velez – CoFounder – santiago.velez@sainapsis.com

## Planteamiento 
El objetivo de este taller es aprender a utilizar Langchain (herramienta fundamental para crear agentes que usen la técnica de Retrieval Augmented Generation, también llamada RAG) además de evaluar buenas prácticas y clean code de Python.  

Las siguientes tareas y desafíos le ayudarán a afianzar el conocimiento en los campos mencionados anteriormente.  

El objetivo final es la creación de un API REST que acepte por input un mensaje de usuario final (para ser procesado por orquestador (api de python que corra un agente de [Langchain](https://python.langchain.com/docs/get_started/introduction)) y utilizando una base de datos de vectores y los endpoints de OpenAI para su LLM, genere una respuesta.


## Desafío #1
Crear una base de datos de vectores en [Pinecone Starter Version](https://www.pinecone.io/) usando su correo institucional, cargar los documentos anexos (FAQs de universidades) usando Embeddings de OpenAI y Langchain. Configurar una Tool de langchain que consulte los documentos y genere una respuesta.

## Prerequicitos:
Es necesario tener instaladas las siguientes librerías en nuestros entornos de trabajo:
```
pip install ChatOpenAI
pip install AgentType
pip install initialize_agent
pip install tool
pip install OpenAIEmbeddings
pip install Pinecone
```

## Desarrollo
1. Primero, configuramos la API key de OpenAI en Windows como variable de entorno, limitada al uso en la clase del laboratorio:
```
$env:OPENAI_API_KEY = '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'
```
2. Luego, replicamos el agente básico que se nos presentó, haciendo uso de:
    + Langchain: Agents, Tools, Embeddings y Vectorstores - Pinecone  
    ![image](https://github.com/SanRocks1220/Taller_IA_AREP/assets/99696682/448417a3-6d59-461e-8d0b-69c4f7cf4a7c)

3. Nos disponemos a añadir los documentos proporcionados referentes a información de los diferentes programas en la ECI:
   + ![image](https://github.com/SanRocks1220/Taller_IA_AREP/assets/99696682/ce19071d-2a4e-4884-87b3-a9f532d39d4a)
   + ![image](https://github.com/SanRocks1220/Taller_IA_AREP/assets/99696682/3d300dbc-8cf0-4a51-9389-0e89845916ca)
4. Creamos una base de datos de Vectores en Pinecone, ingresando con nuestra cuenta institucional:
   + Nombre (index): documentos
   + API Key: dcf9****-****-****-****-********8ac3
   + Environment: gcp-starter
   + ![image](https://github.com/SanRocks1220/Taller_IA_AREP/assets/99696682/a4d68a44-3e9d-420c-b278-d58fda8c8b39)
5. Configuramos la API key de Pinecone y el environment en Windows como variables de entorno:
```
$env:PINECONE_API_KEY = <API KEY de Pinecone Aquí>
$env:PINECONE_ENVIRONMENT = 'gcp-starter'
```
6. Vectorizamos estos documentos y los subimos a la base de Datos recién creada:
   +  ![image](https://github.com/SanRocks1220/Taller_IA_AREP/assets/99696682/42098ba9-9eba-4ce2-b16b-656603b36385)
   +  ![image](https://github.com/SanRocks1220/Taller_IA_AREP/assets/99696682/07214b4d-6fdc-4de4-b697-0e5440ce2542)
   +  ![image](https://github.com/SanRocks1220/Taller_IA_AREP/assets/99696682/45d7621a-fbc0-4fd9-b37f-10f59a96ac9a)

7. Creamos un método de búsqueda con OpenAI, Pinecone y sus agentes, en búsqueda de implementar un nuevo tool:
   + ![image](https://github.com/SanRocks1220/Taller_IA_AREP/assets/99696682/b1d1af40-019a-496c-8042-6e0eb1512e8c)

## Evidencias de Funcionamiento
No se puede tener evidencias de funcionamiento a la fecha de la realización de este taller por diferentes motivos:
1. Al momento de probar las consultas, se indicaba que el número de consultas máximas había sido alcanzado. Este problema persistió a lo largo de la clase, impidiendo consultar correctamente.
2. La API Key de OpenAI fue revocada una vez se finalizó la clase de laboratorio por lo que mayor exerimentación fue imposible, y pagar por consultas propias no era una opción.



## Autor
- [Santiago A. Rocha](https://github.com/SanRocks1220)


## Colaboradores
- [David E. Valencia](https://github.com/DavidVal6)
