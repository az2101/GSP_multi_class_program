
class TodoList:
    def __init__(self):
        self.list_todo = []

    def add(self, todo):
        self.list_todo.append(todo)
        
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_todos = []
        for todo in self.list_todo:
            if todo.complete == False:
                incomplete_todos.append(todo)
        return incomplete_todos

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_todos = []
        for todo in self.list_todo:
            if todo.complete == True:
                complete_todos.append(todo)
        return complete_todos

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self.list_todo:
            if todo.complete == False:
                todo.mark_complete()