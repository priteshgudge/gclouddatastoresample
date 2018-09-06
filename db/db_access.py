from google.cloud import datastore
import os

PROJECT_ID = os.getenv("GC_PROJECT_ID","pocproject-215503")

def create_client(project_id=PROJECT_ID):
    return datastore.Client(project_id)

def write_to_db(client,object_type:str,object_dict:dict,attributes_to_index:set):

    if object_dict is None:
        return ValueError("Object Dictionary is invalid")
    if object_dict is None:
        return ValueError("Object Type String is invalid")

    exclude_from_indexes = object_dict.keys().difference(attributes_to_index)

    key = client.key(object_type)

    entity = datastore.Entity(
        key, exclude_from_indexes=exclude_from_indexes)

    entity.update(object_dict)

    client.put(entity)

    key = entity.key
    object_dict.update({'id': key})

    return object_dict

def read_from_db(client,object_type,object_id):
    key = client.key(object_type, object_id)
    object = client.get(key)

    if not object:
        return None

    #object.update({"id": object_id})

    return object


def upsert_to_db(client, object_type:str, object_id:str, object_dict: dict, attributes_to_index: set):
    if object_dict is None:
        return ValueError("Object Dictionary is invalid")
    if object_type is None:
        return ValueError("Object Type String is invalid")

    if object_id is None:
        return ValueError("Object ID String is invalid")

    exclude_from_indexes = list(set(object_dict.keys()).difference(attributes_to_index))

    key = client.key(object_type, object_id)

    entity = datastore.Entity(key=key,exclude_from_indexes=exclude_from_indexes)
    entity.update(object_dict)

    client.put(entity)

    return object_dict
