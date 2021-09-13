import pytest
from ClassAO import Class_AO

@pytest.mark.parametrize("x,y,z",[(1,2,3),(1,1,2)])
def test_add_method(x,y,z):
    ao = Class_AO()
    assert(ao.add(x,y) == z)

@pytest.mark.parametrize("x,y,z",[(1,2,1),(1,1,0)])
def test_sub_method(x,y,z):
    ao = Class_AO()
    assert(ao.sub(x,y) == z)
