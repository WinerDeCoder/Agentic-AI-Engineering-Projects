from pydantic import BaseModel, Field
from ..utils.product_config import product_name_from_id
from agents import Agent


INSTRUCTION = """You are a product technical supporter . 
You will receive comment from customer about a product - usually question, feedback or complain.
Then you will try your best, use your own base knowledge to answer the customer's question.
Note that you must always return a good answer, even if you don't know.
Only return a technical answer, no need to interact with customer."""

technical_agent = Agent(
    name = "Product Technical Support",
    instruction = INSTRUCTION,
    model = "gpt-4o-mini"
)

def Product_technical_support(product_id: str, comment: str) -> str:
    product_name = product_name_from_id(product_id)
    
    