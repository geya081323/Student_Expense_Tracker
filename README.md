Student Expense Tracker
A Python-based desktop application designed to help students manage and monitor their daily expenses through a simple and user-friendly graphical interface. The application allows users to record transactions, set budget limits, monitor spending, and maintain organized expense records using local CSV storage.

Repository Link
https://github.com/geya081323/Student_Expense_Tracker

Application Description
Student Expense Tracker is a standalone desktop application developed using Python and Tkinter. It assists students in tracking their daily expenditures, monitoring budget limits, and maintaining financial awareness.

The system provides an efficient way to manage personal expenses by allowing users to record transactions, view spending history, calculate total expenses, and receive notifications when spending exceeds the allocated budget.

The application follows Object-Oriented Programming (OOP) principles and demonstrates software engineering concepts such as Encapsulation, Abstraction, Polymorphism, and Dependency Inversion.

Features
Set and update a personal budget limit
Record expense transactions
Store transaction records using CSV files
View transaction history
Delete unwanted transactions
Calculate total expenses automatically
Monitor spending against a budget limit
Receive budget alerts when spending exceeds the limit
Execute automated tests using PyTest
OOP Concepts Applied
Encapsulation
The Transaction class uses private attributes to protect transaction data from direct modification.

Abstraction
The abstract Storage class defines the methods required for data persistence.

Polymorphism
Different storage implementations can be used interchangeably as long as they follow the Storage interface.

Dependency Inversion Principle (DIP)
The application depends on abstractions rather than concrete storage implementations, promoting flexibility and maintainability.

Technologies Used
Python 3
Tkinter
CSV File Handling
PyTest
Object-Oriented Programming (OOP)
Project Structure
Student_Expense_Tracker/
│
├── expense_app.py
├── test_expense.py
├── expenses.csv
│
├── Transaction
├── Storage
├── CSVStorage
├── BudgetSummarizer
└── ExpenseApp
Main Components
Transaction
Stores transaction information including:

Amount
Date
Description
Storage
Abstract class that defines:

Save functionality
Load functionality
CSVStorage
Handles:

Saving transaction records
Loading transaction records
Rewriting transaction data
BudgetSummarizer
Responsible for:

Calculating total expenses
Determining budget status
ExpenseApp
Provides the graphical user interface and application controls.

Testing
The project includes automated tests using PyTest.

Test Coverage
Transaction creation and validation
Budget calculations
CSV storage functionality
Storage abstraction and polymorphism
How to Run
Requirements
Python 3.x installed on your computer
Run the Application
python expense_app.py
Run the Tests
pytest test_expense.py
Expected Output
The application allows users to:

Set a budget limit
Record expenses
View transaction history
Delete transactions
Monitor total spending
Receive budget alerts
Authors
Developed by:

Angela F. De Guzman
Daniel John F. Gudao
Mary Joy E. Granado
Bachelor of Science in Information Technology

Object-Oriented Programming

Notes
Designed for educational purposes.
Uses CSV files for local data storage.
Demonstrates Object-Oriented Programming principles.
Can be extended to support databases, reports, and advanced expense analytics in future versions.
