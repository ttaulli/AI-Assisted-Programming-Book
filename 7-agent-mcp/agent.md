Agent Mode

End of prompt engineering?
- Prompt is more about goals, not detailed descriptions

Creating an app

Prompt:  I want to create a web application that provides weather information for a given city.  I want to use a free API.  Also, what do you suggest for the tech stack?

In the terminal:  npx create-next-app@latest . 

npm run dev

Prompt: Let's create a NextJS app for this.  Use the OpenWeatherMap API.  I have setup NextJS app in the directory 7-agent-mcp/weather-app.  Create a page that allows users to enter a city name and displays the current weather information for that city.

Selection:
- Nextjs
- OpenWeatherMap API
- https://openweathermap.org/api
- Register and get the API
- API Key/Weather - 5713368301d35528e4ecf77aa1aba82d


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

# Unit Tests

- GitHub Copilot can create test cases
- Can't do everything
- But provide a good start
- Different types of unit testing frameworks
- In your prompt, specify the framework
- Chat tends to have more tests than using in-line chat
- /tests and run it 
- tests.py

- GitHub Copilot Spark

https://spark.githubnext.com/