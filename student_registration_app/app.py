from flask import Flask, render_template, request, redirect, Response, jsonify
import psycopg2
from datetime import datetime

connection = psycopg2.connect(
    host="0.0.0.0",
    database="db_name",
    user="db_user",
    password="baku2019"
 )

app = Flask("studentApp")


@app.route("/", methods=["GET", "POST"])
def main_index():

    if request.method == "GET":

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM students;")

        data = cursor.fetchall()

        context = {}

        context["static"] = "static"

        context["student_list"] = data

        return render_template("index.html", **context)
    else:

        cursor = connection.cursor()

        name, surname, email, birthday, point = request.form.get("name"), request.form.get("surname"), request.form.get("email"), request.form.get("birthday"), request.form.get("point")
        cursor.execute(f"INSERT INTO students (name, surname, email, birthday, point) VALUES ('{name}','{surname}','{email}','{birthday}','{point}');")

        connection.commit()

        return redirect("/")



@app.route("/students/<id>/")


def get_student(id):
    print(id)
    cursor = connection.cursor()
    try:

        cursor.execute(f"SELECT * FROM students WHERE id={id};")
        obj = cursor.fetchone()
        print(obj)
        return jsonify({
            "name": obj[1],
            "surname": obj[2],
            "email": obj[3],
            "birthday": obj[4].strftime("%m/%d/%y"),
            "point": obj[5]
        })
    except:
        return jsonify({
            "status": f"Not found {id}"
        })

app.run(debug=True)
# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return "Hello, World!"

# from flask import Flask
# import psycopg2
# import datetime

# connection = psycopg2.connect(
#    host="0.0.0.0",
#    database="db_name",
#    user="db_user",
#    password="baku2019"
# )


# cursor = connection.cursor()

# # file = open("data.sql", "r")

# # cursor.execute(file.read())

# connection.commit()


# print("Cedvel ugurla yaradildi")

