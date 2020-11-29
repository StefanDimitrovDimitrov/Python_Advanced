from project.task import Task


class Section:

    def __init__(self, name):
        self.name = name

        self.task = []

    def add_task(self, new_task: Task):
        task_name_list = [t for t in self.task if new_task == t.name]
        if new_task in task_name_list:
            return f"Task is already in the section {self.name}"

        self.task.append(new_task)
        return f"Task {new_task} is added to the section"

    def complete_task(self, task_name: str):
        return "Completed task {task_name}"
        # return f"Could not find task with the name {task_name}"

    def clean_section(self):
        return f"Cleared {amount of removed tasks} tasks."

    def view_section(self):
        pass

