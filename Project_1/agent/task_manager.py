from agents import Agent, RunContextWrapper, Runner, function_tool
from dataclasses import dataclass
from typing import List, Dict, Any
from pydantic import BaseModel, Field
import asyncio
from .mail_writer import Active_Mail_Writer
from .technical_support import Product_technical_support
from utils.data_class import TechnicalSupport, CustomerContext
from utils.send_mail import send_email


async def task_manager(customer_context: CustomerContext):

    if customer_context.comment != "":

        # Run the technical support agent
        technical_response = await Product_technical_support(
            product_id=customer_context.product_id,
            comment=customer_context.comment
        )


    mail_content = await Active_Mail_Writer(customer_context, technical_response)
    
    await send_email(customer_context, mail_content)