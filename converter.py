import os
import sys
import json

# convert .json files to .txt files
input_path = "D:/ProjectKuliah/BigData/raw_json"
output_path = "D:/ProjectKuliah/BigData/converted_txt"

for filename in os.listdir(input_path):
    with open(os.path.join(input_path, filename), 'r', encoding="utf8") as infile:
        with open(os.path.join(output_path, filename[:-4] + "txt"), 'w', encoding="utf8") as outfile:
            data = json.load(infile)
            outfile.write(json.dumps(data))
            outfile.write('\n')
