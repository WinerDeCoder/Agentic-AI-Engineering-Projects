import asyncio
from dataclasses import dataclass
from agents import Agent, RunContextWrapper, Runner, function_tool
from utils.data_class import CustomerContext


GOOD_INSTRUCTION = """You are a mail writer, and you currently working for Trustify Technology.
You will receive some information of the customer like their name, their rating and their comment also.
You may receive a response from Technical Support to reply to the customer, include this to the mail to response customer comment.
You will write an email to the customer to thank them for their good rating and helpful comment when using the company's product.

Write email in HTML format
"""

BAD_INSTRUCTION = """You are a mail writer, and you currently working for Trustify Technology.
You will receive some information of the customer like their name, their rating and their comment also on a company product, and note that this will be bad rating.
You may receive a response from Technical Support to reply to the customer, include this to the mail to response customer comment.
You will write an email to the customer to apologize for their bad rating and comment when using the company's product.

Write email in HTML format
"""


def dynamic_instructions(
    context: RunContextWrapper[CustomerContext], agent: Agent[CustomerContext]
) -> str:

    return GOOD_INSTRUCTION if int(context.context.rating) >= 4 else BAD_INSTRUCTION

technical_agent = Agent[CustomerContext](
    name = "Mail Writer Agent",
    instructions = dynamic_instructions,
    model = "gpt-4o-mini",    
)

async def Active_Mail_Writer(customer_context: CustomerContext, technical_response: None) -> str:
    result = await Runner.run(
        technical_agent, 
        input = f"""Write an email to the customer with the customer's information:
- Name: {customer_context.name}
- Rating: {customer_context.rating}
- Comment: {customer_context.comment}
Here is the response from Technical Support for the customer's feedback - include this to the email: {technical_response}""" \
                if technical_response else f"""Write an email to the customer with the customer's information:
- Name: {customer_context.name}
- Rating: {customer_context.rating}
- Comment: {customer_context.comment}""",
        context = customer_context)
    
    print(result.final_output)
    return result.final_output