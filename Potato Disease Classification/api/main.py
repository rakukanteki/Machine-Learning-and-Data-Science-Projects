from fastapi import FastAPI, File, UploadFile
import numpy as np
import uvicorn
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()
MODEL = tf.keras.models.load_model("../saved_models/potatoes.keras")
CLASS_NAMES = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data: bytes) -> np.ndarray:
    try:
        image = np.array(Image.open(BytesIO(data)))
        return image
    
    except Exception as e:
        raise ValueError(f"Error Processing Image: {e}")


@app.post("/process_prediction")
async def process_prediction(
    file: UploadFile = File(...) # Dataset is images. So send files.
    ):
    try:
        # await and async does the work of multiple requests.
        image = read_file_as_image(await file.read())
        img_batch = np.expand_dims(image, 0)
    
        predictions = MODEL.predict(img_batch)

        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = round(100 * (np.max(predictions[0])), 2)

        return {
            'class': predicted_class,
            'confidence': float(confidence)
        }
    except Exception as e:
        return {"error": f"Prediction failed: {e}"}


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)