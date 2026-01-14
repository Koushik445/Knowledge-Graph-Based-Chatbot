import re

def parse_intent(user_query: str):
    query = user_query.lower()

    # Trend-based questions
    if any(word in query for word in ["ai", "digital twin", "scada", "iot", "robot", "battery"]):
        return {
            "intent": "BY_TREND",
            "entity": extract_keyword(query)
        }

    # Value-based questions
    if any(word in query for word in ["reliability", "esg", "cost", "efficiency", "compliance", "innovation"]):
        return {
            "intent": "BY_VALUE",
            "entity": extract_keyword(query)
        }

    # Problem-based questions
    if any(word in query for word in ["vegetation", "overload", "billing", "fault", "outage"]):
        return {
            "intent": "BY_PROBLEM",
            "entity": extract_keyword(query)
        }

    # Default
    return {
        "intent": "ALL",
        "entity": None
    }


def extract_keyword(query):
    keywords = [
        "ai", "digital twin", "scada", "iot", "robot",
        "battery", "reliability", "esg", "cost",
        "efficiency", "compliance", "vegetation",
        "billing", "fault", "outage"
    ]

    for k in keywords:
        if k in query:
            return k

    return None
