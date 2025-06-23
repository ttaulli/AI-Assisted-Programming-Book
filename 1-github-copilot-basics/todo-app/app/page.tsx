import { useState } from "react";

export default function Home() {
  const [tasks, setTasks] = useState<string[]>([]);
  const [input, setInput] = useState("");

  const addTask = (e: React.FormEvent) => {
    e.preventDefault();
    if (input.trim()) {
      setTasks([input.trim(), ...tasks]);
      setInput("");
    }
  };

  const removeTask = (idx: number) => {
    setTasks(tasks.filter((_, i) => i !== idx));
  };

  return (
    <div className="flex flex-col items-center min-h-screen p-8 bg-background text-foreground">
      <h1 className="text-3xl font-bold mb-8">To-Do App</h1>
      <form onSubmit={addTask} className="flex gap-2 mb-6 w-full max-w-md">
        <input
          className="flex-1 px-3 py-2 border rounded focus:outline-none focus:ring"
          type="text"
          placeholder="Add a new task..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button
          type="submit"
          className="px-4 py-2 bg-foreground text-background rounded hover:bg-gray-800 dark:hover:bg-gray-200 dark:hover:text-black transition"
        >
          Add
        </button>
      </form>
      <ul className="w-full max-w-md space-y-2">
        {tasks.length === 0 && (
          <li className="text-center text-gray-400">
            No tasks yet. Add one above!
          </li>
        )}
        {tasks.map((task, idx) => (
          <li
            key={idx}
            className="flex justify-between items-center bg-white dark:bg-black/30 rounded px-4 py-2 shadow"
          >
            <span>{task}</span>
            <button
              onClick={() => removeTask(idx)}
              className="text-red-500 hover:text-red-700 font-bold"
              aria-label="Delete task"
            >
              ×
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
