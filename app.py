from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated file storage (in-memory list)
storage = []

@app.route('/')
def index():
    return render_template('index.html', files=storage)

@app.route('/upload', methods=['POST'])
def upload():
    filename = request.form.get('filename')
    if filename and filename not in storage:
        storage.append(filename)
    return redirect(url_for('index'))

@app.route('/update/<old_filename>', methods=['POST'])
def update(old_filename):
    new_filename = request.form.get('new_filename')
    if old_filename in storage and new_filename:
        storage[storage.index(old_filename)] = new_filename
    return redirect(url_for('index'))

@app.route('/delete/<filename>', methods=['POST'])
def delete(filename):
    if filename in storage:
        storage.remove(filename)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

