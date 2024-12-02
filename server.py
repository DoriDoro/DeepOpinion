import sqlite3

from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "d088e8e0ff2734dbbded08ab661f11bfb684b22161eb8d3f20c8d5a4bd6afb9b"

@app.route("/")
def index():
    """
    Renders the home page (index.html) that prompts the user to enter:
    - A username (string).
    - Two positive integers.

    The form submission is handled by the '/display-result' route.
    """
    return render_template("index.html")

@app.route("/display-result", methods=["POST"])
def display_result():
    """
    Processes user input, validates it, and generates a list of even integers
    between the two specified bounds (inclusive). If the input is invalid,
    flashes an error message and redirects to the index page.
    """

    username = request.form.get('username', '').strip()
    int_1 = request.form.get('int_1', '').strip()
    int_2 = request.form.get('int_2', '').strip()

    if not username:
        flash("Please enter a username.", 'danger')

    if not int_1.isdigit() or not int_2.isdigit():
        flash("Both integers must be positive numbers.", 'danger')
        return redirect(url_for('index'))

    int_1, int_2 = int(int_1), int(int_2)

    if int_1 <= 0 or int_2 <= 0:
        flash("Both integers must be positive.", 'danger')
        return redirect(url_for('index'))

    if int_1 >= int_2:
        flash("The second number has to be lager then the first number!", 'danger')
        return redirect(url_for('index'))

    results = [number for number in range(int_1, int_2 + 1) if number % 2 == 0]

    return render_template('results.html', username=username, results=results)
