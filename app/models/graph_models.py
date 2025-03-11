from pydantic import BaseModel
from typing import Dict, Any, Optional

class NodeCreate(BaseModel):
    labels: list[str]
    properties: Dict[str, Any]

class RelationshipCreate(BaseModel):
    from_node_id: int
    to_node_id: int
    type: str
    properties: Optional[Dict[str, Any]] = None

class SearchQuery(BaseModel):
    label: str
    property_name: str
    property_value: Any