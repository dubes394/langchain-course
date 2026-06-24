# we are building one llm component class and one prompt component class and then using runnables we connect them and make a llm App
import random
class Dummy_LLM():
    
    def __init__(self):
        print("LLM created")
    
    def predict(self, prompt):
        
        response_list = [
            "Ottawa is capital of Canada",
            "AI stands for artifical intelligence",
            "IPL is a cricket league"
        ]
        
        return{"response" : random.choice(response_list)}
    
class Dummy_PromptTemplate():
    
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables
        
    def format(self, input_dict):
        return self.template.format(**input_dict)
    
template =Dummy_PromptTemplate(
    template="Write a  {length} poem on {topic}",
    input_variables=['length', 'topic']
)

prompt = template.format({'length' : 'short', 'topic':'cricket'})
print(prompt)

llm = Dummy_LLM()
print(llm.predict("what is day today"))

chain = Dummy_LLM(llm, template)

chain.run({'length': 'short', 'topic':'india'})


        
        