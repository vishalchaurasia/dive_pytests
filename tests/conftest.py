import pytest

from source.student_db import StudentDB


@pytest.fixture(scope="module")
def student_db():

    print("\nCreating StudentDB")

    db = StudentDB()

    yield db

    print("\nCleaning StudentDB")