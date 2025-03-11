from app.db.neo4j_client import Neo4jClient

class GraphService:
    def __init__(self):
        self.db_client = Neo4jClient().connect()

    def get_node_by_id(self, node_id):
        """Retrieve a node by its ID"""
        query = "MATCH (n) WHERE id(n) = $node_id RETURN n"
        results = self.db_client.execute_query(query, {"node_id": node_id})
        return results[0] if results else None

    def create_relationship(self, from_node_id, to_node_id, relationship_type, properties=None):
        """Create a relationship between two nodes"""
        query = """
        MATCH (a), (b)
        WHERE id(a) = $from_id AND id(b) = $to_id
        CREATE (a)-[r:`$rel_type` $props]->(b)
        RETURN r
        """
        params = {
            "from_id": from_node_id,
            "to_id": to_node_id,
            "rel_type": relationship_type,
            "props": properties or {}
        }
        return self.db_client.execute_query(query, params)

    # Additional methods for your knowledge graph operations
    def search_by_property(self, label, property_name, property_value):
        """Search for nodes with a specific property value"""
        query = f"MATCH (n:`{label}`) WHERE n.`{property_name}` = $value RETURN n"
        return self.db_client.execute_query(query, {"value": property_value})