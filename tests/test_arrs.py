import pytest

from utils import arrs


@pytest.fixture
def task_fix():
    return [1, 2, 3, 4]


def test_get(task_fix):
    assert arrs.get(task_fix, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get(task_fix, -1, "test") == "test"


def test_slice(task_fix):
    assert arrs.my_slice(task_fix, 1, 3) == [2, 3]
    assert arrs.my_slice(task_fix, 1) == [2, 3, 4]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(task_fix, -1) == [4]
    assert arrs.my_slice(task_fix, -5) == [1, 2, 3, 4]
