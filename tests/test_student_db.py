def test_add_student(student_db):

    student_db.add_student("Harshada")

    assert student_db.total_students() == 1
    assert student_db.get_students() == ["Harshada"]


def test_remove_student(student_db):

    student_db.add_student("Vishal")
    student_db.remove_student("Vishal")

    assert student_db.total_students() == 1


def test_multiple_students(student_db):

    student_db.add_student("A")
    student_db.add_student("B")
    student_db.add_student("C")

    assert student_db.total_students() == 4