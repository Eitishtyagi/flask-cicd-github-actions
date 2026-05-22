from flask import Flask, render_template, request, redirect, url_for
import socket

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    host = socket.gethostname()
    return render_template('index.html', todos=todos, host=host)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        todos.append({'id': len(todos)+1, 'task': task, 'done': False})
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return redirect(url_for('index'))

@app.route('/done/<int:todo_id>')
def done(todo_id):
    for t in todos:
        if t['id'] == todo_id:
            t['done'] = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
