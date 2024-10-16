import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="debaditya2005@",
            database="extracker"
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            amount DECIMAL(10, 2),
            date DATE,
            type ENUM('income', 'expense'),
            category VARCHAR(255)
        )
        """)
        self.conn.commit()

    def add_transaction(self, name, amount, date, transaction_type, category):
        self.cursor.execute("""
        INSERT INTO transactions (name, amount, date, type, category)
        VALUES (%s, %s, %s, %s, %s)
        """, (name, amount, date, transaction_type, category))
        self.conn.commit()

    def get_all_transactions(self):
        self.cursor.execute("SELECT id, name, amount, date, type, category FROM transactions ORDER BY date DESC")
        return self.cursor.fetchall()

    def delete_transaction(self, transaction_id):
        self.cursor.execute("DELETE FROM transactions WHERE id = %s", (transaction_id,))
        self.conn.commit()

    def get_expense_data(self):
        self.cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE type='expense' GROUP BY category")
        return self.cursor.fetchall()

    def get_income_data(self):
        self.cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE type='income' GROUP BY category")
        return self.cursor.fetchall()

    def get_total_income(self):
        self.cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
        return self.cursor.fetchone()[0] or 0

    def get_total_expenses(self):
        self.cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
        return self.cursor.fetchone()[0] or 0