import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def show_pie_charts(master, expense_data, income_data):
    chart_window = tk.Toplevel(master)
    chart_window.title("Expense and Income Distribution")
    chart_window.geometry("800x400")

    expense_labels = [row[0] for row in expense_data]
    expense_values = [row[1] for row in expense_data]

    income_labels = [row[0] for row in income_data]
    income_values = [row[1] for row in income_data]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    ax1.pie(expense_values, labels=expense_labels, autopct='%1.1f%%', startangle=90)
    ax1.set_title("Expense Distribution")

    ax2.pie(income_values, labels=income_labels, autopct='%1.1f%%', startangle=90)
    ax2.set_title("Income Distribution")

    canvas = FigureCanvasTkAgg(fig, master=chart_window)
    canvas.draw()
    canvas.get_tk_widget().pack()