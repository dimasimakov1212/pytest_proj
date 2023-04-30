import pytest

from utils import arrs


@pytest.fixture
def task_fix():
    return [1, 2, 3, 4]


def test_get(task_fix):
    assert arrs.get(task_fix, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get(task_fix, -1, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.my_slice([1, 2, 3], -4) == [1, 2, 3]
