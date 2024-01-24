#!/usr/bin/env python3
"""Function that changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """
    Function changes all topic of a school document based on the name
    Args:
        mongo_collection: pymongo collection object
        name(str): School name to update
        topics(list(str)): List of topics
    """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})

