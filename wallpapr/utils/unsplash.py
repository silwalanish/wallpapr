from typing import Any, Dict


def get_orientation(config: Dict[str, Any]):
    orientation = config.get("orientation", "landscape")

    if isinstance(orientation, str):
        return orientation
    elif isinstance(orientation, list):
        return ",".join(orientation)
    else:
        return "landscape"


def get_collections(config: Dict[str, Any]):
    collections = config.get("collections", None)

    if not collections:
        return None

    if isinstance(collections, str):
        return collections
    elif isinstance(collections, list):
        collections_list = []
        for collection in collections:
            if isinstance(collection, str):
                collections_list.append(collection)
            elif isinstance(collection, dict):
                collections_list.append(collection.get("id", None))
        return ",".join(collections_list)

    return None


def get_query_params(config: Dict[str, Any]):
    return {
        "orientation": get_orientation(config),
        "collections": get_collections(config) or "",
    }
