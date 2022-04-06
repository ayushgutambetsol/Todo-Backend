import logging

from flask import request, jsonify
from flask_restful import Resource

from app.todoApp.constants.response_constants import ResponseConstants
from app.todoApp.model.todo_list_model import Todo
from app.todoApp.utils.serialize_data import TodoListSerializer

logger = logging.getLogger(__name__)


class TodoListView(Resource):
    """
    TODO : Suggestions to this class
    """

    def get(self):
        try:
            serialize_instance = TodoListSerializer(Todo.get_all(), model_type="todo", many=True)
            logger.info(f"serialize_instance called here")
            tags = Todo.get_all_tags()
            data = {
                "todo_list": serialize_instance.data(),
                "tags": [tag[0] for tag in tags]

            }
            return jsonify(data), 200
        except KeyError as e:
            logger.error(f"Error: {e}")
            return {"message": ResponseConstants.INVALID_REQUEST}, 400
        except ValueError as e:
            logger.error(f"Error: {e}")
            return {"message": ResponseConstants.TODO_WITH_ID_NOT_FOUND}, 400
        except Exception as e:
            logger.error(f"Error: {e}")
            return {"message": ResponseConstants.SOMETHING_WENT_WRONG}, 500

    def post(self):
        try:
            title = request.get_json(force=True)['title']
            if title == "":
                raise ValueError(ResponseConstants.TITLE_REQUIRED)
            Todo.create(title)
            logger.info("New task created")
            return {"message": ResponseConstants.SUCCESS_MESSAGE_CREATE_TODO}, 201
        except KeyError:
            return {"message": ResponseConstants.INVALID_REQUEST}, 400
        except ValueError as e:
            logger.error(f"Error: {e}")
            return {"message": ResponseConstants.INVALID_REQUEST}, 500
        except Exception as e:
            logger.error(f"Error: {e}")
            return {"message": ResponseConstants.SOMETHING_WENT_WRONG}, 500

    def put(self, todo_id):
        try:
            data = request.get_json(force=True)
            data['id'] = todo_id
            serializer = TodoListSerializer(data, model_type="dict")
            if serializer.is_valid():
                parsed_data = serializer.data()
                created_instance = Todo.update(parsed_data['id'], parsed_data['title'], parsed_data['completed'])
                if created_instance:
                    result = {
                        "message": ResponseConstants.SUCCESS_MESSAGE_UPDATE_TODO,
                        "task": parsed_data
                    }
                    return result, 200
            else:
                raise ValueError("Invalid data")
        except KeyError as e:
            logger.error(f"Error: {e}")
            return {"message": ResponseConstants.INVALID_REQUEST}, 400
        except ValueError as e:
            logger.error(f"Error: {e}")
            return {"message": ResponseConstants.INVALID_REQUEST}, 400
        except Exception as e:
            logger.error(f"Error: {e}")
            return {"message": ResponseConstants.SOMETHING_WENT_WRONG}, 500

    def patch(self, todo_id):
        """
        TODO : Implement PATCH method
        :return:
        """
        try:
            Todo.update_complete(todo_id)
            return {"message": ResponseConstants.SUCCESS_PATCH_TODO}, 200
        except KeyError as e:
            logger.error(f"Error: {e}")
            return {"message": ResponseConstants.INVALID_REQUEST}, 400
        except ValueError as e:
            logger.error(f"Error: {e}")
            return {"message": ResponseConstants.INVALID_REQUEST}, 400
        except Exception as e:
            logger.error(f"Error: {e}")
            return {"message": ResponseConstants.SOMETHING_WENT_WRONG}, 500

    def delete(self, todo_id):
        try:
            Todo.delete(todo_id)
            return {"message": ResponseConstants.SUCCESS_MESSAGE_DELETE_TODO}, 200
        except KeyError as e:
            logger.error(f"Error: {e}")
            return {"message": ResponseConstants.INVALID_REQUEST}, 400
        except ValueError as e:
            logger.error(f"Error: {e}")
            return {"message": ResponseConstants.INVALID_REQUEST}, 400
        except Exception as e:
            logger.error(f"Error: {e}")
            return {"message": ResponseConstants.SOMETHING_WENT_WRONG}, 500
