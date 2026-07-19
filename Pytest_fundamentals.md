# dive_pytests

A beginner-friendly pytest revision guide and learning notes.

This repository is meant to be a simple handbook for learning pytest step by step. It is useful for Python beginners, developers revising for interviews, and anyone who wants a quick reminder of the most common pytest ideas.

---

## 1. Assertions

Assertions are the foundation of every test. They check whether the actual result matches the expected result.

### Why they are used
- To verify output
- To confirm behavior
- To make tests fail when something is wrong

### Examples

```python
assert a == b
assert a != b
assert value is None
assert value is not None
```

### Key learning
- A test passes if the assertion is true.
- A test fails if the assertion is false.
- Assertions are the simplest way to test logic.

---

## 2. pytest.raises

Use pytest.raises when you want to verify that a function raises an expected exception.

### Example

```python
import pytest


def calculate_grade(marks):
    if not marks:
        raise ValueError("Marks list cannot be empty")
    return "A"


with pytest.raises(ValueError):
    calculate_grade([])
```

### Key learning
- This is used for negative test cases.
- It is very useful for validation logic.
- It helps confirm that the code handles errors correctly.

---

## 3. pytest.mark.parametrize

This decorator lets you run the same test with different inputs without writing many duplicate test functions.

### Example

```python
import pytest


def calculate_grade(marks):
    if sum(marks) >= 90:
        return "A"
    if sum(marks) >= 75:
        return "B"
    return "C"


@pytest.mark.parametrize(
    "marks, grade",
    [
        ([95, 90], "A"),
        ([80, 75], "B"),
        ([65, 60], "C"),
    ],
)
def test_calculate_grade(marks, grade):
    assert calculate_grade(marks) == grade
```

### Key learning
- It removes duplicate test functions.
- It makes adding more test cases very easy.
- It is great for checking many input combinations.

---

## 4. Fixtures

Fixtures are reusable pieces of test setup. They help create objects or data that many tests need.

### Example

```python
import pytest


@pytest.fixture
def sample_data():
    return {"id": 1, "name": "Alice"}


def test_sample_data(sample_data):
    assert sample_data["id"] == 1
```

### Key learning
- Fixtures reduce repetitive setup code.
- They are automatically injected into test functions when requested.
- They make tests cleaner and easier to maintain.

---

## 5. Fixture Scope

Fixture scope controls how long a fixture lives.

### Scope types

- Function scope: a new fixture is created for every test.
- Module scope: one fixture is shared within a test file.
- Session scope: one fixture is shared across the whole pytest run.

### Comparison table

| Scope | Lifetime | Best for |
| --- | --- | --- |
| Function | New for each test | Isolated data and fresh setup |
| Module | Shared within one file | Data reused by many tests in the same file |
| Session | Shared for the whole run | Expensive setup that should be reused |

### Key learning
- Use the smallest scope that fits your need.
- Function scope is the safest default.
- Wider scopes can improve speed, but may cause shared state issues.

---

## 6. conftest.py

conftest.py is a special file where shared fixtures can be stored.

### Why it is useful
- You can place reusable fixtures in one place.
- Pytest automatically discovers them.
- You do not need to manually import them into every test file.

### Example structure

```python
# conftest.py
import pytest


@pytest.fixture
def sample_data():
    return {"id": 1}
```

### Key learning
- conftest.py helps reduce duplication.
- It makes fixtures available to multiple test files.
- It is a clean way to share setup logic.

---

## 7. Markers

Markers add labels or metadata to tests. They help you organize and run tests in groups.

### Built-in markers
- parametrize
- skip
- skipif
- xfail
- usefixtures

### Custom markers
- smoke
- slow
- integration
- regression
- api
- db
- kafka
- spark

### Example

```python
import pytest


@pytest.mark.smoke
def test_login():
    assert True
```

### How to run marker-based tests

```bash
pytest -m smoke
pytest -m slow
pytest -m "not slow"
```

### Marker summary table

| Marker | Purpose |
| --- | --- |
| smoke | Quick important tests |
| slow | Tests that take more time |
| integration | Tests with multiple components |
| regression | Tests for known bugs |
| api | API-related tests |
| db | Database-related tests |
| kafka | Kafka-related tests |
| spark | Spark-related tests |

### Key learning
- Markers help you group tests by purpose.
- They make it easier to run only the tests you need.
- They are useful in large projects.

---

## 8. MagicMock

MagicMock is used to replace external dependencies with fake objects.

### Why mocking is useful
We often mock things like:
- databases
- APIs
- email services
- Kafka
- S3 storage

This is useful because we do not want tests to depend on real external systems.

### Example concept

```python
from unittest.mock import MagicMock

mock_email = MagicMock()

order = OrderService(mock_email)
order.place_order()

mock_email.send_email.assert_called_once_with(...)
```

### Key learning
- No real external system is called.
- You can verify whether methods were called and what arguments were used.
- MagicMock is helpful when you want full control over dependencies.

---

## 9. @patch

@patch is a decorator that automatically replaces classes or functions with MagicMock objects during test execution.

### Why it is used
It is helpful when a dependency is created inside the source code.

### Example concept

```python
from unittest.mock import patch


@patch("source.notification.EmailService")
def test_send_notification(mock_email_service):
    ...
```

### Key learning
- It provides automatic mocking.
- It temporarily replaces the dependency during the test.
- It is especially useful when the dependency is created internally.

---

## 10. MagicMock vs @patch

| Tool | Who creates the mock | How dependency is provided | Typical use case |
| --- | --- | --- | --- |
| MagicMock | You create it manually | You pass it into the class or function | When you want to control the dependency yourself |
| @patch | Pytest or unittest replaces it | The source code creates the dependency, and patch swaps it | When the dependency is created inside the code |

### Core rule
- MagicMock: you provide the dependency.
- @patch: the source code creates the dependency, so pytest replaces it.

---

## 11. When to use what

| Concept | Use it when |
| --- | --- |
| Assertions | You want to verify output |
| pytest.raises | You want to verify exceptions |
| parametrize | You want to test many inputs with one test |
| Fixtures | You want reusable setup |
| Fixture Scope | You want to control fixture lifetime |
| conftest.py | You want to share fixtures across files |
| Markers | You want to group and run tests by category |
| MagicMock | You want to fake a dependency |
| @patch | You want automatic replacement of an internally created dependency |

---

## 12. Learning journey summary

Here is the simple path to follow:

- ✔ Assertions
- ✔ pytest.raises
- ✔ pytest.mark.parametrize
- ✔ Fixtures
- ✔ Fixture Scope
- ✔ conftest.py
- ✔ Markers
- ✔ MagicMock
- ✔ @patch

---

## 13. Key takeaways

- Assertions are the basic building block of tests.
- pytest.raises helps test error handling.
- parametrize saves time when testing many inputs.
- Fixtures make setup easier and cleaner.
- Fixture scope controls how long a fixture is available.
- conftest.py is a great place for shared fixtures.
- Markers help organize and run tests by category.
- MagicMock is useful for replacing external systems.
- @patch helps replace dependencies created inside the code.

Happy testing!