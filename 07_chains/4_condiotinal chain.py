from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


load_dotenv()

model1 = ChatOpenAI()

model2 = ChatAnthropic(model_name = "claude-sonnet-4-6")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = "Classify the sentiment of the  "
)