import os

import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
import keras_ocr

class MachineLearning:

    @staticmethod
    async def imageToText(imageAsNumpyArray: np.ndarray) -> str:
        """
        Recognizes text from an image numpy ndarray using the Keras-OCR library.

        Args:
            imageAsNumpyArray: A numpy ndarray of the image.

        Returns:
            A string containing the extracted text.
        """
        pipeline = keras_ocr.pipeline.Pipeline()
        extractedText = ""

        try:
            prediction = pipeline.recognize([imageAsNumpyArray])[0]
            for text, box in prediction:
                extractedText += text + " "  
        except Exception as e:
            extractedText = "Something went wrong..."
            print("--------------------------------------------------------- ERROR")
            print(e)

        return extractedText

