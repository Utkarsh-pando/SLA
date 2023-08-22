import os
import docx
import doc2txt

class Doc2TxtTextExtractor:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def extract_text(self, file_path):
        full_path = os.path.join(self.folder_path, file_path)
        if file_path.endswith(".docx"):
            text = doc2txt.process(full_path)
            return text.split("\n")
        return []

    def extract_all_text(self):
        all_text = []
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".docx"):
                text = self.extract_text(filename)
                all_text.extend(text)
        return all_text
    
folder_path = "path/to/your/folder"
docx_extractor = DocxTextExtractor(folder_path)
doc2txt_extractor = Doc2TxtTextExtractor(folder_path)

docx_text = docx_extractor.extract_all_text()
doc2txt_text = doc2txt_extractor.extract_all_text()

print("Text extracted using DocxTextExtractor:")
for item in docx_text:
    print(item)

print("\nText extracted using Doc2TxtTextExtractor:")
for item in doc2txt_text:
    print(item)