import json
import os
from flask import Flask, request
from Constants import UPLOAD_FOLDER, ARCHIVE_FOLDER, RESULT_FOLDER
from Constants import ALLOWED_EXTENSIONS

UPLOAD_ERROR = json.dumps(
    {"error": "Cannot find valid Python source code file."})

app = Flask(__name__)


def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS


def get_no_file_error(app_id):
    return json.dumps(
        {"appId": app_id, "error": "Cannot find a corresponding file."})


def get_pending(app_id):
    return json.dumps({"appId": app_id, "status": "pending"})


@app.route("/submit", methods=["POST"])
def submit():
    file = request.files["file"]
    if not file and not allowed_file(file.filename):
        return UPLOAD_ERROR
    appId = request.form["appId"]
    file.save(os.path.join(UPLOAD_FOLDER, appId + ".py"))
    return json.dumps({"appId": appId})


@app.route("/app/<app_id>")
def get_app_status(app_id):
    file_path = os.path.join(UPLOAD_FOLDER, app_id + ".py")
    if os.path.isfile(file_path):
        return get_pending(app_id)
    res_path = os.path.join(RESULT_FOLDER, app_id + ".res")
    if os.path.isfile(res_path):
        return open(res_path).read()
    return get_no_file_error(app_id)


@app.route("/apps", methods=["POST"])
def get_apps_status():
    r = []
    for app_id in request.form["app_ids"].split(','):
        r.append(json.loads(get_app_status(app_id.strip())))
    return json.dumps(r)


@app.route("/status/<app_id>/<count>")
def get_status(app_id, count):
    r = []
    file_id, count = int(app_id), int(count)
    while file_id > 0 and count > 0:
        app_id = "%d" % file_id
        r.append(json.loads(get_app_status(app_id)))
        file_id = file_id - 1
        count = count - 1
    return json.dumps(r)


if __name__ == "__main__":
    app.run()
