from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def message():
    print("---Log message --> Message function is executed---")
    return "Success 200"
