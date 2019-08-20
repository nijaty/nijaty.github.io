from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>Hello World!</h1>'


@app.route("/home", methods=['GET', 'POST'], defaults={'name': 'Default'})
@app.route("/home/<string:name>", methods=['GET', 'POST'])
def home(name):
    return '<h1>Bura {}in home page-dir</h1>'.format(name)


@app.route("/query")
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {}. You are from {}. You are in query page</h1>'.format(name, location)


@app.route("/the_form", methods=['GET', 'POST'])
def the_form():
    if request.method == 'GET':
        return '''<form method='POST' action="/the_form">
                <input type="text" name="name">
                <input type="text" name="location">
                <input type="submit" value="Submit">
                    </form>'''
    else:
        name = request.form['name']
        location = request.form['location']

        return '<h1>Hello {}. You are from {}. You have submitted the form successfully!<h1>'.format(name, location)


# @app.route('/process', methods=['POST'])
# def process():
#     name = request.form['name']
#     location = request.form['location']
#
#     return '<h1>Hello {}. You are from {}. You have submitted the form successfully!<h1>'.format(name, location)


@app.route("/processjson", methods=['POST'])
def processjson():
    data = request.get_json()

    name = data['name']
    location = data['location']

    random_list = data['random_list']

    return jsonify({
        'result': 'Success', 'name': name, 'location': location, 'random_key_in_list': random_list[1]
    })


if __name__ == '__main__':
    app.run(debug=True)
