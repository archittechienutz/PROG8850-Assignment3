# PROG8850 - Assignment 3: Web App with Database & Selenium Testing

This project is a simple Python Flask web application that uses a MySQL database to store user credentials submitted through a login form. The project also includes an automated test script using Selenium to verify the application's functionality.

This README provides instructions on how to set up and run the entire project within a GitHub Codespace environment.

## 1. Setup and Installation

The environment comes with most tools pre-installed. You only need to install the Python packages and set up the database.

### Step 1: Install Python Dependencies

In the terminal, run the following command to install Flask, Selenium, and the MySQL connector:
```bash
pip install -r requirements.txt
```

### Step 2: Start the MySQL Database Server

This project uses Ansible to automate the database server setup. Run the following command:
```bash
ansible-playbook up.yml
```
This will start the MySQL service inside your Codespace.

### Step 3: Create the Database and Table

Next, you need to create the `users` table by running the SQL script.

First, log into the MySQL command line client. The password is `Secret5555`.
```bash
mysql -u root -p -h 127.0.0.1
```

Once you see the `mysql>` prompt, run the `source` command to execute the script:
```sql
source schema_changes.sql;
```

After the command succeeds, you can leave the MySQL client:
```sql
exit;
```
Your database is now ready.

## 2. Running the Project

To run the application and the test, you will need **two separate terminals** open in your Codespace.

### Terminal 1: Run the Web Application

In your first terminal, start the Flask web server:
```bash
python app.py
```
Leave this terminal running. It will serve your web application, and a notification should appear allowing you to open the web page in a browser.

### Terminal 2: Run the Selenium Test

Open a new, second terminal. With the web application still running in the first terminal, execute the automated test script:
```bash
python test_selenium.py
```
The script will run a headless Firefox browser, interact with your web app, and print the results to the terminal. You should see a `✅ Test Passed` message upon successful completion.

## 3. Project File Descriptions

- **`app.py`**: The main Python Flask application that serves the login page and handles form submissions.
- **`test_selenium.py`**: The automated test script that uses Selenium to test the login functionality and verify database insertion.
- **`requirements.txt`**: Lists the required Python packages for the project.
- **`schema_changes.sql`**: The SQL script to create the database (`testdb`) and the `users` table.
- **`up.yml` / `down.yml`**: Ansible playbooks to start and stop the MySQL database service.
- **`.devcontainer`**: Contains the configuration for the GitHub Codespace environment. 