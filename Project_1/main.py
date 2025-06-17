from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner, trace, function_tool, OpenAIChatCompletionsModel, input_guardrail, GuardrailFunctionOutput
from typing import Dict
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
from pydantic import BaseModel
import os
import time
import shutil
import csv
import pandas as pd
import json
from utils.excel_handle import Excel_Customer_Handler
from utils.data_class import CustomerContext
from agent.task_manager import task_manager
import asyncio

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')



# Get the file path from the environment variable
file_path = "data/customer.xlsx"  # Ensure this points to a valid .csv file

async def main():

    df = Excel_Customer_Handler(file_path)

    for index, row in df.iterrows():
        date, email, name, rating, comment, product_id = row["Date"], row["Email"], row["Name"], \
                                                        float(row["Rating"]), row["Comment"], row["Product_ID"]
                                                        
        customer_feedback = CustomerContext(name=name, email=email, rating=rating, comment=comment, product_id=product_id)

        # Analyse Comment
        await task_manager(customer_feedback)
        
        
if __name__ == "__main__":
    asyncio.run(main())
