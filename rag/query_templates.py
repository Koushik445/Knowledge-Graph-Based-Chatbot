# Central place for Cypher queries

GET_ALL_IDEAS = """
MATCH (i:Idea)
RETURN i.id AS id, i.title AS title
"""

GET_IDEAS_BY_TREND = """
MATCH (i:Idea)-[:LEVERAGES_TREND]->(t:TechnologyTrend)
WHERE toLower(t.name) CONTAINS toLower($trend)
RETURN i.id AS id, i.title AS title, t.name AS trend
"""

GET_IDEAS_BY_PROBLEM = """
MATCH (i:Idea)-[:HAS_PROBLEM]->(p:Problem)
WHERE toLower(p.name) CONTAINS toLower($problem)
RETURN i.id AS id, i.title AS title, p.name AS problem
"""

GET_IDEAS_BY_VALUE_TYPE = """
MATCH (i:Idea)-[:DELIVERS_VALUE]->(bv:BusinessValue)
WHERE toLower(bv.type) CONTAINS toLower($value_type)
RETURN i.id AS id, i.title AS title, bv.type AS value_type
"""

GET_IDEA_DETAILS = """
MATCH (i:Idea {id: $idea_id})
OPTIONAL MATCH (i)-[:HAS_PROBLEM]->(p)
OPTIONAL MATCH (i)-[:LEVERAGES_TREND]->(t)
OPTIONAL MATCH (i)-[:DELIVERS_VALUE]->(bv)
OPTIONAL MATCH (i)-[:INVOLVES]->(s)
OPTIONAL MATCH (i)-[:DEPENDS_ON]->(d)
OPTIONAL MATCH (i)-[:HAS_RISK]->(r)
RETURN
i.id AS id,
i.title AS title,
i.description AS description,
collect(DISTINCT p.name) AS problems,
collect(DISTINCT t.name) AS trends,
collect(DISTINCT bv.type) AS value_types,
collect(DISTINCT s.role) AS stakeholders,
collect(DISTINCT d.name) AS dependencies,
collect(DISTINCT r.type) AS risks
"""
