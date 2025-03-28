import sqlite3
from flask import Flask, request
import os
import boto3
import paramiko

app = Flask(__name__)

# Hardcoded credentials (security issue)
DB_PASSWORD = "super_secret_password123"
AWS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

@app.route('/user/<username>')
def get_user(username):
    # SQL Injection vulnerability
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return str(cursor.fetchall())

@app.route('/upload', methods=['POST'])
def upload_file():
    # Insecure file handling
    file = request.files['file']
    file.save(f"/uploads/{file.filename}")
    return "File uploaded successfully"

def connect_to_server():
    # Insecure SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('example.com', username='admin', password='password123')
    return ssh

def aws_operations():
    # Hardcoded AWS credentials
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_KEY,
        aws_secret_access_key=AWS_SECRET
    )
    
    # Insecure bucket configuration
    s3.create_bucket(
        Bucket='XXXXXXXXX',
        ACL='public-read'
    )

@app.route('/process', methods=['POST'])
def process_data():
    # Cross-site scripting vulnerability
    user_input = request.form['input']
    return f"<div>Processed input: {user_input}</div>"

if __name__ == '__main__':
    # Insecure configuration
    app.run(debug=True, host='0.0.0.0')
