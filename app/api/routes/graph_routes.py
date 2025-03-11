from fastapi import APIRouter, Depends, HTTPException
from app.services.graph_service import GraphService
from app.models.graph_models import NodeCreate, RelationshipCreate, SearchQuery

router = APIRouter(prefix="/api/graph", tags=["knowledge graph"])

@router.get("/node/{node_id}")
async def get_node(node_id: int):
    service = GraphService()
    node = service.get_node_by_id(node_id)
    if not node:
        raise HTTPException(status_code=404, detail="Node not found")
    return node

@router.post("/relationship")
async def create_relationship(relationship: RelationshipCreate):
    service = GraphService()
    result = service.create_relationship(
        relationship.from_node_id,
        relationship.to_node_id,
        relationship.type,
        relationship.properties
    )
    return {"message": "Relationship created", "data": result}

@router.post("/search")
async def search_nodes(search_query: SearchQuery):
    service = GraphService()
    results = service.search_by_property(
        search_query.label,
        search_query.property_name,
        search_query.property_value
    )
    return {"results": results}