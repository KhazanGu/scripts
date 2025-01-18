import os
import re
import pandas as pd

translate_en = dict()
translate_zh = dict()

file_path = 'sync.xlsx' 

file_name_en = "Localizable_en.strings"
file_name_zh = "Localizable_zh.strings"

def read(file_path):
    df = pd.read_excel(file_path)

    for i, row in df.iterrows():
        # print(i)
        key = row[0]
        value = row[1]
        translate_en[key] = value
        translate_zh[key] = key


def write(file_path, data):
    with open(file_path, 'w') as file:
        for key in data:
            value = data[key]
            file.write(f"\"{key}\" = \"{value}\";\n")


read(file_path)

write(file_name_en, translate_en)
write(file_name_zh, translate_zh)

# print(rep)