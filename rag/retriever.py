from graph.neo4j_connection import get_session
import rag.query_templates as queries


class GraphRetriever:

    def __init__(self):
        self.session = get_session()

    def get_all_ideas(self):
        result = self.session.run(queries.GET_ALL_IDEAS)
        return [r.data() for r in result]

    def get_ideas_by_trend(self, trend):
        result = self.session.run(
            queries.GET_IDEAS_BY_TREND,
            {"trend": trend}
        )
        return [r.data() for r in result]

    def get_ideas_by_problem(self, problem):
        result = self.session.run(
            queries.GET_IDEAS_BY_PROBLEM,
            {"problem": problem}
        )
        return [r.data() for r in result]

    def get_ideas_by_value_type(self, value_type):
        result = self.session.run(
            queries.GET_IDEAS_BY_VALUE_TYPE,
            {"value_type": value_type}
        )
        return [r.data() for r in result]

    def get_idea_details(self, idea_id):
        result = self.session.run(
            queries.GET_IDEA_DETAILS,
            {"idea_id": idea_id}
        )
        record = result.single()
        return record.data() if record else None
