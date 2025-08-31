from os import getenv
from uvicorn import run
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    run("api:app", port=int(getenv("PORT")), reload=True)
