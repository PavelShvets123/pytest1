from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1], 0, "test") == 1
    assert arrs.get([1, 2, 3, 4, 5], -1, "test") == "test"
    assert arrs.get([1, 2, 3, 4, 5], 0, ) == 1
    assert arrs.get(['cat', 'dog', 'mouse'], 0, "test") == 'cat'


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4, -1) == [5, 6, 7, 8, 9]
    assert arrs.my_slice([1, 2, 3, 4, 5, 6, 7], -1, 3) == []
    assert arrs.my_slice([1, 2, 3, 4, 5, 6, 7], 0, 1) == [1]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], -10) == [1, 2, 3, 4, 5]

