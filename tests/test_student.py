import pytest

from source.student import calculate_grade


def test_grade_a():
    assert calculate_grade([95, 90, 92]) == "A"


def test_grade_b():
    assert calculate_grade([75, 80, 78]) == "B"


def test_grade_c():
    assert calculate_grade([60, 65, 70]) == "C"


def test_grade_f():
    assert calculate_grade([30, 40, 50]) == "F"


def test_empty_marks():
    with pytest.raises(ValueError):
        calculate_grade([])


def test_negative_marks():
    with pytest.raises(ValueError):
        calculate_grade([95, -2, 80])


def test_marks_above_100():
    with pytest.raises(ValueError):
        calculate_grade([90, 110, 85])


def test_boundary_90():
    assert calculate_grade([90, 90]) == "A"


def test_boundary_75():
    assert calculate_grade([75, 75]) == "B"


def test_boundary_60():
    assert calculate_grade([60, 60]) == "C"