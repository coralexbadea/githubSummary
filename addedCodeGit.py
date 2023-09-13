import subprocess

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

# Get and print the added code
# added_code = get_added_code()
# if added_code is not None:
#     print("Added Code:")
#     print(added_code)
