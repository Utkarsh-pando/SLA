import os
import json
import csv
import pandas as pd

class NERDataConverter:
    def __init__(self, folder_path, json_folder, csv_output_path, ner_data_raw="NER DATA RAW"):
        self.folder_path = folder_path
        self.json_folder = json_folder
        self.csv_output_path = csv_output_path
        self.ner_data_raw = ner_data_raw

    def preprocess(self, data):
        processed_data = {}
        for key, value in data.items():
            value = value.replace("\\t", " ").strip()
            if value:
                processed_data[key] = value
        return processed_data

    def convert_to_json(self):
        txt_files = [file for file in os.listdir(self.folder_path) if file.endswith(".txt")]

        for txt_file in txt_files:
            file_path = os.path.join(self.folder_path, txt_file)
            with open(file_path, "r") as file:
                file_contents = file.read()
                lines = file_contents.split("\n")

            json_filename = txt_file.replace(".txt", ".json")
            json_path = os.path.join(self.json_folder, json_filename)

            lines_list = [line.strip() for line in lines if line.strip()]

            with open(json_path, "w") as json_file:
                json.dump(lines_list, json_file, indent=4)
   
    def convert_to_csv(self):
        csv_data = []

        json_files = [file for file in os.listdir(self.json_folder) if file.endswith(".json")]

        for json_file in json_files:
            json_path = os.path.join(self.json_folder, json_file)
            with open(json_path, "r") as file:
                json_data = json.load(file)  
                for index, value in enumerate(json_data, start=1):
                    csv_data.append([str(index), value, json_file])  

        with open(self.csv_output_path, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Sentence", "Token", "Filename"])
            csv_writer.writerows(csv_data)



class NERDataAnalyzer:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def read_csv(self):
        df = pd.read_csv(self.csv_path)
        
        new_rows = []
        for index, row in df.iterrows():
            values = row["Token"].split(" ")
            for value in values:
                if value.strip():
                    new_rows.append({"Sentence": row["Sentence"], "Token": value, "Filename": row["Filename"]})
        
        new_df = pd.DataFrame(new_rows)
        new_df.to_csv(self.csv_path, index=False) 
   
if __name__ == "__main__":
    folder_path = "data/txt"
    json_folder = "data/json/raw/txttorawjson"
    csv_output_path = "data/datasets/ner/ner_data.csv"
    converter = NERDataConverter(folder_path, json_folder, csv_output_path)
    converter.convert_to_json()
    converter.convert_to_csv()
    csv_path = "data/datasets/ner/ner_data.csv"
    analyzer = NERDataAnalyzer(csv_path)
    df = analyzer.read_csv()
# '''

