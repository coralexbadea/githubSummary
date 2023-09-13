import argparse
from path_manipulation.copy import create_tree_copy

from summarise import set_variables, process_files_in_folder

def main():    
    parser = argparse.ArgumentParser(description="Description of your script.")
    parser.add_argument("--folder_path", help="Path to the folder")
    parser.add_argument("--global_type", help="Global type")
    parser.add_argument("--api_key", help="API Key")

    args = parser.parse_args()
    set_variables(args)
    folder_path = args.folder_path

    result_folder_path = create_tree_copy(folder_path)
    process_files_in_folder(result_folder_path)

if __name__ == "__main__":
    main()
