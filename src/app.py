from flask import Flask, render_template
import os
import database as bd

templateDir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
templateDir = os.path.join(templateDir, 'src', 'templates')

app = Flask(__name__, template_folder = templateDir)

#Routers
@app.route('/')
def gome():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=4000)