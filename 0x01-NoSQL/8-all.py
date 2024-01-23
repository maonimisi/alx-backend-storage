#!/usr/bin/env python3
"""
Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """Function return a liss of all document in a collection

       Args: mongo_collection as the pymongo collection object
    """
    return mongo_collection.find()
