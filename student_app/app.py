from flask import Flask, request, redirect, url_for, render_template


from student import Student

app = Flask(__name__)

students = []


@app.route('/')
def root():
    return redirect(url_for('index'))


@app.route('/students', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        new_student = Student(request.form['first_name'], request.form['last_name'])
        students.append(new_student)
        return redirect(url_for('index'))
    return render_template('index.html', students=students)


@app.route('/students/new')
def new():
    return render_template('new.html')


@app.route('/students/<int:id>')
def show(id):
    for student in students:
        if student.id == id:
            found_student = student
    return render_template('show.html', student=found_student)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
