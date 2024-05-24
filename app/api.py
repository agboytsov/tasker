import json

from flasgger import swag_from
from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError

from handlers import get_tasks, get_task, update_task, create_task, delete_task

api = Blueprint('api', __name__, template_folder="templates/app1")


@api.route("/tasks", methods=["GET", "POST"])
@swag_from('api_schemas/tasks_list/get.yml', methods=['GET'])
@swag_from('api_schemas/tasks_list/post.yml', methods=['POST'])
def tasks_list():
    """Endpoint для создания статей и получения списка статей.
    """
    if request.method == "GET":
        tasks = get_tasks()
        try:
            if tasks:
                return tasks, 200
            return json.dumps({"error": 'No tasks'}), 404
        except (TypeError, IntegrityError):
            return json.dumps({"error": 'Wrong request'}), 400
    elif request.method == "POST":
        new_task = create_task(request.json["title"], request.json["description"])
        return new_task
    else:
        return "Method not supported", 405


@api.route("/tasks/<int:task_id>", methods=["GET", "PUT", "DELETE"])
@swag_from('api_schemas/one_task/get.yml', methods=['GET'])
@swag_from('api_schemas/one_task/put.yml', methods=['PUT'])
@swag_from('api_schemas/one_task/delete.yml', methods=['DELETE'])
def one_task(task_id):

    match request.method:
        case "GET":
            return get_task(task_id)
        case "PUT":
            return update_task(task_id, request.json['title'], request.json['description'])
        case "DELETE":
            return delete_task(task_id)
        case _:
            return {'error': 'Method not allowed'}, 400
