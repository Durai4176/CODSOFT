from flask import Flask, render_template_string, request, jsonify
import os  # Import os to get the PORT environment variable

app = Flask(__name__)

# A list to hold tasks (you could also store it in a database)
tasks = []

# HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beautiful To-Do List</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            text-align: center;
            background: linear-gradient(to right, #6a11cb, #2575fc);
            margin: 0;
            padding: 20px;
            color: white;
        }
        .container {
            max-width: 400px;
            background: white;
            padding: 20px;
            margin: auto;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
            color: black;
        }
        h2 {
            color: #6a11cb;
        }
        input {
            width: 80%;
            padding: 10px;
            border: 1px solid #6a11cb;
            border-radius: 5px;
        }
        button {
            padding: 10px 15px;
            border: none;
            background: #2575fc;
            color: white;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
            margin-left: 5px;
        }
        button:hover {
            background: #1a56d0;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            background: #f4f4f4;
            padding: 10px;
            margin: 5px 0;
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .completed {
            text-decoration: line-through;
            color: gray;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>To-Do List</h2>
        <input type="text" id="taskInput" placeholder="Add a new task...">
        <button onclick="addTask()">Add</button>
        <ul id="taskList">
            {% for task in tasks %}
                <li class="{{ 'completed' if task['completed'] else '' }}" id="task-{{ loop.index0 }}">
                    {{ task['text'] }}
                    <button onclick="removeTask({{ loop.index0 }})">❌</button>
                    <button onclick="toggleTask({{ loop.index0 }})">✔️</button>
                </li>
            {% endfor %}
        </ul>
    </div>

    <script>
        function addTask() {
            let taskInput = document.getElementById("taskInput");
            let taskText = taskInput.value.trim();
            if (taskText === "") return;

            fetch("/add", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: `task=${taskText}`
            })
            .then(response => response.json())
            .then(data => updateTaskList(data.tasks));

            taskInput.value = "";
        }

        function removeTask(taskId) {
            fetch(`/remove/${taskId}`, {
                method: "DELETE"
            })
            .then(response => response.json())
            .then(data => updateTaskList(data.tasks));
        }

        function toggleTask(taskId) {
            fetch(`/toggle/${taskId}`, {
                method: "POST"
            })
            .then(response => response.json())
            .then(data => updateTaskList(data.tasks));
        }

        function updateTaskList(tasks) {
            const taskList = document.getElementById("taskList");
            taskList.innerHTML = '';
            tasks.forEach((task, index) => {
                const li = document.createElement("li");
                li.className = task.completed ? 'completed' : '';
                li.innerHTML = `${task.text} <button onclick="removeTask(${index})">❌</button> <button onclick="toggleTask(${index})">✔️</button>`;
                taskList.appendChild(li);
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_text = request.form.get('task')
    if task_text:
        tasks.append({'text': task_text, 'completed': False})
    return jsonify(tasks=tasks)

@app.route('/remove/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return jsonify(tasks=tasks)

@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = not tasks[task_id]['completed']
    return jsonify(tasks=tasks)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Get the port Render provides or default to 5000
    app.run(host="0.0.0.0", port=port, debug=True)