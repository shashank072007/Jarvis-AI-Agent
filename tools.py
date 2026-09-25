import logging
import asyncio
import os
import smtplib
import requests
from livekit.agents import function_tool, RunContext
from langchain_community.tools import DuckDuckGoSearchRun
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText
from typing import Optional

@function_tool()
async def get_weather(
    context: RunContext, 
    city: str) -> str:
    """
    Get the current weather for a given city.
    """
    try:
        # Running synchronous requests in a thread to avoid blocking the event loop
        response = await asyncio.to_thread(requests.get, f"https://wttr.in/{city}?format=3")
        if response.status_code == 200:
            logging.info(f"Weather for {city}: {response.text.strip()}")
            return response.text.strip()   
        else:
            logging.error(f"Failed to get weather for {city}: {response.status_code}")
            return f"Could not retrieve weather for {city}."
    except Exception as e:
        logging.error(f"Error retrieving weather for {city}: {e}")
        return f"An error occurred while retrieving weather for {city}." 

@function_tool()
async def search_web(
    context: RunContext,
    query: str
) -> str:
    """Search the web using DuckDuckGo."""

    try:
        print("SEARCH TOOL CALLED:", query)

        search = DuckDuckGoSearchRun()

        results = await asyncio.to_thread(
            search.run,
            query
        )

        logging.info(f"Search results for '{query}': {results}")

        return results

    except Exception as e:
        logging.exception(f"Web search failed for '{query}'")
        return f"Search failed: {e}"
    
@function_tool()    
async def send_email(
    context: RunContext,
    to_email: str,
    subject: str,
    message: str,
    cc_email: Optional[str] = None
) -> str:
    """
    Send an email through Gmail.
    """
    
    # We define the blocking SMTP logic inside a separate function
    def _send_smtp_logic():
        try:
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            
            gmail_user = os.getenv("GMAIL_USER")
            # Checks both common variable names
            gmail_password = os.getenv("GMAIL_APP_PASSWORD") or os.getenv("GMAIL_PASSWORD")
            
            if not gmail_user or not gmail_password:
                return "Error: Gmail credentials not found in .env"
            
            msg = MIMEMultipart()
            msg['From'] = gmail_user
            msg['To'] = to_email
            msg['Subject'] = subject
            
            recipients = [to_email.strip()]
            if cc_email:
                msg['Cc'] = cc_email
                recipients.append(cc_email.strip())
            
            msg.attach(MIMEText(message, 'plain'))
            
            # Use 'with' for reliable connection closing
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(gmail_user, gmail_password)
                server.sendmail(gmail_user, recipients, msg.as_string())
            
            return "Success"
            
        except smtplib.SMTPAuthenticationError:
            return "Authentication failed. Check your App Password."
        except Exception as e:
            return str(e)

    # Run the blocking _send_smtp_logic in a background thread
    result = await asyncio.to_thread(_send_smtp_logic)

    if result == "Success":
        logging.info(f"Email sent successfully to {to_email}")
        return f"Email sent successfully to {to_email}"
    else:
        logging.error(f"Email error: {result}")
        return f"Email sending failed: {result}"