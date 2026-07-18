# Pytest Markers Cheat Sheet

## What are Markers?

A **marker** is metadata (a label) attached to a test function.

Markers help pytest to:

- Run specific groups of tests
- Skip tests
- Mark expected failures
- Parameterize tests
- Apply fixtures
- Categorize tests (Smoke, Integration, Kafka, etc.)

---

# Built-in Markers

These markers are provided by pytest and directly affect test execution.

| Marker | Usage |
|---------|-------|
| `@pytest.mark.parametrize` | Execute the same test multiple times using different input datasets. |
| `@pytest.mark.skip` | Skip the test unconditionally. |
| `@pytest.mark.skipif(condition)` | Skip the test only when a specified condition evaluates to `True`. |
| `@pytest.mark.xfail` | Execute the test but mark it as an expected failure (known bug or unfinished feature). |
| `@pytest.mark.filterwarnings` | Ignore or control specific warnings during test execution. |
| `@pytest.mark.usefixtures("fixture_name")` | Execute one or more fixtures without explicitly passing them as test function arguments. |

---

# Common Custom Markers

These markers are created by developers and usually registered inside `pytest.ini`.

| Marker | Usage |
|---------|-------|
| `@pytest.mark.smoke` | Mark critical, fast-running tests that verify core application functionality. |
| `@pytest.mark.slow` | Mark tests that take significantly longer to execute. |
| `@pytest.mark.integration` | Mark tests involving external systems such as databases, APIs, Kafka, etc. |
| `@pytest.mark.unit` | Mark isolated unit tests that don't depend on external resources. |
| `@pytest.mark.api` | Mark REST API-related tests. |
| `@pytest.mark.db` | Mark database-related tests. |
| `@pytest.mark.kafka` | Mark Kafka producer/consumer tests. |
| `@pytest.mark.spark` | Mark Spark/PySpark-related tests. |
| `@pytest.mark.bigquery` | Mark Google BigQuery-related tests. |
| `@pytest.mark.regression` | Mark tests that ensure previously fixed bugs do not reappear. |
| `@pytest.mark.sanity` | Mark a small subset of tests that validate major functionality before deeper testing. |

---

# Plugin-Based Markers

These require installing additional pytest plugins.

| Marker | Usage |
|---------|-------|
| `@pytest.mark.asyncio` | Execute asynchronous (`async def`) test functions. *(pytest-asyncio)* |
| `@pytest.mark.timeout` | Fail a test if it exceeds a specified execution time. *(pytest-timeout)* |
| `@pytest.mark.order` | Execute tests in a predefined order. *(pytest-order)* |

---

# Most Frequently Used Markers

These are the markers you'll encounter most often in real-world projects.

### 1. `@pytest.mark.parametrize`

**Purpose**

Run the same test multiple times using different inputs.

Example

```python
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (5, 5, 10),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected
```

---

### 2. `@pytest.mark.skip`

**Purpose**

Completely skip a test.

Example

```python
@pytest.mark.skip(reason="Feature under development")
def test_login():
    ...
```

Result

```
SKIPPED
```

---

### 3. `@pytest.mark.skipif`

**Purpose**

Skip a test only if a condition is satisfied.

Example

```python
import sys

@pytest.mark.skipif(
    sys.platform == "win32",
    reason="Linux only"
)
def test_linux_feature():
    ...
```

---

### 4. `@pytest.mark.xfail`

**Purpose**

Run the test but expect it to fail.

Useful when:

- Known bug exists
- Bug fix is under development
- You don't want CI to fail

Example

```python
@pytest.mark.xfail(reason="Known divide-by-zero bug")
def test_divide():
    divide(10, 0)
```

Result

```
XFAIL
```

---

### 5. `@pytest.mark.smoke`

**Purpose**

Mark fast, critical tests.

Example

```python
@pytest.mark.smoke
def test_application_starts():
    ...
```

Run only smoke tests

```bash
pytest -m smoke
```

---

### 6. `@pytest.mark.slow`

**Purpose**

Mark long-running tests.

Example

```python
@pytest.mark.slow
def test_load_10gb_data():
    ...
```

Run only slow tests

```bash
pytest -m slow
```

Exclude slow tests

```bash
pytest -m "not slow"
```

---

# Running Tests Using Markers

Run only smoke tests

```bash
pytest -m smoke
```

Run only slow tests

```bash
pytest -m slow
```

Run smoke and regression tests

```bash
pytest -m "smoke or regression"
```

Exclude slow tests

```bash
pytest -m "not slow"
```

Run integration tests

```bash
pytest -m integration
```

---

# Registering Custom Markers

Create a `pytest.ini` file.

```ini
[pytest]
markers =
    smoke: Smoke tests
    slow: Slow running tests
    integration: Integration tests
    regression: Regression tests
    kafka: Kafka tests
```

Without registration, pytest will issue warnings for unknown custom markers.

---

# Quick Summary

| Marker | Purpose |
|---------|----------|
| `parametrize` | Execute one test with multiple datasets. |
| `skip` | Ignore a test completely. |
| `skipif` | Conditionally skip a test. |
| `xfail` | Expect the test to fail. |
| `smoke` | Label fast, critical tests. |
| `slow` | Label long-running tests. |
| `integration` | Label tests using external systems. |
| `unit` | Label isolated unit tests. |
| `api` | Label API tests. |
| `db` | Label database tests. |
| `kafka` | Label Kafka tests. |
| `spark` | Label Spark tests. |
| `bigquery` | Label BigQuery tests. |
| `regression` | Label regression tests. |
| `sanity` | Label basic validation tests. |