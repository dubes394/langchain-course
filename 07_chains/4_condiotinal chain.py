#description : developed a app where we get feedback from the user and then we classify it positive and negative and generate proper feedback based on that

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal


load_dotenv()

model1 = ChatOpenAI()

model2 = ChatAnthropic(model_name = "claude-sonnet-4-6")

parser1 = StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal['positive', 'negative'] = Field(description="Give the sentiment of the feedback")
    
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template = "Classify the sentiment of the following feedback text into positive or negative \n {feedback} {format_instruction}",
    input_variables = ['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model1 | parser2

prompt2 = PromptTemplate(
    template = "Write a appropriate to this positive feedback \n {feedback}",
    input_variables = ['feedback']
)
prompt3 = PromptTemplate(
    template = "Write a appropriate to this negative feedback \n {feedback}",
    input_variables = ['feedback']
)


branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model1 | parser1 ),
    (lambda x:x.sentiment == 'negative', prompt3 | model1 | parser1 ),
    RunnableLambda(lambda x: "could not find the value")
)

final_chain = classifier_chain | branch_chain 

print(final_chain.invoke({"feedback" : "This is wonderful phone"}))

final_chain.get_graph().print_ascii()
