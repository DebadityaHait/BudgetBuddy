import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def create_input_frame(master, update_category_callback):
    input_frame = tk.Frame(master, bg="#f0f0f0")
    input_frame.pack(pady=10)

    tk.Label(input_frame, text="Name:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    name_entry = tk.Entry(input_frame, font=("Arial", 12))
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Amount:", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    amount_entry = tk.Entry(input_frame, font=("Arial", 12))
    amount_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Date:", bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    date_entry = DateEntry(input_frame, width=12, background='darkblue', foreground='white', borderwidth=2, font=("Arial", 12))
    date_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Type:", bg="#f0f0f0").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    type_var = tk.StringVar(value="expense")
    tk.Radiobutton(input_frame, text="Expense", variable=type_var, value="expense", bg="#f0f0f0", command=update_category_callback).grid(row=3, column=1, sticky="w")
    tk.Radiobutton(input_frame, text="Income", variable=type_var, value="income", bg="#f0f0f0", command=update_category_callback).grid(row=3, column=1, sticky="e")

    tk.Label(input_frame, text="Category:", bg="#f0f0f0").grid(row=4, column=0, padx=5, pady=5, sticky="e")
    category_var = tk.StringVar()
    category_dropdown = ttk.Combobox(input_frame, textvariable=category_var, state="readonly", font=("Arial", 12))
    category_dropdown.grid(row=4, column=1, padx=5, pady=5)

    return input_frame, name_entry, amount_entry, date_entry, type_var, category_var, category_dropdown

def create_button_frame(master, add_callback, delete_callback, chart_callback):
    button_frame = tk.Frame(master, bg="#f0f0f0")
    button_frame.pack(pady=10)

    add_button = tk.Button(button_frame, text="Add Transaction", command=add_callback, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
    add_button.grid(row=0, column=0, padx=5)

    delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_callback, bg="#F44336", fg="white", font=("Arial", 12, "bold"))
    delete_button.grid(row=0, column=1, padx=5)

    pie_chart_button = tk.Button(button_frame, text="Show Pie Charts", command=chart_callback, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
    pie_chart_button.grid(row=0, column=2, padx=5)

    return button_frame

def create_treeview(master):
    tree = ttk.Treeview(master, columns=("ID", "Name", "Amount", "Date", "Type", "Category"), show="headings", height=15)
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Amount", text="Amount")
    tree.heading("Date", text="Date")
    tree.heading("Type", text="Type")
    tree.heading("Category", text="Category")
    tree.column("ID", width=50)
    tree.column("Name", width=150)
    tree.column("Amount", width=100)
    tree.column("Date", width=100)
    tree.column("Type", width=100)
    tree.column("Category", width=150)
    tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(master, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    return tree