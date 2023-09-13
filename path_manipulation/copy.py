import shutil
import os 

def copy_file(source_path, destination_path):
    try:
        # Copy the file from source to destination
        shutil.copy(source_path, destination_path)
        print(f"File '{source_path}' copied to '{destination_path}' successfully.")
    except FileNotFoundError:
        print(f"File '{source_path}' not found.")
    except PermissionError:
        print(f"Permission denied while copying '{source_path}' to '{destination_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_tree_copy(folder_path, destination_folder=None):
    import shutil
    # Source folder
    source_folder = f'{folder_path}'
    if not destination_folder:
        destination_folder = f'{folder_path}_copy'


    # Delete the existing destination directory if it exists
    if os.path.exists(destination_folder):
        shutil.rmtree(destination_folder)
    try:
        # Copy the entire folder tree from source to destination
        shutil.copytree(source_folder, destination_folder)
        print(f"Folder '{source_folder}' copied to '{destination_folder}' successfully.")
        return destination_folder
    except Exception as e:
        print(f"Error copying folder: {e}")
  