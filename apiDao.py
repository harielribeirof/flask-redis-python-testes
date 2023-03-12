class TodoDAO(object):
    def __init__(self, api):
        self.todos = []
        self.api = api

    def get(self, key):
        for todo in self.todos:
            if todo['key'] == key:
                return todo
        self.api.abort(404, "Key {} doesn't exist".format(key))

    def create(self, data):
        todo = data
        self.todos.append(todo)
        return todo

    def update(self, key, data):
        todo = self.get(key)
        todo.update(data)
        return todo

    def delete(self, key):
        todo = self.get(key)
        self.todos.remove(todo)