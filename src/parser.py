'''
# docx_extractor = DocxTextExtractor(folder_path)
# import docx
# docx_text = docx_extractor.extract_all_text()

# print("Text extracted using DocxTextExtractor:")
# for item in docx_text:
#     print(item)


'''
import os
import doc2text
from docx import Document

class DocxTextExtractor:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def extract_text(self):
        text_data = []
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".docx"):
                file_path = os.path.join(self.folder_path, filename)
                docx_text = self._extract_docx_text(file_path)
                text_data.append(docx_text)
        return text_data

    def _extract_docx_text(self, file_path):
        doc = Document(file_path)
        doc_text = []
        for element in doc.element.body:
            if element.tag.endswith(("p", "tbl")):
                element_text = doc2text.extract(file_path, page_numbers=[element.get_or_add_tc().get_or_add_tr()])
                doc_text.append(element_text.strip())
        return "\n".join(doc_text)


if __name__ == "__main__":
    folder_path = "path/to/your/docx/files/folder"
    text_extractor = DocxTextExtractor(folder_path)
    extracted_text = text_extractor.extract_text()
    for i, text in enumerate(extracted_text, start=1):
        print(f"Document {i}:\n{text}\n{'='*40}\n")
