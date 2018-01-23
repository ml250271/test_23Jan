from flask import Flask
from models import Comment

app = Flask(__name__)


@app.route("/")
def index():

    page = """
    <!DOCTYPE html>
    <html>

    <head>

    </head>

    <body>
        <h1>"Welcome!"</h1>
    </body>

    </html>
    """

    return page


@app.route("/api/v1.0/comments")
def api_comments():
    page2 = """
    <!DOCTYPE html>
    <html>

    <head>

    </head>

    <body>
    <h1>Table should be here</h1>
    </body>
    <p id=table>
    { </p>
    </html>
    """
    return page2
#     return page.format(table)



