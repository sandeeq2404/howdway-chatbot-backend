from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.chat import router

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def read_root():
    return {"status": "Backend is running"}
