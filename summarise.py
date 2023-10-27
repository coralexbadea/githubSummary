import glob
import os
import sys
import requests
import openai
import os
# from dotenv import load_dotenv
# load_dotenv()

def set_variables(args):
    global folder_path
    global global_type
    global api_key

    folder_path = args.folder_path
    global_type = args.global_type
    api_key = args.api_key

comment_symbols = {
    ".py": '#',     # Python
    ".java": '//',  # Java
    ".js": '//',    # JavaScript
    ".jsx": '//',    # JavaScript
    ".ts": '//',    # TypeScript
    ".tsx": '//',    # TypeScript
    ".c": '//',     # C
    ".cpp": '//',   # C++
    ".cs": '//',    # C#
    ".php": '//',   # PHP
    ".rb": '#',     # Ruby
    ".go": '//',    # Go
    ".swift": '//', # Swift
    ".kt": '//',    # Kotlin
    ".pl": '#',     # Perl
    ".rust": '//',  # Rust
    ".scala": '//', # Scala
    ".html": '<!--',# HTML
    ".css": '/*',   # CSS
    ".sql": '--',   # SQL
}
language_extensions = comment_symbols.keys()

global global_type
global api_key
global folder_path


globalType = 'llama'
api_key = None

def add_double_slashes(text, simbol='//'):
    lines = text.split('\n')  # Split the text into lines
    commented_lines = [simbol + ' ' + line for line in lines]  # Add "//" before each line
    return '\n'.join(commented_lines)  # Join the lines back together

# Function to add "This is a file" to the beginning of a file
def add_comments_to_file(file_path, file_extension):
    with open(file_path, 'r+') as file:
        content = file.read()
        file.seek(0, 0)
        response = make_api_post(instr=f"{content}")
        commentedResponse = add_double_slashes(response, simbol=comment_symbols[file_extension])
        file.write(commentedResponse + content)

# Function to process files in a folder tree recursively
def process_files_in_folder(folder_path):
    for file_path in glob.glob(f'{folder_path}/**/*', recursive=True):
        _, file_name = os.path.split(file_path)
        _, file_extension = os.path.splitext(file_name)
        if(file_extension in language_extensions):
            add_comments_to_file(file_path, file_extension)
            print(f"Processed: {file_path}")
            
def make_api_post(instr=None):
    if globalType=='openai':
        return make_openai_post(instr)
    else :
        return make_llama_post(instr)
        
def make_openai_post(message): 
    # Set your OpenAI API key
    global api_key
    print("here is your api KEY!!")
    openai.api_key = api_key
    messages = [ {"role": "system", "content": "You are a intelligent assistant speciallised on code explanation. You write a list of explanations only."} ]
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", temperature=0.0, messages=messages
        )
      
    reply = chat.choices[0].message.content
    reply = reply.replace("Here is a", "-")
    return reply
  

def make_llama_post(instr=None, headers=None):
    url = "https://www.llama2.ai/api"
    data = {
        "prompt": f"[INST] Explain code: {instr} [/INST]\n",
        "version": "2796ee9483c3fd7aa2e171d38f4ca12251a30609463dcfd4cd76703f22e96cdf",
        "systemPrompt": "You are a helpful assistant.",
        "temperature": 0.75,
        "topP": 0.9,
        "maxTokens": 800
    }
    try:
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            return response.text
        else:
            response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return ""
    
  
    
