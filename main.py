from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


model = ChatOpenAI(model="gpt-4o-mini-2024-07-18")

parser = StrOutputParser()

system_template = "Translate the following into {language}:"
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_template), 
        ("user", "{text}")
    ]
)

chain = prompt | model

result = chain.invoke({"language": "Urdu", "text": "What is your name ?"})

print (result)