import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
import keras_ocr

class MachineLearning:

    @staticmethod
    async def imageToText(imageAsNumpyArray):

        pipeline = keras_ocr.pipeline.Pipeline()
        prediction = pipeline.recognize([imageAsNumpyArray])[0]

        extractedText = ""
        for text, box in prediction:
            extractedText += text + " "  

        return extractedText

