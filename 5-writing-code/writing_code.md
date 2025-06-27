# Writing Code

# New Way
- https://x.com/aaditsh/status/1917143080207335843

# Custom Instructions
- fine tune responses for prompts
- guarantee code aligns with your build tools, formatting style, and workflows.
- no more copy-pasting context in every prompt.
- enforces shared conventions across all contributors 

- .GitHub folder
- copilot-instructions.md
- This is added to your prompts
- Check references

- Best Practices
- Keep instructions short and specific. One guideline per line .
- Focus on what matters: coding conventions, tech stacks, commit style, issue trackers.
- Avoid vague requests.

# Next Edit Suggestions (NES)
- It's about editing existing code
- Configure this at bottom right copilot icon
- Used default LLM

nextedit.py 

# IP
- Code referencing or matching
- Will detect if AI-code generated matches public repos
- Can detect issues with intellectual property rights
- Less than 1% of the results

## Learning
- Prompt: For someone who does not know Python, what should I learn first?
- Prompt: What are some beginner-friendly projects I can try to improve my skills in React?
- Prompt: Can you suggest resources for learning advanced SQL queries?
- Prompt: How would you implement a basic "to-do list" app in both Python and JavaScript to highlight their differences?
- Prompt: I know how to use loops in C++. Can you show me how loops work in Python for comparison?
- Prompt: Find 5 useful YouTube videos that show how to learn Rust.

## Study Guides

- Prompt: Create a study guide for JavaScript. Focus on a beginner level.

You can then follow this up with:
- Prompt: Please create a study schedule for me. What topics should I study? What about practice exercises or quizzes? Coding problems? Links to resources?

### LeetCode
- Prompt: Suggest 3 common LeetCode interview questions.

## Comments

- AI good at coming up with them
- Prompt: Add comments that are clear and according to best coding practices.
- But do you need them?
- After all, AI is also good at explaining code

## Starter Project
- Lots of boilerplate with code
- Scaffold the product
- @workspace /new a nodejs project with the express library
- Screenshot of the scaffold/explain it

## Notebook
- Agent mode
- Prompt: Create a Jupyter Notebook.  Import housing.csv and create a table for it

## Refactoring
- Process of restructuring code without changing its external behavior

### Ninja Code
- Example: 
- console.log((function(n, a = 0, b = 1) { while (--n) [a, b] = [b, a + b]; return a; })(10));
- Prompt: Can you explain this code in a step-by-step process? Also, can you write this in a simpler way that is more maintainable?

### Extract Method
- Simplify a long method or function
- Breack it into smaller, more manageable functions
- Prompt: Use the extract method on this file
- See extract-method.py

### Decomposing Conditionals
- A refactoring technique used to simplify complex conditional expressions in your code
- Prompt: refactor
- See decompose-conditionals.py

### Renaming
- Clarity and maintainability
- Prompt: refactor
- renaming.py

### Dead Code
- Refactor for non-used code
- Be careful
- dead-code.py

## Functions
- Think of the single responsibility principle
- Name it clearly
- Keep it short and sweet
- Parameters are key
- Stay consistent

Prompt: Write a Python function named calculate_area that takes two integers as parameters, length and width, and returns the area of a rectangle. Include a docstring explaining the function's purpose and ensure the function handles non-integer inputs by raising a TypeError.

Prompt: I need a JavaScript function called filterAndTransform. It should take an array of objects as input. Each object has properties name (string) and age (number). The function should return a new array containing the names of people who are 18 years or older, converted to uppercase. Include comments explaining the logic.

Prompt: Create a C++ function named efficientSort that sorts an array of integers in ascending order. The function should be optimized for time complexity. Provide comments within the function explaining the choice of sorting algorithm and its time complexity.

Prompt: Can you generate a Java function called safeDivide that takes two double parameters, numerator and denominator, and returns their division? The function should handle division by zero by returning a custom error message. Include Javadoc comments explaining the function and its error handling.

## Data

- Creating data/synthetic data
- Can be a tedious process
- Creating a database schema:

Prompt: Can you help me design a basic database schema for a blog? I need to know what tables I should create and the primary relationships between them.

Prompt: What would be an efficient table structure for managing customer orders in a relational database? What fields and data types should I include?

Prompt: How should I define the relationships between tables in a relational database for an application that deals with event management? Specifically, I need help with understanding foreign keys and join tables.

- Sample data generation: 

Prompt: Create demo data for 5 IDs and email data and save this to a CSV file.

Prompt: Create demo data for 50 products, including product ID, name, price, and category.

Prompt: Create a demo dataset of 150 order records, each with an order ID, customer ID, order date, and total amount.

Prompt: Generate sample data for 100 employees, including employee ID, full name, department, and email address.

Prompt: Create sample data for 80 customer feedback entries, including feedback ID, customer ID, comments.

- SQL:

Prompt: Generate a SQL insert statement to populate the Feedback table with the data.

- Data conversion: 

Prompt: Here's a CSV row: 'John Doe, 35, New York'. Can you convert this into an XML format for me?



## Regular Expressions (Regex)

Example:  
^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$

Prompt: Create a regex pattern to validate standard email addresses. The email should start with alphanumeric characters, followed by optional dots, hyphens, or underscores. Then, there should be an "@" symbol, followed by more alphanumeric characters, a dot, and finally, a domain name that is 2 to 6 characters long.

Prompt: Provide me with a regex pattern to validate URLs. The URL may start with "http" or "https", followed by "://", then a domain name which can include alphanumeric characters and dots. After the domain, there can be an optional path that starts with a "/" and can include alphanumeric characters, slashes, dots, or hyphens. The URL may end with an optional "/".

Prompt: Create a regex pattern to validate dates in the MM/DD/YYYY format. The month should be between 01 and 12, the day should be between 01 and 31, and the year should be either in the 1900s or 2000s.

## GPTs
- Custom ChatGPTs
- Easy to build workflows using the power of the LLM
- LangChain GPT
- Prompt: Write a program that calls the openai LLM

## UI

Prompt: I'm creating a website for my home bakery business named "Sweet Whisk." I want a logo that's warm and inviting. The main products are cakes and cookies, so maybe those could be incorporated into the design. I like pastel colors, especially light pink and mint green. The style should be simple and modern, with a touch of playfulness.

Create UI for calc.png

Write it in JavaScript and html.

Write the code to make it function.

## OCR in ChatGPT

## Claude
Prompt: Please code this UI
Use website.png

Prompt: Write the code for this
Use calc.png

## Database Models

Using a SQL schema or file, developers typically build models or classes that represent the structure of the database.

Usually use Object-Relational Mapping (ORM) tools for this.

Example file for this: artists.sql
Prompt: Create a model for the artist table

## Clerk

Copy prompt feature