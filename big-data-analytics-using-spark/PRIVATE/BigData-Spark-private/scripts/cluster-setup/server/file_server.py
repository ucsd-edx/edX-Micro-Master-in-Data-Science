import os
from flask import Flask, abort, send_file
from Constants import OUTPUT_FOLDER

app = Flask(__name__)


@app.route("/output/<dirname>/<filename>")
def get_file(dirname, filename):
    path = os.path.join(os.path.join(OUTPUT_FOLDER, dirname), filename)
    if os.path.isfile(path):
        return send_file(path, as_attachment=True)
    abort(404)


if __name__ == "__main__":
    app.run()
