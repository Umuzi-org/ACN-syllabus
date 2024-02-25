---
_db_id: 997
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/manual-app-deployment/postgresql-installation
  - k8s/manual-app-deployment/nginx-tls
ready: true
submission_type: continue_repo
tags:
- kubernetes
- python
title: Python App Setup
---

Let's setup the Python app on your instance.

First, on the GitHub repository, create a file named `app.py` under a folder named `python`. This is the app's source code.

```python
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Database connection parameters
db_params = {
    "dbname": "yourdb",
    "user": "youruser",
    "password": "yourpassword",
    "host": "localhost",  # Change this if your database is on a different host
}

# Function to create the "pressed" table
def create_pressed_table():
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        # Check if a row exists in the "pressed" table
        cur.execute("CREATE TABLE IF NOT EXISTS pressed (count INTEGER);")

        cur.execute("SELECT 1 FROM pressed LIMIT 1;")

        if cur.fetchone() is None:
            # If no row exists, insert an initial row with count = 1
            cur.execute("INSERT INTO pressed (count) VALUES (1);")
        else:
            # If a row exists, increment the count
            cur.execute("UPDATE pressed SET count = count + 1;")

        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn:
            conn.close()

# Function to get the count from the "pressed" table
def get_pressed_count():
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        # Retrieve the count from the "pressed" table
        cur.execute("SELECT count FROM pressed;")
        count = cur.fetchone()[0] if cur.rowcount > 0 else 0
        return count
    except Exception as e:
        print(str(e))
        return 0
    finally:
        if conn:
            conn.close()

# Define a route to get the status
@app.route('/api/get-status', methods=['GET'])
def get_status():
    # Get the count from the "pressed" table
    count = get_pressed_count()

    return jsonify({'count': count})

# Define a route to increment the "pressed" table
@app.route('/api/pressed', methods=['GET'])
def increment_pressed():
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        # Increment the "pressed" table
        cur.execute("UPDATE pressed SET count = count + 1;")
        conn.commit()

        # Get the updated count
        count = get_pressed_count()

        return jsonify({'count': count})
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    # Create the "pressed" table if it doesn't exist
    create_pressed_table()

    app.run(host='0.0.0.0', port=5000)  # Replace with your preferred host and port

```

Next, create a file named `myflaskapp.service` under the same folder with the content below. This file will create a service which will ensure our app is running in the backgroud.

```
[Unit]
Description=My Flask App
After=network.target

[Service]
User=root
WorkingDirectory=/home/ubuntu/umuzi-k8s/python
ExecStart=/home/ubuntu/umuzi-k8s/python/venv/bin/python /home/ubuntu/umuzi-k8s/python/app.py

[Install]
WantedBy=multi-user.target
```

Save the files, commit and pull the changes from the repository on the EC2 instance.

---

Now, on the EC2 instance, let's configure our Python environment.

Create a Python virtual environment to isolate our app dependencies.

```
# updates the package manager
sudo apt update

# installs Python virtual environment
sudo apt install python3.10-venv

# createa a virtual environment named `vevn`
python3 -m venv /home/ubuntu/umuzi-k8s/python/venv
```

Now let's access the virtual environment and install our app's dependencies.

```
# activates the virtual environment
source /home/ubuntu/umuzi-k8s/python/venv/bin/activate

# installs the system dependencies for psycopg2
# psycopg2 is used to access the PostgreSQL database from a Python app
sudo apt install build-essential libssl-dev python3-dev libpq-dev -y

# installs the app's dependencies
pip install psycopg2 flask
```

Setup the Python app's service.

```
# copy the service file
sudo cp python/myflaskapp.service /etc/systemd/system/myflaskapp.service

# reload the service daemon
sudo systemctl daemon-reload

# enable and start the Python app
sudo systemctl enable myflaskapp
sudo systemctl start myflaskapp
sudo systemctl status myflaskapp
```

Run the following command to test if the app is running properly:

```
# accesses the app's API
# should return {"count":1}
curl http://127.0.0.1:5000/api/get-status
```