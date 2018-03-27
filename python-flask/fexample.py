from flask import Flask, render_template

app = Flask(__name__)

@app.route('/flask/')
def hello_flask():
	return 'Hello Flask'

@app.route('/python/')
def hello_python():
	return 'Hello Python'

@app.route('/welcome')
def renderwelcome():
    return render_template('welcome.html')


@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello1.html', name = user)


@app.route('/myindex')
def abcd():
   return '<html><body><h1>Hello World HTML Code Returned </h1></body></html>'


@app.route('/')
def fmain():
	return 'Welcome !'


if __name__ == '__main__':
    app.run(debug=True)