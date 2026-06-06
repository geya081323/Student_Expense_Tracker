Student Expense Tracker

Application Description
Student Expense Tracker is a standalone Python desktop application designed to help students monitor and manage their daily expenses effectively. The system provides a simple graphical interface that allows users to record expenses, set budget limits, review transaction history, and monitor spending status.

The application was developed using Python and follows Object-Oriented Programming (OOP) principles to ensure modularity, maintainability, and code reusability. It operates locally using CSV file storage and does not require an internet connection or external database.

The application allows users to:
- Set and update a personal budget limit
- Record expense transactions with corresponding descriptions
- Store expense records using CSV file handling
- View transaction history in a graphical user interface
- Delete unwanted transaction records
- Calculate total expenses automatically
- Monitor spending against a predefined budget limit
- Receive notifications when expenses exceed the allocated budget
- Execute automated tests to verify system functionality

Built with a clean graphical user interface using Tkinter, the system emphasizes simplicity, usability, and accessibility. The application follows a structured Input–Process–Output model, ensuring reliable performance and organized expense management.

Through this application, students can develop better financial awareness and budgeting habits by keeping track of their daily expenditures in a centralized and easy-to-use platform.

------------------------------------------------------------

OOP Concepts Used

Encapsulation

Private attributes are used within the Transaction class to protect transaction data from direct modification.

Abstraction

The Storage abstract class defines standard methods that all storage implementations must follow.

Polymorphism

Different storage implementations can be substituted as long as they follow the Storage interface.

Dependency Inversion Principle (DIP)

High-level modules depend on abstractions rather than concrete implementations, promoting flexibility and scalability.

------------------------------------------------------------

Technologies Used
- Python (Core Programming Language)
- Tkinter (Graphical User Interface Framework)
- CSV File Handling
- PyTest (Automated Testing Framework)
- Object-Oriented Programming (OOP)

------------------------------------------------------------

Project Structure

Student_Expense_Tracker/

|

|-- expense_app.py

|-- expenses.csv

|-- test_expense.py

|

|-- Transaction Class

|-- Storage Interface

|-- CSVStorage Class

|-- BudgetSummarizer Class

|-- ExpenseApp Class


------------------------------------------------------------

System Components

Transaction
Responsible for storing expense transaction information, including:
- Amount
- Date
- Description

Storage
An abstract class that defines the standard methods for data persistence.

CSVStorage
Responsible for:
- Saving expense records
- Loading stored records
- Updating transaction data

BudgetSummarizer
Responsible for:
- Calculating total expenses
- Determining whether the user is within the budget limit

ExpenseApp
Provides the graphical user interface and serves as the main application controller.

------------------------------------------------------------

Testing

The project includes automated test cases developed using PyTest.

Test Coverage
- Transaction creation and validation
- Budget calculation and monitoring
- CSV storage functionality
- Storage abstraction and polymorphism verification

The tests help ensure that system functionalities operate as expected and maintain software reliability.

------------------------------------------------------------

How to Run

Requirements
- Python 3.x

Application Execution
Open the project folder and execute the main application file:

 python expense_app.py

Running Tests
Execute the automated test file using PyTest:

 pytest test_expense.py

------------------------------------------------------------

Expected Output
The application enables users to:
1. Set a budget limit
2. Record expense transactions
3. View all recorded expenses
4. Delete selected transactions
5. Monitor total spending
6. Receive budget alerts when limits are exceeded

------------------------------------------------------------

Authors
Developed by:
- Angela F. De Guzman (GITHUB: https://github.com/geya081323)
- Daniel John F. Gudao (GITHUB: https://github.com/gudaodanieljohn)
- Mary Joy E. Granado (GITHUB: https://github.com/marygranado)

In Partial Fulfillment of the Requirements for the Subject Object-Oriented Programming under the Bachelor of Science in Information Technology program.

------------------------------------------------------------

Notes
- Designed for educational purposes
- Uses CSV files for local data storage
- Demonstrates Object-Oriented Programming concepts and software design principles
- Can be extended to support database integration, report generation, and advanced expense analytics in future versions
