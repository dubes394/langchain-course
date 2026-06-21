from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers.structured import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatOpenAI()

#first step to create schema to guide llm 
 
schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic"),
    
]

template = PromptTemplate(
    template = "Give 3 fact about {topic} \n {format_instruction}",
    variables = ["topic"],
    partial_variables = {"format_instruction":parser.get_format_instruction()}
)

chain = template | model | parser 

result = chain.invoke({"topic" : "mars"}) 
print(result)