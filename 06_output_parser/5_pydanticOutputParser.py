from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

class Person(BaseModel):
    
    name : str = Field(description= " Name of the person")
    age :  int = Field(gt=18, description= ' Age of the person')
    city : str = Field(description="Name of the city the person lives in")
    
parser = PydanticOutputParser(pydantic_object = Person)

template = PromptTemplate(
    template = "Generate name, age and city of a fictional person. Give it retro person,say {place} in 1950s {format_instruction}",
    input_variables = ["topic"],
    partial_variables = {"format_instruction":parser.get_format_instructions()}
    
)

chain = template | model | parser
# prompt = template.invoke({"place":"Canada"})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)
final_result = chain.invoke({"place" : "India"})
print(final_result)