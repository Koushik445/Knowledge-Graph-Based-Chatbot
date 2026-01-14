// ===============================
// NODE CONSTRAINTS
// ===============================

CREATE CONSTRAINT idea_id IF NOT EXISTS
FOR (i:Idea) REQUIRE i.id IS UNIQUE;

CREATE CONSTRAINT problem_name IF NOT EXISTS
FOR (p:Problem) REQUIRE p.name IS UNIQUE;

CREATE CONSTRAINT trend_name IF NOT EXISTS
FOR (t:TechnologyTrend) REQUIRE t.name IS UNIQUE;

CREATE CONSTRAINT stakeholder_role IF NOT EXISTS
FOR (s:Stakeholder) REQUIRE s.role IS UNIQUE;

CREATE CONSTRAINT dependency_name IF NOT EXISTS
FOR (d:Dependency) REQUIRE d.name IS UNIQUE;

CREATE CONSTRAINT risk_type IF NOT EXISTS
FOR (r:Risk) REQUIRE r.type IS UNIQUE;
