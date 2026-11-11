import pytest

from school_tools import grade


@pytest.mark.parametrize(
    ("mark", "expected_grade"),
    [
        (32, "F"),
        (33, "D"),
        (59, "D"),
        (60, "C"),
        (69, "C"),
        (70, "B"),
        (79, "B"),
        (80, "A"),
    ],
)
def test_grade_boundaries(mark, expected_grade):
    assert grade(mark) == expected_grade


@pytest.mark.parametrize("mark", [-1, 101])
def test_grade_rejects_marks_outside_range(mark):
    with pytest.raises(ValueError, match="between 0 and 100"):
        grade(mark)
