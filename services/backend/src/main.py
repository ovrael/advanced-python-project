from src.Tools.machineLearning import MachineLearning as ML
from src.Tools.utils import Utils
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os
from typing import List


app = FastAPI()

# CORS middleware to allow cross-origin resource sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:7000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Event handler for startup of the application
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

# API endpoint to upload a file and extract text from it
@app.post("/extractTextFromImage/")
async def extract_text_from_image(file: UploadFile | None = None):
    """
    Converts image data uploaded in binary format via POST request to a numpy ndarray.
    Then recognizes text from an image numpy ndarray using the Keras-OCR library.

    Args:
        file: Image data uploaded in binary format via POST request.

    Returns:
        A JSON data containing the result status of operation, additional message and extracted text.
    """

    # Check if a file was sent
    if not file:
        return {
            "result": False,
            "message": "Couldn't process received file.",
            "extractedText": "Couldn't process received file."
            }
    
    # Check if the file extension is valid
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return {
            "result": False,
            "message": "File has incorrect extension. Ensure image is jpg/jpeg/png.",
            "extractedText": "File has incorrect extension. Ensure image is jpg/jpeg/png."
            }

    # Convert the image to a numpy array and extract text from it
    numpyImage = await Utils.convertImageToNumpyArray(file)
    extractedText = await ML.imageToText(numpyImage)

    return {
        "result": True,
        "message": "File received correctly. Searching for text.",
        "extractedText": extractedText
        }


@app.post("/detect_objects")
async def detect_objects(file: UploadFile = UploadFile(...)) -> List[dict]:
    # Save image to a temporary file
    with open(file.filename, "wb") as buffer:
        buffer.write(await file.read())
    image_path = file.filename

    # Call analyzeImage method to detect objects in the image
    detected_objects = ML.analyzeImage(image_path)

    print(detected_objects)

    # Return detected objects and their details
    return detected_objects