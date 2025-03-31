from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Kiubi API 🚀"}

@app.post("/create-flight/")
def create_flight(flight: dict):
    return {"message": "Flight added successfully", "flight": flight}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
