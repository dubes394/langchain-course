from typing import TypedDict

class person(TypedDict):
    name : str
    age : int
    
new_person: Person  = {'name': 'nitish', 'age': 45}

print(new_person)