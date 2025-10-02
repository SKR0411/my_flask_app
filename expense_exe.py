import tkinter as tk

expenses = []

def add_expense():
    item = item_entry.get()
    amount = float(amount_entry.get())
    expenses.append({"item": item, "amount": amount})
    item_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    update_list()

def update_list():
    listbox.delete(0, tk.END)
    total = 0
    for e in expenses:
        listbox.insert(tk.END, f"{e['item']}: ₹{e['amount']}")
        total += e['amount']
    total_label.config(text=f"Total: ₹{total}")

root = tk.Tk()
root.title("Expense Tracker")

tk.Label(root, text="Item:").pack()
item_entry = tk.Entry(root)
item_entry.pack()

tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Button(root, text="Add", command=add_expense).pack()

listbox = tk.Listbox(root, width=40)
listbox.pack()

total_label = tk.Label(root, text="Total: ₹0")
total_label.pack()

root.mainloop()