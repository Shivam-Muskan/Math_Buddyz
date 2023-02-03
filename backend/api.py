from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.fibonacci.routes import router as FibonacciRouter
from backend.matrix.routes import router as MatrixRouter
from backend.ComputerNumberSystem.routes import router as NumberSystemRouter
from backend.linearAlgebra.routes import router as AlgebraRouter
from backend.NumericalMethods.routes import router as NumericalMethodsRouter


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
app.include_router(NumberSystemRouter)
app.include_router(AlgebraRouter)
app.include_router(NumericalMethodsRouter)
