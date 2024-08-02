import getpass
import os
from langchain_community.embeddings import OpenAIEmbeddings
from app import APP

api_key = "sk-proj-HJDZRZXAzIsjRsX36xhRT3BlbkFJPBY0fIauMJh2JirMPmEV"
os.environ["OPENAI_API_KEY"] = api_key
embeddings = OpenAIEmbeddings()
