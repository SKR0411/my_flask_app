from flask import Flask, render_template_string, request

app = Flask(__name__)

expenses = []

html = """
<!DOCTYPE html>
<html>
<head><title>Expense Tracker</title></head>
<body>
  <h1>Expense Tracker</h1>
  <form method="post">
    Item: <input name="item">
    Amount: <input name="amount" type="number" step="0.01">
    <button type="submit">Add</button>
  </form>
  <ul>
    {% for e in expenses %}
      <li>{{e['item']}}: ₹{{e['amount']}}</li>
    {% endfor %}
  </ul>
  <h3>Total: ₹{{total}}</h3>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        item = request.form["item"]
        amount = float(request.form["amount"])
        expenses.append({"item": item, "amount": amount})
    total = sum(e["amount"] for e in expenses)
    return render_template_string(html, expenses=expenses, total=total)

if __name__ == "__main__":
    app.run(debug=True)
