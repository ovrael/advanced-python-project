import os

import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
import keras_ocr
import keras
import cv2


from keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import keras.utils as image
import keras.api._v2.keras as keras



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


    def analyzeImage(image_path: str) -> str:
        # Load the image and resize it to the input shape of MobileNetV2
        img = image.load_img(image_path, target_size=(224, 224))

        # Convert the image to a numpy array
        img_array = image.img_to_array(img)

        # Expand the dimensions of the image to match the input shape of MobileNetV2
        img_array = np.expand_dims(img_array, axis=0)

        # Preprocess the image using the preprocess_input function of MobileNetV2
        img_array = preprocess_input(img_array)

        # Load the MobileNetV2 model
        model = keras.applications.mobilenet_v2.MobileNetV2()

        # Make predictions on the image using the MobileNetV2 model
        predictions = model.predict(img_array)

        # Decode the predictions using the decode_predictions function of MobileNetV2
        decoded_predictions = decode_predictions(predictions, top=3)[0]

        # Create a list of detected objects and their scores
        detected_objects = [{'class': class_name, 'score': float(score)} for (_, class_name, score) in decoded_predictions]

        # Visualize the detected objects and their scores on the image
        img = cv2.imread(image_path)
        for obj in detected_objects:
            cv2.putText(img, '{}: {:.2f}'.format(obj['class'], obj['score']), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imwrite('output.jpg', img)

        # Return the detected objects and their scores
        return detected_objects

