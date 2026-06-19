from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt1 = template1.invoke({'topic' : 'mars'})

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Give a 5 lines summary of /n {text}',
    input_variables=['text']
)

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text' : result.content})

result1 = model.invoke(prompt2)

print(result1.content)
