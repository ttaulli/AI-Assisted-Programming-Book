# /help for general help or you can have a prompt

# Create code by using comments
# Comment/Prompt:  Create a Python function that converts fahrenheit to celsius
# Tab to accept; esc to cancel



# Start with def convert




# Create code by using Chat
# Sidebar chat - Pull down at top of VS Code
# Prompt:  Write a program that converts fahrenheit to celsius
# Note:  in the chat input box, you can see chat history with up arrow.

# In the chat, you can select the LLL (large language model)
# gpt-4o (default), o1-preview, 01-mini
# Adding Anthropic’s Claude 3.5 Sonnet, Google’s Gemini 1.5 Pro
# Will see the files that are in the context


# Icon for audio
# @ sign is used to call an agent
# Help with the terminal
# Insert it into the terminal
# Prompt:  @terminal What is the command to list the files in a directory?

# Help with VSCode
# @vscode How do I open the Command Palette?
# @vscode How do I change the theme?
# @vscode How do I install extensions?

# Working with context
# When prompting, what are you refering to?
# #editor is the context for the active file
# #file the file where your cursor is
# Do not even need to specify "file" because it is the default
# Just specify the name of the file
# #selection is what you have highlighted in the active file
# if GitHub Copilot does not have the relevant context, it often will 
# respond with a more generic answer

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    sorted_numbers = bubble_sort(numbers)
    print("Sorted numbers:", sorted_numbers)


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
# Prompt:  What code adds a task?
# Click the references

# /explain provide details about the code
# In-line Chat
# ctrl + i for Windows
# cmd + i for Mac

def add(a, b):
    return a + b

# sparkle icon
# /doc to add comments and documentation
# Prompt:  Add error handling


# /clear
# Clear the Chat
# Can be more than about making things more tidy
# Can be helpful if you are going to focus on another topic

# Can create a Notebook
# @workspace /newNotebook Python to load a CSV dataset

# @github
# can search the web for repos 

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

# Use GitHub Copilot in GitHub.com
# Access it by clicking the icon on the top right of the screen
# Can work with repositories or ask generic questions
# Click into the code
# Click file icon and get repo
# Can use extensions for Chat
# Activate them but may be fee
# In the Chat, you can select the ...
# Different ways to intereact with Chat, such as Immersive mode

# LLM cut-off for training date
# Prompt:  As of your last training date, what was the current version of Go?









