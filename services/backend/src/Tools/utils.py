import cv2
from fastapi import UploadFile
import numpy as np

class Utils:
        
    @staticmethod
    async def convertImageToNumpyArray(fileData: UploadFile) -> np.ndarray:
        """
        Converts image data uploaded in binary format via POST request to a numpy ndarray.
        If the image contains an alpha channel, it is converted to an RGB image by removing the alpha channel.

        Args:
            fileData: Image data uploaded in binary format via POST request.

        Returns:
            A numpy ndarray representing the image. In case of RGB images, the third dimension has a value of 3.
        """
        contents = await fileData.read()
        np_array = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)

        if img.shape[-1] == 4:
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        return img