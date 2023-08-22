import uvicorn
from fastapi import FastAPI, UploadFile, File
# from src.engine import QuestionParser
from fastapi.exceptions import HTTPException
# import json
# import nltk
# nltk.download('stopwords')
# nltk.download('wordnet')

app = FastAPI()

@app.post("/parse_docx")
async def parse_docx(file: UploadFile = File(...)):
    if not file.filename.lower().endswith('.docx'):
        raise HTTPException(400, detail="Invalid Document Type. Only .docx files are allowed.")
    else:
        docx_filename = file.filename
        file_path = f'data/docs/docx/done/{docx_filename}'
        with open(file_path, 'wb') as f:
            f.write(await file.read())

        # parser = QuestionParser(file_path, 'data/datasets/text_dropdown_range.xlsx', 'data/datasets/Single_Multiple_Range.csv', 'data/datasets/single_multiple_grid.csv')

        # parser.parse_docx()  

        # try:
        #     parser.train_text_classifier()
        # except:
        #     pass
        # try:
        #     parser.train_mention_classifier()
        # except:
        #     pass
        # try:
        #     parser.grid_classifier()
        # except:
        #     pass
        # parser.create_text_json()
        # parser.create_mention_json()
        # parser.create_grid_json()
        # parser.merge_json()

        # json_filename = docx_filename.split('.docx')[0]
        # with open(f'data/docs/json/final/{json_filename}.json', 'r') as f:
        #     result = json.load(f)

        # return result

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
