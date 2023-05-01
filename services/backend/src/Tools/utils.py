import cv2
import numpy as np

class Utils:
        
    @staticmethod
    async def convertImageToNumpyArray(fileData):
        contents = await fileData.read()
        np_array = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)

        return img