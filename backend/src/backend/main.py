from fastapi import FastAPI


app = FastAPI(
    title="Real Estate",
    description="Продажа недвижимости",
    version="0.1.0",
    # docs_url="/docs",
    # redoc_url="/redoc"
)

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.get("/health")
async def health_check():
    return {"status": "ok", "version": "0.1.0"}


