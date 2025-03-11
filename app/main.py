from fastapi import FastAPI
from app.api.routes import graph_routes
from app.core.config import settings

app = FastAPI(
    title="Knowledge Graph Agent",
    description="API for interacting with a Neo4j knowledge graph",
    version="1.0.0"
)

app.include_router(graph_routes.router)

@app.on_event("startup")
async def startup():
    # Initialize connections, etc.
    pass

@app.on_event("shutdown")
async def shutdown():
    # Close connections, etc.
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=settings.DEBUG)