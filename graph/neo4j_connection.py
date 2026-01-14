from neo4j import GraphDatabase

NEO4J_URI = "neo4j+s://77c62fba.databases.neo4j.io"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "GELAlan5RA6ewc43njkoZ_p-NQIKnLI0vgWXpOaJIKU"   

driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USER, NEO4J_PASSWORD)
)

def get_session():
    return driver.session()
