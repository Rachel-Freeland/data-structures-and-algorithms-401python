from code_challenges.insertion_sort import insertion_sort


def test_input_array():
    arr = [8, 4, 23, 42, 16, 15]
    actual = insertion_sort(arr)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


