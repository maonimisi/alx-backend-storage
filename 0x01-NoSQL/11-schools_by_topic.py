#!/usr/bin/env python3
"""Function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """
    Function that finds schools by topic
    Args:
        mongo_collection: pymongo collection object
        topic(str): topic searched
    Returns: list of schools having the specified topic
    """
    return mongo_collection.find({"topics": {"$in": [topic]}})

