from pydantic import BaseModel, Field
from agents import Agent
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from .data_class import CustomerContext
import os
from dotenv import load_dotenv
load_dotenv("../.env")

sendgrid_api_key = os.getenv('SENDGRID_API_KEY')

async def send_email(customer_context: CustomerContext, mail_content: str) -> None:

    message = Mail(
        from_email='phucbao04321@gmail.com',
        to_emails=customer_context.email,
        subject='Sending with Twilio SendGrid is Fun',
        html_content= mail_content)
    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(e.message)