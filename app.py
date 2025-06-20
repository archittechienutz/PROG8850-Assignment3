from flask import Flask, render_template_string, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Secret5555',
    'database': 'testdb'
}

# HTML template for the login form
login_form = '''
<!doctype html>
<title>Login Form</title>
<h2>Login Form</h2>
<form method="post">
  Username: <input type="text" name="username" required><br><br>
  Password: <input type="password" name="password" required><br><br>
  <input type="submit" value="Login">
</form>
{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul>
    {% for message in messages %}
      <li>{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            cursor.close()
            conn.close()
            flash('User added successfully!')
        except Exception as e:
            flash(f'Error: {e}')
        return redirect(url_for('login'))
    return render_template_string(login_form)

if __name__ == '__main__':
    app.run(debug=True)