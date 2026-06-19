from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    
    name : str = "kunal" 
    age : Optional[int] = None
    Email : EmailStr
    cgpa : float = Field(gt=0, lt=10, description= "A decimal value representing the cgpa of a student")
    
new_student = {"age" : 32, "cgpa" : 8}

student = Student(**new_student)

print(student)
