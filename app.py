from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def greet_json():
    return {"Hello": "World!"}

@app.get("/mlendp")
def ml_json():
    return {"Hello": "This is a ml endpoint"}

# Define a route to serve images
@app.get("/images/{image_name}")
async def get_image(image_name: str):
    # Assuming images are stored in a directory named 'images'
    image_path = f"images/{image_name}"
    try:
        # Return the image using FileResponse
        return FileResponse(image_path)
    except FileNotFoundError:
        # If the file is not found, return a 404 error
        raise HTTPException(status_code=404, detail="Image not found")

@app.get("/audio/{audio_name}")
async def get_image(audio_name: str):
    # Assuming images are stored in a directory named 'images'
    audio_path = f"audio/{audio_name}"
    try:
        # Return the image using FileResponse
        return FileResponse(audio_path)
    except FileNotFoundError:
        # If the file is not found, return a 404 error
        raise HTTPException(status_code=404, detail="Image not found")
