# Local application imports
from api_calls.api_call_decorators import get, post, put, delete, payload_type
from api_calls.api_call import APICall


@get
def get_custom_dimensions() -> APICall:
    """Returns an array of custom dimensions objects
    that each contain information about an individual custom dimension."""
    return APICall("/customdimensions")

@get
def get_custom_dimension_info(custom_dimension_id: int) -> APICall:
    """Returns a custom dimension object containing
    information about an individual custom dimension"""
    url_path = f"/customdimension/{custom_dimension_id}"
    return APICall(url_path)

@post
@payload_type(dict)
def create_custom_dimension() -> APICall:
    """Creates and returns a custom dimension object
    containing information about an individual custom dimension"""
    return APICall("/customdimension")

@put
@payload_type(dict)
def update_custom_dimension(custom_dimension_id: int) -> APICall:
    """Updates and returns a custom dimension object
    containing information about an individual custom dimension"""
    url_path = f"/customdimension/{custom_dimension_id}"
    return APICall(url_path)

@delete
def delete_custom_dimension(custom_dimension_id: int) -> APICall:
    """Deletes a custom dimension."""
    url_path = f"/customdimension/{custom_dimension_id}"
    return APICall(url_path)

@post
@payload_type(dict)
def create_populator() -> APICall:
    """Creates and returns a populator object containing
    information about an individual populator"""
    return APICall("/customdimension/{custom_dimension_id}/populator")

@put
@payload_type(dict)
def update_populator(custom_dimension_id: int, populator_id: int) -> APICall:
    """Updates and returns a populator object containing
    information about an individual populator"""
    url_path = f"/customdimension/{custom_dimension_id}/populator/{populator_id}"
    return APICall(url_path)

@delete
def delete_populator(custom_dimension_id: int, populator_id: int) -> APICall:
    """Deletes a populator"""
    url_path = f"/customdimension/{custom_dimension_id}/populator/{populator_id}"
    return APICall(url_path)
