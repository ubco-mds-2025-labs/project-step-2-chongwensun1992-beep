# README – DATA 533 Project Step 2 Submission

## Group Members
- **Chongwen Sun**
- **Inaara Rajwani**

---

# 1. Project Overview
This project step focuses on:

- Implementing unit tests using Python’s `unittest` framework  
- Enhancing the SmartBudget project with proper error handling  
- Practicing collaborative development using Git branches and pull requests  

All requirements listed in **DATA 533: Project Step 2** have been fully implemented.

---

# 2. Unit Testing Requirements (14 marks)

## ✔ 2.1 Four separate test classes (corresponding to four Step-1 modules)
We created at least four independent test classes in separate files:

| Step-1 Module | Step-2 Test File | Test Class |
|--------------|------------------|-------------|
| `base_record.py` | `tests/test_base_record.py` | `TestRecordBase` |
| `budget_record_controller.py` | `tests/test_budget_record_controller.py` | `TestBudgetRecordController` |
| `file_io_data_controller.py` | `tests/test_json_io.py` | `TestJsonIO` |
| `income.py` & `expense.py` | `tests/test_income_expense.py` | `TestIncomeExpense` |

Additional non-required tests:
- `tests/test_summary.py`
- `tests/test_insights.py`

---

## ✔ 2.2 Each test class has ≥ 2 test cases and each test case contains ≥ 4 assertions
All test classes include multiple test cases with 4+ assertions each, covering:

- Valid inputs  
- Invalid inputs  
- Exception handling  
- Mocked file operations  
- Branching logic  

Assertions used include:
- `assertEqual`
- `assertTrue`
- `assertIn`
- `assertRaises`
- `mock.assert_called_once()`, etc.

---

## ✔ 2.3 Use of `setUp()`, `tearDown()`, `setUpClass()`, `tearDownClass()`
Across multiple test files, we demonstrated correct use of all unittest lifecycle methods:

- `setUpClass()` for class-level initialization  
- `setUp()` for fresh state per test  
- `tearDown()` for cleanup  
- `tearDownClass()` for finalization  

---

## ✔ 2.4 Test Suite Implemented
The test suite is located at:

- tests/test_suite.py


It aggregates all test classes and runs them together:

-- python -m unittest tests/test_suite.py


---

# 3. GitHub Collaboration Requirements (6 marks)

## ✔ New repository created  
Step-1 code was uploaded and collaborators were added.

## ✔ Branches created
Each member created their own feature/testing branch and pushed work regularly.

## ✔ Pull Requests & Merges
All work was merged through PRs after review.

## ✔ Commit history demonstrates equal contribution
Both group members’ commits are visible in the repository history.

---

# 4. Project File Structure

```
smartbudget/
└── tests/
    ├── __init__.py
    ├── test_base_record.py
    ├── test_budget_record_controller.py
    ├── test_income_expense.py
    ├── test_json_io.py
    ├── test_insights.py
    ├── test_summary.py
    └── test_suite.py

```
---

# 5. Completion Statement

All requirements for **DATA 533 – Project Step 2** have been fully satisfied:

- ✔ Four independent test classes  
- ✔ Multiple test cases with ≥ four assertions  
- ✔ Usage of unittest lifecycle methods  
- ✔ Test suite included  
- ✔ GitHub collaboration with branches, PRs, and shared contribution  


