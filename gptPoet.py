import json
import subprocess

# from stableDiff import create_image

def get_added_code():
    try:
        # Run the "git diff" command to get added code
        git_diff_command = ["git", "diff", "--unified=0"]
        git_diff_process = subprocess.Popen(git_diff_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Run the "findstr" command to filter added code
        findstr_command = ["findstr", "/r", "^+[^+].*"]
        result = subprocess.run(findstr_command, stdin=git_diff_process.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Close the "git diff" process
        git_diff_process.stdout.close()
        
        # Check if the command was successful
        if result.returncode == 0:
            added_code = result.stdout
            return added_code
        else:
            print("Error running 'findstr':")
            print(result.stderr)
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    

import openai 
import os 
def make_openai_post(api_key, message, system_prompt="You are a helpful assistant"): 
    # Set your OpenAI API key
    api_key = api_key
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


def read_json(json_path):
    data = None
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data 


def main():
    jsonData = read_json('./prompts.json')
    begin_prompt = "explain to me in summary what this code does:"
    message = get_added_code()

    prompt = begin_prompt + message 
    apy_key = input("API KEY:")

    code_summary = make_openai_post(apy_key, prompt)

    begin_prompt = "write me a short poem that comprehends this code description without doing any reference to programming or  programming languages:"
    prompt = begin_prompt + code_summary 
    code_poet = make_openai_post(apy_key, prompt)
    print("code poet done\n\n", code_poet)

    # create_image(code_poet)
    
main()
# get_added_code()