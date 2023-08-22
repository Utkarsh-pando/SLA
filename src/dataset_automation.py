import os
import json
import csv

class NERDataConverter:
    def __init__(self, folder_path, json_folder, csv_output_path, ner_data_raw="NER DATA RAW"):
        self.folder_path = folder_path
        self.json_folder = json_folder
        self.csv_output_path = csv_output_path
        self.ner_data_raw = ner_data_raw

    def convert_to_json(self):
        txt_files = [file for file in os.listdir(self.folder_path) if file.endswith(".txt")]

        for txt_file in txt_files:
            file_path = os.path.join(self.folder_path, txt_file)
            with open(file_path, "r") as file:
                file_contents = file.read()
                lines = file_contents.split("\n")

            json_filename = txt_file.replace(".txt", ".json")
            json_path = os.path.join(self.json_folder, json_filename)

            lines_dict = {str(line_number + 1): line.strip() for line_number, line in enumerate(lines)}

            with open(json_path, "w") as json_file:
                json.dump(lines_dict, json_file, indent=4)

    def convert_to_csv(self):
        csv_data = []

        json_files = [file for file in os.listdir(self.json_folder) if file.endswith(".json")]

        for json_file in json_files:
            json_path = os.path.join(self.json_folder, json_file)
            with open(json_path, "r") as file:
                json_data = json.load(file)
                for key, value in json_data.items():
                    csv_data.append([key, value, json_file])

        with open(self.csv_output_path, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Key", "Value", "Filename"])
            csv_writer.writerows(csv_data)

# Example usage
if __name__ == "__main__":
    folder_path = "data/txt"
    json_folder = "data/json/raw/txttorawjson"
    csv_output_path = "data/datasets/ner/ner_data.csv"
    converter = NERDataConverter(folder_path, json_folder, csv_output_path)
    converter.convert_to_json()
    converter.convert_to_csv()
