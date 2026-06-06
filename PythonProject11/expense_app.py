import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
from abc import ABC, abstractmethod
from datetime import datetime

# --- 1. THE DATA (Encapsulation: Keeping attributes private) ---
class Transaction:
    def __init__(self, cost, date, description):
        self.__cost = float(cost)
        self.__date = date
        self.__description = description

    def get_details(self):
        return {"Amount": self.__cost, "Date": self.__date, "Description": self.__description}


# --- 2. STORAGE SYSTEM (Dependency Inversion & Polymorphism) ---
class Storage(ABC):

    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self):
        pass


class CSVStorage(Storage):

    def __init__(self, filename="expenses.csv"):
        self.file_path = filename

    def save(self, data):
        fields = ["Amount", "Date", "Description"]
        with open(self.file_path, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            if f.tell() == 0:
                writer.writeheader()
            writer.writerow(data)

    def rewrite_all(self, all_data):
        fields = ["Amount", "Date", "Description"]
        with open(self.file_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(all_data)

    def load(self):
        try:
            with open(self.file_path, "r") as f:
                return list(csv.DictReader(f))
        except FileNotFoundError:
            return []


# --- 3. BUSINESS LOGIC (Budget Summarizer) ---
class BudgetSummarizer:
    def __init__(self, budget_limit=0):
        self.budget_limit = budget_limit

    @staticmethod
    def calculate_total(transactions):
        return sum(float(t['Amount']) for t in transactions)

    def is_over_budget(self, total):
        return total > self.budget_limit


# --- 4. USER INTERFACE ---
class ExpenseApp:
    def __init__(self, master):
        self.root = master
        self.root.title("✨ Student Expenses Tracker ✨")
        self.root.geometry("480x680")
        self.root.resizable(False, False)
        self.root.configure(bg="#E3F2FD")

        self.storage = CSVStorage()
        self.summarizer = BudgetSummarizer()

        self.font_main = ("Segoe UI", 10)
        self.font_bold = ("Segoe UI", 10, "bold")

        title_banner = tk.Label(
            self.root,
            text="✨ STUDENT EXPENSES TRACKER ✨",
            font=("Segoe UI", 16, "bold"),
            bg="#1976D2",
            fg="white",
            pady=12
        )
        title_banner.pack(fill="x")

        tk.Label(
            self.root,
            text="💰 BUDGET MANAGEMENT 💰",
            font=("Segoe UI", 13, "bold"),
            bg="#E3F2FD",
            fg="#1565C0"
        ).pack(pady=(20, 5))

        self.budget_label = tk.Label(
            self.root,
            text="Current Limit: ₱0.00",
            font=("Segoe UI", 11, "bold"),
            bg="#E3F2FD",
            fg="#2E7D32"
        )
        self.budget_label.pack()

        tk.Button(
            self.root,
            text="SET NEW BUDGET",
            command=self.set_budget,
            bg="#FFD54F",
            fg="black",
            activebackground="#FFC107",
            relief="flat",
            padx=12
        ).pack(pady=10)

        input_frame = tk.Frame(
            self.root,
            bg="#FFFFFF",
            bd=2,
            relief="ridge"
        )
        input_frame.pack(pady=10, padx=20)

        tk.Label(
            input_frame,
            text="Cost (₱):",
            font=self.font_bold,
            bg="#FFFFFF",
            fg="#0D47A1"
        ).grid(row=0, column=0, sticky="w", padx=5)

        self.cost_entry = tk.Entry(
            input_frame,
            font=self.font_main,
            relief="groove",
            bd=2,
            bg="#FFFDE7"
        )
        self.cost_entry.grid(row=0, column=1, pady=5)

        tk.Label(
            input_frame,
            text="Description:",
            font=self.font_bold,
            bg="#FFFFFF",
            fg="#0D47A1"
        ).grid(row=1, column=0, sticky="w", padx=5)

        self.desc_entry = tk.Entry(
            input_frame,
            font=self.font_main,
            relief="groove",
            bd=2,
            bg="#FFFDE7"
        )
        self.desc_entry.grid(row=1, column=1, pady=5)

        tk.Button(
            self.root,
            text="➕ LOG TRANSACTION",
            command=self.add_transaction,
            bg="#43A047",
            fg="white",
            activebackground="#2E7D32",
            font=self.font_bold,
            relief="flat",
            width=22
        ).pack(pady=10)

        tk.Label(
            self.root,
            text="📋 TRANSACTION HISTORY",
            font=("Segoe UI", 11, "bold"),
            bg="#E3F2FD",
            fg="#6A1B9A"
        ).pack(pady=(15, 0))

        self.listbox = tk.Listbox(
            self.root,
            width=55,
            height=12,
            font=self.font_main,
            relief="groove",
            bd=3,
            bg="#FFFFFF",
            fg="#212121",
            selectbackground="#42A5F5",
            selectforeground="white"
        )
        self.listbox.pack(pady=5, padx=20)

        btn_frame = tk.Frame(self.root, bg="#E3F2FD")
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame,
            text="🗑 DELETE SELECTED",
            command=self.delete_transaction,
            bg="#EF5350",
            fg="white",
            activebackground="#D32F2F",
            relief="flat",
            width=18
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            btn_frame,
            text="📊 CHECK STATUS",
            command=self.display_summary,
            bg="#29B6F6",
            fg="white",
            activebackground="#0288D1",
            relief="flat",
            width=18
        ).grid(row=0, column=1, padx=5)

        self.refresh_view()

    def set_budget(self):
        new_limit = simpledialog.askstring("Budget Setup", "Enter new budget limit:")
        try:
            if new_limit:
                self.summarizer.budget_limit = float(new_limit)
                self.budget_label.config(text=f"Current Limit: ₱{self.summarizer.budget_limit:,.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a numeric value for the budget.")

    def add_transaction(self):
        try:
            cost = float(self.cost_entry.get())

            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            t = Transaction(
                cost,
                current_datetime,
                self.desc_entry.get()
            )

            self.storage.save(t.get_details())

            self.cost_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)

            self.refresh_view()

        except ValueError:
            messagebox.showerror("Error", "Invalid cost. Please enter a number.")

    def delete_transaction(self):
        try:
            selected_index = self.listbox.curselection()[0]
            all_data = self.storage.load()
            all_data.pop(selected_index)
            self.storage.rewrite_all(all_data)
            self.refresh_view()
        except IndexError:
            messagebox.showwarning("Selection", "Please select a transaction to delete.")

    def display_summary(self):
        data = self.storage.load()
        total = self.summarizer.calculate_total(data)

        if self.summarizer.is_over_budget(total):
            messagebox.showwarning(
                "Budget Alert",
                f"Warning: Limit Exceeded!\nSpent: ₱{total:,.2f}"
            )
        else:
            remaining = self.summarizer.budget_limit - total
            messagebox.showinfo(
                "Status",
                f"Within Budget\nSpent: ₱{total:,.2f}\nRemaining: ₱{remaining:,.2f}"
            )

    def refresh_view(self):
        self.listbox.delete(0, tk.END)
        for item in self.storage.load():
            self.listbox.insert(
                tk.END,
                f"💸 ₱{item['Amount']}   •   {item['Description']}"
            )


if __name__ == "__main__":
    main_window = tk.Tk()
    app = ExpenseApp(main_window)
    main_window.mainloop()
