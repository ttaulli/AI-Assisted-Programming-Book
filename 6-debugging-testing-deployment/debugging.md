# Documentation, Debugging & Deployment

# Comments

/doc deprecated

With Agent mode, may see much less of / slash commands

# API

Prompt:  Please generate detailed API documentation for this API. The documentation should include descriptions for each endpoint, required request parameters, possible responses, and examples of requests and responses in JSON format. Additionally, include potential error codes and their meanings. Use clear headings and structure the documentation for easy readability. Create this as a separate markdown file in the 6-debugging-testing-deployment folder 

# Debugging

35% to 50% of a developer's time is spent on debugging

Syntax Errors

Code does not conform to the syntax rules of the programming language

Usually caught by the compiler or interpreter before the code is executed

Logical Errors

These bugs occur when the code is syntactically correct but does not produce the desired result due to flawed logic or reasoning

# /fix command in GitHub Copilot

# Logical error
def find_max(a, b):
    if a < b:
        return a
    else:
        return b
    
print(find_max(3, 5)) # 3


# Error handling
def divide_numbers(a, b):
    return a / b

print(divide_numbers(10, 0)) 


# optimization
def calculate_squares(numbers):
    squares = []
    for num in numbers:
        squares.append(num * num)
    return squares

print(calculate_squares([1, 2, 3, 4, 5]))



# security bug

- A SQL Injection is a security vulnerability that allows attackers to interfere with the queries an application makes to its database.
- Occurs when: User input is improperly sanitized, allowing malicious code to be included in SQL statements.
- Can lead to unauthorized data access, data modification, database corruption, or even the execution of administrative operations on the database.

import sqlite3

def get_user_data(user_id):
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()
    return result

# Deployment

Deployment Automation and Scripts

Script Generation 
Bash Prompt:
  "Generate a Bash script that deploys a Node.js application to an Ubuntu server, installs necessary dependencies, and sets up PM2 to manage the application process."
 
PowerShell Prompt:  
  "Write a PowerShell script to deploy a .NET Core web application to a Windows Server, configure IIS, and set up firewall rules for HTTP and HTTPS."

CI/CD Pipeline Configuration

GitHub Actions Prompt 
  "Write a GitHub Actions YAML file that builds a Docker image from the repository, pushes it to Docker Hub, and then deploys it to a Kubernetes cluster."

Containerization**

Dockerfile Configuration Prompt
  "Generate a Dockerfile for a Python Django application that installs dependencies, copies application files, and runs `python manage.py runserver`."

Kubernetes Manifest Prompt
  "Write a Kubernetes deployment and service manifest to deploy a MySQL database with persistent storage in a Kubernetes cluster."