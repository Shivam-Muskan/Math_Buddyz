from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .fibonacci.routes import router as FibonacciRouter
from .matrix.routes import router as MatrixRouter

app = FastAPI()

app_name = "Math Buddyz"
app_version = 0.3

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=600
)


@app.get("/")
async def version():
    return {
        "name": app_name,
        "version": app_version
    }


@app.get("/health")
async def health():
    return {
        "health": "Ok"
    }


app.include_router(FibonacciRouter)
app.include_router(MatrixRouter)

