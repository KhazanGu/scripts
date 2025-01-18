import os
import re
import pandas as pd

rep = dict()

file_path = 'translate.xlsx' 

ignore_directorys = {'.git', 'Wallet.xcodeproj', 'Assets.xcassets','fastlane', 'WalletTests', 'WalletUITests', 'HDWalletKit'}
ignore_files = ('.strings', '.plist', '.DS_Store', '.ttf', '.storyboard', 'Gemfile.lock', 'Gemfile', 'search.py', 'README.md', '.xlsx', '.py')

df = pd.read_excel(file_path)

for i, row in df.iterrows():
    key = f"localized(key: \"{row[0]}\")"
    value = f"localized(key: \"{row[1]}\")"
    rep[key] = value
    
print(rep)

def replace(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

        modified_content = file_content
        
        for key, value in rep.items():
            pattern = re.escape(key)
            if re.search(pattern, modified_content):  # Debugging check to see if the pattern exists
                print(f"Found pattern '{key}' in file {file_path}. Replacing with '{value}'.")
                modified_content = re.sub(pattern, value, modified_content)
            else:
                print(f"Pattern '{key}' not found in file {file_path}.")

        if modified_content != file_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(modified_content)
            print(f"Changes saved to file: {file_path}")
        else:
            print(f"No changes made to file: {file_path}")


def all_files():
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in ignore_directorys]
        for file in files:
            if not file.endswith(ignore_files):
                path = os.path.join(root, file)
                # print(path)
                replace(path)



all_files()
