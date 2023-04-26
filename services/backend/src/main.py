from ast import List
import os
from fastapi import FastAPI, File, Response, UploadFile, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:7000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "Hello, World!"


@app.get("/about")
def about():
    return "This is about us page!"

# @app.post("/uploadfiles/")
# async def create_upload_files(files: List[UploadFile] = File(...)):
#     result=""
#     for file in files:
#         print(file)
#         # fpath = os.path.join(
#         #     STORAGE_PATH, f'{file.filename}'
#         # )
#         # async with aiofiles.open(fpath, 'wb') as f:
#         #     content = await file.read()
#         #     await f.write(content)

        

#     return {"message": "success"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {
            "result": False,
            "message": "No upload file sent.",
            }
    
    return {
        "result": True,
        "message": "File received correctly.",
        "filename": file.filename,
        }