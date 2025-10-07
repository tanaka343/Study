from flask import Flask,render_template
from mysql_connect import cursor

app= Flask(__name__)

# @app.route('/<id>')
# def top(id):
#     return f"hello{id}"

# items=[
#     {'id':'1','name':'tanaka','age':'12'}
# ]
items = cursor.execute('SELECT * FROM sapu_db.users')

@app.route('/')
def top():
    return render_template('index.html',values=items)


if __name__ == '__main__':
    app.run()