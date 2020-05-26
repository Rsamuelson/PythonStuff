from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    # Show the loan input form:
    return render_template("loan-form.html")


# Add the @app.route() decorator so POST to /compute runs this method:
@app.route('/compute', methods=['POST'])
def compute():
    # For a POST request, request.form is a dictionary that contains the posted
    # form data. It will have string values for 'rate', 'years', and 'amount'.
    # These values are just set to samples so the code will run, but you need
    # to get the values from the request.form[] dictionary and convert to
    # int or float as needed.
    rate = float(request.form['rate'])
    years = int(request.form['years'])
    amount = float(request.form['amount'])
    print(rate, years, amount)
    payment = 0
    total_interest = 0
    amort_table = []

    # Use the values to compute the payment.
    # Then loop over the months, compute the interest, payment, and
    monthlyrate = float(rate) / 12.0
    months = int(years) * 12
    payment = float(amount) * ((monthlyrate * (1 + monthlyrate) ** months) /
                                ((1 + monthlyrate) ** months - 1))
    balance = float(amount)

    for month in range(months):
        interest = balance * monthlyrate
        principal = payment - interest
        balance = balance - principal
        total_interest += interest
        amort_table.insert(month, {"month": month + 1, 'payment': payment, 'principal': principal, 'interest': interest, 'balance': balance})

    # After the loop is complete, render the output page. Send values for
    # the rate, years, amount, payment, and the amortization table:
    return render_template("loan-table.html", rate=rate, years=years,
                           amount=amount, payment=payment,
                           total_interest=total_interest,
                           amort_table=amort_table)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)