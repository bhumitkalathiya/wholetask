from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend (React) to access backend API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Change if React runs on a different port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
