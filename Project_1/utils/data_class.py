import json
from dataclasses import dataclass, field
from pydantic import BaseModel, Field
    

class TechnicalSupport(BaseModel):
    product: str
    comment: str
    response: str 

@dataclass
class CustomerContext:
    name: str
    email: str
    rating: str
    comment: str
    product_id: int