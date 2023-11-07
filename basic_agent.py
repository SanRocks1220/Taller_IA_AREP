from fileinput import close
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import tool
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pinecone import Pinecone
import pinecone
import os

@tool("SayHello", return_direct=True)
def say_hello(name:str) -> str:
    """Answer when someone says hello"""
    return f"Hello {name}! My name is Sainapsis"
    
def docsToPinecone():
    docs = [
        "documents\economia.txt", 
        "documents\ingenieria-civil.txt", 
        "documents\ingenieria-electrica.txt", 
        "documents\ingenieria-electronica.txt", 
        "documents\ingenieria-industrial.txt", 
        "documents\ingenieria-sistemas.txt"
    ]
    dataList = []
    pinecone.init(api_key = os.getenv('PINECONE_API_KEY'), environment = os.getenv('PINECONE_ENVIRONMENT'))
    embeddings = OpenAIEmbeddings()
    for doc in docs: 
        with open(doc, 'r', encoding='UTF-8', errors='ignore') as file:
            text = file.read()
        data = Pinecone.from_texts(texts = [text], embedding = embeddings, index_name = "documentos")
        dataList.append(data)
    print(data)

def buscar():
    pinecone.init(api_key='PINECONE_API_KEY', environment='PINECONE_ENVIRONMENT')
    embeddings = OpenAIEmbeddings()
    # if you already have an index, you can load it like this
    docsearch = Pinecone.from_existing_index("documentos", embeddings)
    query = "Cuantos años de acreditación tiene ingeniería de industrial?"
    docs = docsearch.similarity_search(query)
    print(docs)

def main():
    llm = ChatOpenAI(temperature=0)
    tools = [
        say_hello
    ]
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True
    )
    print(agent.run("Hello! My name is Santiago"))
    

buscar()