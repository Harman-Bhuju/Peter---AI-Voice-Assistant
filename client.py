from dotenv import load_dotenv
import os
from google import genai
import time
load_dotenv()

client = genai.Client(api_key=os.getenv("gemini_api"))

def ask_peter(user_input):
    system_prompt = """
        You are Peter.

        Give direct answers only.

        Do not introduce yourself.
        Do not say 'I'm Peter'.
        Do not use greetings.
        Do not use markdown.
        Do not use any symbols like (*,/#@ or anything).
        Keep answers short and conversational.
     """
    contents=[
        system_prompt,
        user_input
    ]
    for _ in range(2):
            try:
                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=contents,
                )
                return response.text

            except Exception as e:
                print("Error:", e)
                time.sleep(2)

    return "Sorry, I couldn't respond right now."



