Agent Mode

Use Claude 3.7 Sonnett

Recommendations:

Prompts:

What are libraries and frameworks to create web applications?

What are free APIs that can be used to retrieve information about the weather? 

Selection:
- Nextjs
- OpenWeatherMap API
- https://openweathermap.org/api
- Register and get the API

Process:
- Create a new folder for the project
- Then upload it to VS Code

Prompts

Create a new Nextjs project in the current directory. Do not initialize a git repository.


How do I run this?

Replace the homepage of this project with a search input that for city that provides weather details. use the @fetch https://openweathermap.org/api

MCP Demo

- Select Agent Mode from the dropdown menu.​
- You can find MCP servers here: https://github.com/modelcontextprotocol/servers
- Supabase provides a fully managed PostgreSQL database as part of each project you create. 
- Create an account: https://supabase.com/
- Click Start project
- Register an account
- Enter the name of the project
- Enter password
- Select Table Editor
- Select Create a new table
- Name: Todos
- Click New column
- For name, enter: task
- Click save
- Click Insert to add new rows of data

- To to the terminal 
- npm install -g @supabase/mcp-server-supabase
- This command installs the Supabase MCP server globally on your system.
- Obtain Your Supabase Personal Access Token
- Click on your profile avatar and select Account preferences.
- Select Access Tokens
- Select Generate new token
- Enter name for it
- Copy your token

- Instructions:  https://supabase.com/docs/guides/getting-started/mcp
- In VS Code, create a .vscode directory in your project root if it doesn't already exist
- Create a .vscode/mcp.json file if it doesn't already exist
- Add the following configuration:


{
  "inputs": [
    {
      "type": "promptString",
      "id": "supabase-access-token",
      "description": "Supabase personal access token",
      "password": true
    }
  ],
  "servers": {
    "supabase": {
      "command": "npx",
      "args": ["-y", "@supabase/mcp-server-supabase@latest"],
      "env": {
        "SUPABASE_ACCESS_TOKEN": "${input:supabase-access-token}"
      }
    }
  }
}

- Save the file
- You will see Start inside it
- Click it to run the mcp server
- Enter your access toke for supabase
- Activate Chat
- In the tools icon, you will see you have 26
- Click it
- You can select/deselect the tools you want to use
- Prompt: What is the schema of the todos table?
- Prompt: Add a completed field.

- Agent and unit testing
