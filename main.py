from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def test_api():
    return {"status" : "working"}