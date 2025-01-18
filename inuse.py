import os
import re
import pandas as pd

filename = 'Localizable.strings'

def read_file_to_dict(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.split('=')
                key = key.strip().strip('"')
                value = value.strip().strip('"').strip('";')
                data[key] = value
    return data

data_dict = read_file_to_dict(filename)

df = pd.DataFrame(list(data_dict.items()), columns=['Key', 'Value'])

df.to_excel('output.xlsx', index=False, engine='openpyxl')

print("Excel file created successfully!")

