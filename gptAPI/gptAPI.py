import openai
import dotenv
import os 
dotenv.load_dotenv()  # Load variables from .env file into environment
api_key = os.getenv("API_KEY")


def make_openai_post(message, system_prompt="You are a helpful assistant"): 
    # Set your OpenAI API key
    api_key = os.getenv("API_KEY")
    print("here is your api KEY!!")
    openai.api_key = api_key
    messages = [ {"role": "system", "content": system_prompt} ]
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", temperature=0.0, messages=messages
        )
      
    reply = chat.choices[0].message.content
    return reply