from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def greet():
    return {"message": "Привет, user!"}


if __name__ == "__main__":
    uvicorn.run("main_fastapi_1:app")




