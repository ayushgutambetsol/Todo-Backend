from app.todoApp.model.todo_list_model import Todo


class TodoListSerializer:

    """
    TODO : Suggest enhancements to this class
    """

    fields = ['id','title', 'complete', 'date_modified', 'tag']

    def __init__(self, todo_list, model_type, many=False):
        self.todo_list = todo_list
        self.model_type = model_type
        self.many = many

    def is_valid(self):
        if self.todo_list:
            if self.model_type == "todo":
                return True
            if self.todo_list.keys() == Todo.__dict__.keys():
                return True
        else:
            return False

    def serialize_many(self):
        result = []
        for i in self.todo_list:
            if self.model_type == 'todo':
                i = i.__dict__
            temp_dict = {}
            for fields in self.fields:
                if fields not in temp_dict.keys():
                    temp_dict[fields] = i[fields]
                    if fields == 'complete':
                        temp_dict[fields] = True if i['complete'] else False
            result.append(temp_dict)
        return result

    def serialize_one(self):
        if self.model_type == 'todo':
            result = self.todo_list.__dict__
        else:
            if self.todo_list.get('completed', False):
                self.todo_list['completed'] = True if self.todo_list['completed'] else False
            result = self.todo_list
        return result

    def return_data(self):
        if self.many:
            return self.serialize_many()
        else:
            return self.serialize_one()

    def data(self):
        if self.is_valid():
            return self.return_data()
        else:
            return None
