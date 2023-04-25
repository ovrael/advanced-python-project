from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:7000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "Hello, World!"


@app.get("/about")
def about():
    return "This is about us page!"


@app.get("/test")
def test():
    return "Testing! Hahahaha"


@app.get("/test2")
def test2():
    return "Testing again!"
