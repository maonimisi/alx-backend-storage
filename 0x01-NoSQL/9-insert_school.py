#!/usr/bin/env python3
"""Function that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """function add a new document to an existing colletion
    Args:
         Pymongo collection object: mongo_collection
         kwargs: dictionary of a new document to insert

    Returns:
        id of the new document added
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
