import pandas as pd
from neo4j_connection import get_session

CSV_PATH = "data/ideas_dataset.csv"

def ingest():
    df = pd.read_csv(CSV_PATH)

    with get_session() as session:
        for _, row in df.iterrows():
            session.run(
                """
                MERGE (i:Idea {id: $id})
                SET i.title = $title,
                    i.description = $description,
                    i.complexity = $complexity,
                    i.time_to_implement = $time,
                    i.potential_roi = $roi,
                    i.remarks = $remarks

                MERGE (p:Problem {name: $problem})
                MERGE (i)-[:HAS_PROBLEM]->(p)

                MERGE (bv:BusinessValue {
                    value: $business_value,
                    type: $value_type
                })
                MERGE (i)-[:DELIVERS_VALUE]->(bv)

                MERGE (u:UseCase {description: $use_case})
                MERGE (i)-[:HAS_USE_CASE]->(u)
                """,
                {
                    "id": row["Idea_ID"],
                    "title": row["Idea_Title"],
                    "description": row["Detailed_Idea_Description"],
                    "complexity": row["Complexity_Level"],
                    "time": row["Time_to_Implement"],
                    "roi": row["Potential_RoI_Level"],
                    "remarks": row["Remarks"],
                    "problem": row["Problem_Pattern_From_Issues"],
                    "business_value": row["Expected_Business_Value"],
                    "value_type": row["Type_of_Value"],
                    "use_case": row["Example_Use_Case"]
                }
            )

            # ---- Trends ----
            for trend in str(row["Trend_Insight_Leveraged"]).split(";"):
                session.run(
                    """
                    MATCH (i:Idea {id: $id})
                    MERGE (t:TechnologyTrend {name: $trend})
                    MERGE (i)-[:LEVERAGES_TREND]->(t)
                    """,
                    {"id": row["Idea_ID"], "trend": trend.strip()}
                )

            # ---- Stakeholders ----
            for s in str(row["Stakeholders_Involved"]).split(","):
                session.run(
                    """
                    MATCH (i:Idea {id: $id})
                    MERGE (st:Stakeholder {role: $role})
                    MERGE (i)-[:INVOLVES]->(st)
                    """,
                    {"id": row["Idea_ID"], "role": s.strip()}
                )

            # ---- Dependencies ----
            for d in str(row["Dependencies"]).split(","):
                session.run(
                    """
                    MATCH (i:Idea {id: $id})
                    MERGE (dep:Dependency {name: $dep})
                    MERGE (i)-[:DEPENDS_ON]->(dep)
                    """,
                    {"id": row["Idea_ID"], "dep": d.strip()}
                )

            # ---- Risks ----
            session.run(
                """
                MATCH (i:Idea {id: $id})
                MERGE (r:Risk {type: $risk})
                MERGE (i)-[:HAS_RISK]->(r)
                """,
                {"id": row["Idea_ID"], "risk": row["Risks_or_Constraints"]}
            )

    print("✅ Graph ingestion completed successfully")

if __name__ == "__main__":
    ingest()
