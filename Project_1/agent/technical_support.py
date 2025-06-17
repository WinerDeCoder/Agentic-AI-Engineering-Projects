from pydantic import BaseModel, Field
from utils.product_config import product_name_from_id
from agents import Agent, Runner, RunContextWrapper, function_tool
from utils.data_class import TechnicalSupport
import asyncio


INSTRUCTION = """You are a product technical supporter . 
You will receive comment from customer about a product - usually question, feedback or complain.
Then you will try your best, use your own base knowledge to answer the customer's question.
Note that you must always return a good answer, even if you don't know.
Only return a technical answer, no need to interact with customer."""

technical_agent = Agent(
    name = "Product Technical Support",
    instructions = INSTRUCTION,
    model = "gpt-4o-mini",
    output_type = TechnicalSupport,
)

async def Product_technical_support(product_id: int, comment: str) -> str:
    product_name = product_name_from_id(product_id)
    
    result = await Runner.run(technical_agent, f"This is the product name: {product_name}, and this is the comment from customer: {comment}")
    return result.final_output
