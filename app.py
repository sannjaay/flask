from flask import *

app = Flask(__name__)


@app.route('/')
def funct():
    return render_template('index.html')
@app.route('/admin')
def funct1():
    return "this is admin"
@app.route('/student')
def funct2():
    return 'this is student'
@app.route('/staff')
def funct3():
    return 'this is staff'

@app.route('/user/<name>')
def user(name):
    if(name == 'admin'):
        return redirect(url_for('funct1'))
    if(name == 'student'):
        return redirect(url_for('funct2'))
    if(name == 'staff'):
        return redirect(url_for('funct3'))
if __name__ == '__main__':
    app.run(debug=True)