import pytest
from ClassAO import Class_AO

@pytest.mark.parametrize("x,y,z",[(1,2,3),(1,1,3)])
def test_add_method(x,y,z):
    ao = Class_AO()
    assert(ao.add(x,y) == z)