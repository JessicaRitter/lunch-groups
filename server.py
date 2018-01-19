from flask import Flask, render_template, redirect, request, session
from apartmentlist import create_group, create_groups, find_group_sizes
import jinja2

app = Flask(__name__)

app.secret_key = "APP_KEY"


@app.route('/', methods=["GET", "POST"])
def show_page():
    return render_template('home.html')

@app.route('/names', methods=["POST"])
def show_names():
    names = request.form.get("names")
    print names
    names = names.split(' ')
    num_emps = len(names)
    groups = create_groups(num_emps)
    employee_groups = create_group(groups, names)

    return render_template('names.html',employee_groups=employee_groups,
                                groups=groups)














if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000)

