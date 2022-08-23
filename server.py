from fastapi import FastAPI
import uvicorn
from fastapi import UploadFile, File
from PIL import Image
import numpy as np
import io
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def Hello_World():
    return "Hello World"


@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    pil_image = Image.open(io.BytesIO(contents))
    pil_image = pil_image.resize((200, 200))
    print("resize done")
    i = np.asarray(pil_image)
    input_arr = np.array([i])
    print("array made")
    return {"prediction": "MONKEY WITH A BAR" }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
