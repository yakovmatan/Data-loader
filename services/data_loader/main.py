from fastapi import FastAPI
from services.data_loader.data_loader import DataLoader

app = FastAPI()
loader = DataLoader()

@app.get("/data")
def get_data():
    return loader.get_data()