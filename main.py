import uvicorn
from backend.api import app

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
    # uvicorn.run('backend.api:app', host="127.0.0.1", port=8080, reload=True)
