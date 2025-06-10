# Task Tracker CLI

## Project URL:
https://roadmap.sh/projects/task-tracker

A simple command-line tool to manage tasks (add, delete, update, mark status, list) using a `tasks.json` file for storage.

## Features
- Add new tasks with description
- Update existing tasks
- Delete tasks by ID
- Mark tasks as `done` or `in-progress`
- List tasks filtered by status

## Usage

```bash
python task_cli.py add "Your task description"
python task_cli.py list
python task_cli.py update <ID> "New description"
python task_cli.py delete <ID>
python task_cli.py mark-done <ID>
python task_cli.py mark-in-progress <ID>
