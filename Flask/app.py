from flask import Flask, request, jsonify,render_template, redirect, url_for

app = Flask('app', template_folder='template')

#main page
@app.route('/')
def hello_world():
    return 'hello, user!'

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method =='GET':
        return "ECHO: GET\n"
    elif request.method == 'POST':
        return 'ECHO: POST\n'
    elif request.method == 'PATCH':
        return 'ECHO: PATCH\n'
    elif request.method == 'PUT':
        return 'ECHO: PUT\n'
    elif request.method == 'DELETE':
        return 'ECHO: DELETE\n'



@app.route('/country', methods = ['GET'])
def countryall():
    return jsonify({'country':'GEO'})

@app.route('/getHTML')
def index():
    return render_template('hello.html')

@app.route('/login', methods = ['POST','GET'])
def login_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['psw']
        if username == 'nika' and password == 'nika1234':
            return 'succsess'
        else:
            return redirect(url_for('hello_world'))
    return render_template('hello.html')

@app.route('/home/')
def home_page():
    return '<h1>HOME</h1>'
app.run(host='localhost', port=8080)