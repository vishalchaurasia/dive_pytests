import pytest

from source.student import calculate_grade


@pytest.mark.parametrize(
    "marks, expected_grade",
    [
        ([95, 90, 92], "A"),
        ([75, 80, 78], "B"),
        ([60, 65, 70], "C"),
        ([30, 40, 50], "F"),
        ([90, 90], "A"),
        ([75, 75], "B"),
        ([60, 60], "C"),
    ],
)
def test_calculate_grade(marks, expected_grade):
    assert calculate_grade(marks) == expected_grade


@pytest.mark.parametrize(
    "marks",
    [
        [],
        [95, -2, 80],
        [90, 110, 85],
    ],
)
def test_invalid_marks(marks):
    with pytest.raises(ValueError):
        calculate_grade(marks)