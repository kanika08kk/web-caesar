from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True
form="""<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form method="post" action="result"><b><font size=5>Rotate by:</font></b> 
      <input type=\"text\" name="rot" value=\"0\">
    <br><textarea type=\"textarea\" name="text">{0}</textarea>
    <input type=submit value=\"Submit Query\">
    </body>
</html>"""

@app.route("/")
def index():
    return form.format("")
@app.route("/result", methods=['POST'])
def encrypt():
    rot1=int(request.form['rot'])
    strToBeEncrupted=request.form['text']
    encrypted=rotate_string(strToBeEncrupted,rot1)
    return form.format(encrypted)
app.run()
