"""
BudgetRecordController
----------------------

Coordinates all record-related operations in SmartBudget:
    - Adding income and expenses
    - Displaying summaries and analytical insights
    - Triggering visualizations
    - Forwarding new records to the storage layer

This class serves as the CONTROLLER layer connecting:
    entity  → Income, Expense
    analysis → summary, insights, plots
    storage → append_to_json
"""

from smartbudget.entity.income import Income
from smartbudget.entity.expense import Expense

from smartbudget.analysis_module_1.summary import (
    total_income, total_expenses, budget_balance
)
from smartbudget.analysis_module_1.insights import (
    income_details, expense_details, plot_expense_by_category
)

from smartbudget.file_io_module_3 import append_to_json


class BudgetRecordController:
    """
    Controller class responsible for:
    - Managing income and expense records
    - Handling all user-facing operations (summary, details, plots)
    - Creating and storing new financial records

    This controller interacts with model classes (Income, Expense)
    and with I/O helper functions such as append_to_json().
    """

    def __init__(self):
        self.incomes = []
        self.expenses = []

    # ------------------ Display Functions ------------------ #

    def show_summary(self):
        """
        Display overall budget summary, including:
        - Total income
        - Total expenses
        - Remaining balance
        The actual calculations are handled by helper functions.
        """
        print("\n=== Budget Summary ===")
        print("Total Income:", total_income())
        print("Total Expenses:", total_expenses())
        print("Balance:", budget_balance())
        print("=======================\n")

    def show_income_details(self):
        """
        Create a new expense record.
        Logic mirrors add_income(), but includes category.
        """
        print("\n=== Income Details ===")
        details = income_details()
        if not details:
            print("No incomes recorded.\n")
            return
        for d in details:
            print(" -", d)
        print()

    def show_expense_details(self):
        print("\n=== Expense Details ===")
        details = expense_details()
        if not details:
            print("No expenses recorded.\n")
            return
        for d in details:
            print(" -", d)
        print()

    def show_expense_plot(self):
        print("\n=== Expense Visualization ===")
        print("Generating chart...")
        plot_expense_by_category()
        print("\n✔ Chart displayed!\n")

    # ------------------ Record Creation ------------------ #

    def add_income(self):
        print("\n--- Add Income ---")
        name = input("Enter income name: ")
        amount = float(input("Enter amount: "))
        source = input("Enter source: ")

        inc = Income(name, amount, source)
        self.incomes.append(inc)
        append_to_json([inc])

        print("\n✔ Income added:", inc.describe(), "\n")

    def add_expense(self):
        print("\n--- Add Expense ---")
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        exp = Expense(name, amount, category)
        self.expenses.append(exp)
        append_to_json([exp])

        print("\n✔ Expense added:", exp.describe(), "\n")
