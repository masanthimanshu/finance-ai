from fastapi import FastAPI

app = FastAPI(title="Fiance App")

@app.get("/health")
def health():
    return {"message": "Server is running"}
