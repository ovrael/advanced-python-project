from src.Tools.machineLearning import MachineLearning as ML
from src.Tools.utils import Utils
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:7000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    logLevels = ["INFO","WARNING","ERROR","NONE" ]
    print("\n\n ---------------=================== Backend startup ===================---------------")
    print("-- Name: AI Tools")
    print("-- Authors: Jacek Jendrzejewski, Maciej Baranowski")
    print("-- Version: 1.0.0")
    print("-- Tensorflow log level: " + logLevels[int(os.environ['TF_CPP_MIN_LOG_LEVEL'])])

@app.get("/")
def home():
    return "Hello, World!"


@app.get("/about")
def about():
    return "This is about us page!"


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {
            "result": False,
            "message": "Couldn't process received file.",
            }
    
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return {
            "result": False,
            "message": "File has incorrect extension. Ensure image is jpg/jpeg/png.",
            }

    numpyImage = await Utils.convertImageToNumpyArray(file)
    extractedText = await ML.imageToText(numpyImage)

    return {
        "result": True,
        "message": "File received correctly. Searching for text.",
        "filename": file.filename,
        "extractedText": extractedText
        }