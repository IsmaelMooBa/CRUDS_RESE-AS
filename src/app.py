from flask import Flask, render_template
import os
import database as db

templateDir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
templateDir = os.path.join(templateDir, 'src', 'templates')

app = Flask(__name__, template_folder = templateDir)

#Routers
@app.route('/')
def home():
    Cursor = db.database.cursor()
    Cursor.execute("SELECT * FROM products")
    myresult = Cursor.fetchall()
    
    insertObject = []
    columName = [column[0] for column in Cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columName, record)))
    Cursor.close()
    return render_template('index.html', data = insertObject)


if __name__ == '__main__':
    app.run(debug=True, port=4000)