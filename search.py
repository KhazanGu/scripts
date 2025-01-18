import os
import re
import pandas as pd

ignore_directorys = {'.git', 'Wallet.xcodeproj', 'Assets.xcassets','fastlane', 'WalletTests', 'WalletUITests', 'HDWalletKit'}
ignore_files = ('.strings', '.plist', '.DS_Store', '.ttf', '.storyboard', 'Gemfile.lock', 'Gemfile', 'search.py', 'README.md', '.xlsx')

localized = set()
words = set()

file_name = "A_Localizable.strings"
excel_name = "words.xlsx"

def reg(pattern, content):
    matches = re.findall(pattern, content)
    return matches


def read(path):
    pattern = r"localized\(key:.*?\)"

    with open(path, "r") as file:
        content = file.read()

    matches = reg(pattern, content)

    # print(matches)
    localized.update(set(matches))


def all_files():
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in ignore_directorys]
        for file in files:
            if not file.endswith(ignore_files):
                path = os.path.join(root, file)
                # print(path)
                read(path)


def write(file_path):
    with open(file_path, 'w') as file:
        for item in words:
            # print(item)
            file.write(f"\"{item}\" = \"{item}\";\n")

def inExcel():
    df = pd.DataFrame(list(words), columns=["英文"])

    df.to_excel(excel_name, index=False)

all_files()

# print(localized)

for e in localized:
    all = set(reg(r"\".*?\"", e))
    res = map(lambda s: s[1:-1], all)
    words.update(res)

words.remove("")

print(words)

write(file_name)

inExcel()