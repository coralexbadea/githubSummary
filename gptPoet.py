import subprocess

# from stableDiff import create_image

def get_added_code(dindArg="^+[^+].*"):
    try:
        # Run the "git diff" command to get added code
        git_diff_command = ["git", "diff", "--unified=0"]
        git_diff_process = subprocess.Popen(git_diff_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Run the "findstr" command to filter added code
        findstr_command = ["findstr", "/r", findArg]
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


def main():
    begin_prompt = "explain to me in summary what this code does:"
    message = get_added_code()
    if not message:
        message = get_added_code("^-[^-].*")
    prompt = begin_prompt + message 
    apy_key = input("API KEY:")

    code_summary = make_openai_post(apy_key, prompt)

    begin_prompt1 = "Write me a list of methaphoric words separated by comma describing the below code description. Remember I want only a list of methaphoric words separated by comma and nothing else:\nCode description:\n"
    begin_prompt2 = "write me a short poem that comprehends this code description without doing any reference to programming or  programming languages:"

    prompt1 = begin_prompt1 + code_summary 
    prompt2 = begin_prompt2 + code_summary 

    code_poet1 = make_openai_post(apy_key, prompt1)
    code_poet2 = make_openai_post(apy_key, prompt2)

    print("code poet done\n\n", code_poet1)
    print("code poet done\n\n", code_poet2)


    # create_image(code_poet)
    
main()
# get_added_code()