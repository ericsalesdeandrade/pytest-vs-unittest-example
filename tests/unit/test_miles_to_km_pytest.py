import pytest
import logging
from miles_to_km.core import miles_to_km, km_to_miles

# Get logger
logger = logging.getLogger('__miles_to_km__')
logger.setLevel(logging.INFO)


def test_miles_to_km():
    assert miles_to_km(1) == 1.61

def test_km_to_miles():
    assert km_to_miles(1) == 0.62

def test_miles_to_km_dict_type():
    with pytest.raises(TypeError):
        miles_to_km({'a': 1, 'b': 2})

def test_miles_to_km_list_type():
    with pytest.raises(TypeError):
        mile_to_km([1,2,3])


