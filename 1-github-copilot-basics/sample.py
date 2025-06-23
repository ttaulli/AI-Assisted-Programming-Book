
# Create code by using comments
# Comment/Prompt:  Create a Python function that converts fahrenheit to celsius
# Tab to accept; esc to cancel

# create a function that converts fahrenheit to celsius
# Note:  can also use the comment icon on the top right of the screen

# create a function that converts fahrenheit to celsius





# Start with def convert
# def multiply(a, b):



# Create code by using Chat
# Click Copilot icon on top right of the screen
# Select Open Chat
# Prompt:  Write a program that converts fahrenheit to celsius
# Note:  in the chat input box, you can see chat history with up arrow.

# In the chat, you can select the LLL (large language model)
# Can bring in LLMs via API - select Manage Models
# Will see the files that are in the context
# Which model?
https://x.com/windsurf_ai/status/1917656073177292809?s=43&t=cS1w1VZsy-iY3t91NeeUSw
# Add context like files
# Icon for audio
# Ask or activate Edits or Agent
# @ sign is used to call a service/function
# @terminal - Help with the terminal
# Insert it into the terminal
# Prompt:  @terminal What is the command to list the files in a directory?

# Help with VSCode
# @vscode How do I open the Command Palette?
# @vscode How do I change the theme?
# @vscode How do I install extensions?

# Working with context
# When prompting, what are you refering to?
# #fetch to access an external website, such as API
# if GitHub Copilot does not have the relevant context, it often will 
# respond with a more generic answer
# show how this works with sort.py

# @workspace 
# Refers to the Visual Studio Code workspace
# Can't look at everything because of the limits of the LLM's context window 
# Code bases can be massive
# so will evaluate:
# 1. file system structure
# 2. relevant code snippets (class, methods, comments)
# does not have access to git history
# Cannot handle prompts like:
# "Fix all the bugs in this project" (too vague and expansive)
# "How many JS files does this project have?" (LLMs not good at counting; besides can use VS Code for this)

# In the Chat, you can select the file icon
# Can indicate what part of the program you want to focus on

# Example:  my-python-project
# Prompt:  @workspace what is todo-app?
# Fuzzy search
# Prompt:  @workspace in the todo app, what code adds a task?
# Click the references

# /explain provide details about the code
# In-line Chat
# ctrl + i for Windows
# cmd + i for Mac

def add(a, b):
    return a + b

# sparkle icon; highlight the code above
# Prompt:  Add error handling

# /clear
# Clear the Chat
# Can be more than about making things more tidy
# Can be helpful if you are going to focus on another topic
# can also create a new chat session by clicking +

# In the chat, you can select Copilot Edits
# Top middle icon
# Similar to the Composer feature in Cursor
# If you are working with multiple files
# Select files:  
# for todo:  main.py, models.py, views.py
# Prompt:  Add authentication to this

# Terminal
# Activate it and use in-line chat
# Prompt:  How do I create a project for NextJS?
# Or select something in the terminal and right click + Copilot + Explain

# GitHub CLI
# Installation:  https://cli.github.com/
# In terminal for setup
# sudo gh auth login (will go through the process for authentication)
# sudo gh extension install github/gh-copilot
# sudo gh copilot explain "ps - aux"
# sudo gh copilot suggest "create a new directory"
# Note: can create aliases to shorten the commands

# Copilot extensions
# Add context, say from third-party apps
# Two types:
# Go to those that are only for GitHub Copilot
# https://github.com/marketplace?type=apps&copilot_app=true
# Refer to them with @
# The other way is to add it from the chat
# These extensions can be used with or without Copilot, but have Copilot
# capabilities
# Click @ and then select Install Chat Extensions


# Copilot allows you to build your own extenions.

# Click Settings (bottom left icon) and search for Copilot

# Use GitHub Copilot in GitHub.com
# Access it by clicking the icon on the top right of the screen
# Can work with repositories or ask generic questions
# Click into the code
# Click file icon and get repo
# Can use extensions for Chat
# Activate them but may be fee
# In the Chat, you can select the ...
# Different ways to intereact with Chat, such as Immersive mode

# short hand for GitHub Copilot
# / @

# You can have the AI generate pull request descriptions
# Select version control icon on the left
# Click sparkle icon

# Public code matching/referencing
# Prompt:  what is recursion? 