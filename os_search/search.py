import os
import fnmatch

def search_word_in_files(root_dir, target_word):
    matching_files = []
    
    for root, _, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if target_word in content:
                        matching_files.append(file_path)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    return matching_files