from neo4j import GraphDatabase
from app.core.config import settings
import logging

class Neo4jClient:
    def __init__(self):
        self._driver = None
        self.logger = logging.getLogger(__name__)

    def connect(self):
        """Connect to Neo4j Aura instance"""
        try:
            self._driver = GraphDatabase.driver(
                settings.NEO4J_URI,
                auth=(settings.NEO4J_USERNAME, settings.NEO4J_PASSWORD),
                database=settings.NEO4J_DATABASE
            )
            # Verify connection
            self._driver.verify_connectivity()
            self.logger.info(f"Successfully connected to Neo4j Aura instance {settings.NEO4J_INSTANCE_ID}")
            return self
        except Exception as e:
            self.logger.error(f"Failed to connect to Neo4j: {str(e)}")
            raise

    def close(self):
        """Close the driver connection"""
        if self._driver is not None:
            self._driver.close()
            self.logger.info("Neo4j connection closed")

    def execute_query(self, query, parameters=None):
        """Execute a Cypher query and return results"""
        if not self._driver:
            self.connect()
            
        with self._driver.session(database=settings.NEO4J_DATABASE) as session:
            try:
                result = session.run(query, parameters or {})
                return [record.data() for record in result]
            except Exception as e:
                self.logger.error(f"Query execution failed: {str(e)}")
                self.logger.debug(f"Query: {query}, Parameters: {parameters}")
                raise