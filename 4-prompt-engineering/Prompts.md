# 4 - Prompt Engineering

# Be Polite
* Please, can you ?
* The underlying datasets may pickup on more accurate content

# System Message

* Persona or role
* A sentence or two
* Example:  You are an experienced Python developer

# Instructions for the LLM

* Clear
* Focus on a task
* Multiple tasks can confuse or redirect the LLM

Examples:  

Create a Python function that takes a list of integers and returns the sum of all even numbers in the list

Create a function that merges two dictionaries, with values from the second dictionary overwriting those from the first if there are duplicate keys

Write a function that reads a JSON file, modifies a specific field, and writes the updated data back to the file

Implement a function that safely converts a string to an integer, returning None if the conversion fails

Implement a function that safely converts a string to an integer, returning None if the conversion fails

* Order of the words matter with the prompt
* Based on the transformer model -- which predicts the next word based on the prior information
* Example:  the output will be at the end of the prompt

# Text Classification

* Give the LLM text and it will analyze it
* Use case:  sentiment analysis, such as with user feedback
* ChatGPT is a good option
* Prompt:  Can you analyze these customer reviews and tell me if the sentiment is generally positive, negative or neutral?

# Translation

* localization
* Example:  Translate the following UI text into French:  Save, Exit, File, Edit, Help.

# Code Conversion

* Convert code between different languages
* Do the same for frameworks:  React to Vue, Express.js to Flask API
* Can struggle with complex code or older code bases (COBOL)
* Have LLM explain the code

# Delimiters

* Separate conent with ###, \"\"\", and so on
* Focus the LLM on what you want to work on
* Examples:

Explain this code:

###
_ = lambda f: lambda *a, **k: f(*a, **k)
__ = [chr(ord('a') + i) for i in range(26)]
___ = __[17] + __[4] + __[2] + __[10]  # "reck"
____ = lambda x: ''.join(map(lambda c: chr(((ord(c) - 97 + 13) % 26) + 97), x))  # rot13
_____ = {____(k): v for k, v in {___: 42, __[0]*3: 7}.items()}  # {'erpx': 42, 'nnn': 7}

print(_____['erpx'] * _____['nnn'])  # 42 * 7 = 294

###

Stripe API


Use this prompt:  Here's the Stripe API documentation on confirming a payment intent #fetch https://docs.stripe.com/api. Could you walk me through the steps and show an example in Python?

In the Spotify Web API, what are the required parameters for searching for a track, and can you show me a Python code example of how to use it?

Is this based on the most up-to-date version of the API documentation?


# Output Formating

Examples (try in GitHub Copilot and ChatGPT): 

Create a Python function that takes a list of user objects (each object containing a user's ID and name) and returns a JSON object that maps user IDs to names. Format the output as JSON.

Write a Python script using BeautifulSoup to scrape the top 10 headlines from a news website. Generate an HTML report with these headlines, including links to the full articles. Style the HTML with inline CSS to make it visually appealing.

Develop a Python function that analyzes a pandas DataFrame of sales data. Create a bar chart using Matplotlib showing monthly sales totals. Save the chart as a PNG file and return a dictionary with summary statistics (total sales, average monthly sales, best and worst months).

Write a Python script that interacts with a REST API (e.g., OpenWeatherMap) to fetch weather data for multiple cities. Store the API key and city list in a YAML configuration file. Output the weather information as a formatted text report.

Create a Python script using Pillow and reportlab that processes a folder of images. Generate a PDF report with thumbnails of each image, including file names and basic image statistics (dimensions, file size). Add a title page and page numbers to the PDF.

# Output Length

Examples:

Be precise

Write a detailed explanation

Do not provide an exaplanation

Express this in one paragraph

Express this in 300 words

# Technical Terms and Acronyms

* Define them
* Prompt:  I'm having DB connection issues. How to fix them?
* What does DB refer to?  What type of databases:
* Prompt:  I am encourning a connection timeout issue while trying to connect to my PostgreSQL database using JDBC. How can I resolve this?

# Zero-Shot and Few-Shot Learning

* Provide examples in the prompt
* Form of prompt learning

Example:

Based on the following examples of normalizing a list of numbers to a range of [0, 1]:
1. Input: [2, 4, 6, 8] Output: [0, 0.3333, 0.6667, 1]
2. Input: [5, 10, 15] Output: [0, 0.5, 1]
3. Input: [1, 3, 2] Output: [0, 1, 0.5]
Generate a function in Python that takes a list of numbers as input and returns a list of normalized numbers.

Example:

Create a JavaScript function to validate email addresses. The function should return true for valid emails and false for invalid ones. Here are some test cases to consider:

test@example.com (valid)

invalid.email@com (invalid)

user@subdomain.example.co.uk (valid)

@missingusername.com (invalid)


Ensure the function handles these cases correctly.

# Leading Prompts

* Avoid assumptions
* Try to be neutral
* Leading prompt:  Isn't it true that migrating to a microservices architecture will always improve system scalability?
* Better:  What are the advantages and challenges of migrating to a microservices architecture in terms of system scalability?

# Examples and analogies

* A way to learn new concepts
* Prompt:  Explain inheritance that is used in object-oriented programming by using an analogy.

# Context

- Of course, LLMs can't read your mind
- This is why it's important to provide context
- GitHub provides this via the IDE
- File extension (if py, will know to write code I Python)
- Will also use the following for the contex:
    - Name of the active file and its code
    - Content before and after the cursor
    - Comments
    - Other open files
- This context is included with your prompt
- GitHub Copilot will engage in inference/connecting the dots of the codebase
    - Considers your coding style and patterns within
    - Understand and use imported libraries and custom functions defined in your project
    - Respects your IDE settings, like indentation style
    - Use the folder structure and file names to better understand the project context
- Reduces the need for writing lengthy prompts

- Example of using GitHub Copilot for context for SQL
- Use sample.sql file
- Prompt:  Find All Employees in a the sales department
- Pronpt:  Turn this into a stored procedure