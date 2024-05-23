from flask import Blueprint, request, render_template
import requests

from handlers import get_tasks, get_task, update_task, create_task, delete_task

front = Blueprint('front', __name__, template_folder="templates")

SITE = "http://127.0.0.1:5000"

@front.route("/")
def start_page():
    tasks = requests.get(f"{SITE}/api/tasks")
    if tasks.ok:
        return render_template("index.html", tasks=tasks.json())
    return render_template("index_no_tasks.html")