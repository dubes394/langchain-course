from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

model = ChatOpenAI()

# USING NORMAL TYPED DICT
# class Review(TypedDict): 
    
#     summary : str 
#     sentiment : str
    
# structured_model = model.with_structured_output(Review)

# result = structured_model.invoke("The hardware great, but software sucks. especially while multi tasking. Also camera quality can be improved")

# print(type(result))
# print(result['summary'])
# print(result['sentiment'])

# USING ANNOTATED TYPEDICT, WHICH IS GUIDING THE LLM FOR A OUTPUT

class Review(TypedDict):
    
    key_themes : Annotated[list[str], "Give all important specifications in a list "]
    summary : Annotated[str, "A brief summary of the review"]
    sentiment : Annotated[str, "return sentiment in 3 ways, positive or negative or neutral"]
    pros : Annotated[Optional[list[str]], "Give me list of all pros in a list"]
    cons : Annotated[Optional[list[str]], "Give me list of all cons in a list "]
    name : Annotated[Optional[list[str]], "Provide me name of reviewer in upper case"]
    
    
structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, its an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Cons:
Heavy and bulky
UI is laggy and may not be compatible with few apps
The S pens glitches sometimes        
                                 
                                 
Review by Nitish Singh""")

print(result.keys())