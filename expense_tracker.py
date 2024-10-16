import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from database import Database
from gui_components import create_input_frame, create_button_frame, create_treeview
from charts import show_pie_charts

class ExpenseTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("BudgetBuddy")
        self.master.geometry("800x700")
        self.master.configure(bg="#f0f0f0")

        self.db = Database()
        self.expense_categories = ["Food", "Transportation", "Housing", "Utilities", "Entertainment", "Other"]
        self.income_categories = ["Salary", "Investments", "Gifts", "Other"]

        self.create_widgets()

    def create_widgets(self):
        # App Title
        title_label = tk.Label(self.master, text="BudgetBuddy", font=("Arial", 24, "bold"), bg="#f0f0f0")
        title_label.pack(pady=10)

        # Input Frame
        self.input_frame, self.name_entry, self.amount_entry, self.date_entry, self.type_var, self.category_var, self.category_dropdown = create_input_frame(self.master, self.update_category_options)

        # Buttons Frame
        self.button_frame = create_button_frame(self.master, self.add_transaction, self.delete_selected, self.show_pie_charts)

        # Summary Frame
        self.create_summary_frame()

        # Treeview
        self.tree = create_treeview(self.master)

        self.load_transactions()
        self.update_summary()

    def create_summary_frame(self):
        summary_frame = tk.Frame(self.master, bg="#f0f0f0")
        summary_frame.pack(pady=10)

        self.balance_label = tk.Label(summary_frame, text="Balance: $0.00", font=("Arial", 14, "bold"), bg="#f0f0f0")
        self.balance_label.grid(row=0, column=0, padx=10)

        self.income_label = tk.Label(summary_frame, text="Total Income: $0.00", font=("Arial", 14), bg="#f0f0f0")
        self.income_label.grid(row=0, column=1, padx=10)

        self.expense_label = tk.Label(summary_frame, text="Total Expenses: $0.00", font=("Arial", 14), bg="#f0f0f0")
        self.expense_label.grid(row=0, column=2, padx=10)

    def update_category_options(self):
        if self.type_var.get() == "expense":
            self.category_dropdown['values'] = self.expense_categories
        else:
            self.category_dropdown['values'] = self.income_categories
        self.category_var.set('')

    def add_transaction(self):
        name = self.name_entry.get()
        amount = self.amount_entry.get()
        date = self.date_entry.get_date()
        transaction_type = self.type_var.get()
        category = self.category_var.get()

        if not name or not amount or not category:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")
            return

        self.db.add_transaction(name, amount, date, transaction_type, category)

        self.name_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.category_var.set('')

        self.load_transactions()
        self.update_summary()

    def load_transactions(self):
        self.tree.delete(*self.tree.get_children())
        transactions = self.db.get_all_transactions()
        for transaction in transactions:
            self.tree.insert("", "end", values=transaction)

    def delete_selected(self):
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("Warning", "No item selected")
            return

        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete the selected item(s)?")
        if confirm:
            for item in selected_items:
                values = self.tree.item(item)['values']
                self.db.delete_transaction(values[0])
            self.load_transactions()
            self.update_summary()

    def show_pie_charts(self):
        expense_data = self.db.get_expense_data()
        income_data = self.db.get_income_data()
        show_pie_charts(self.master, expense_data, income_data)

    def update_summary(self):
        total_income = self.db.get_total_income()
        total_expenses = self.db.get_total_expenses()
        balance = total_income - total_expenses

        self.balance_label.config(text=f"Balance: Rs.{balance:.2f}")
        self.income_label.config(text=f"Total Income: Rs.{total_income:.2f}")
        self.expense_label.config(text=f"Total Expenses: Rs.{total_expenses:.2f}")