from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def student():
	return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(type(result))
      print(result)
      return render_template("result.html",result = result)

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
   	user = request.form['Name']
   	resp = make_response(render_template('readcookie.html'))
   	resp.set_cookie('username', user)
   
   return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('username')
   return '<h1>welcome '+name+'</h1>'

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello1.html', name = user)


@app.route('/myindex')
def myindex():
   return '<html><body><h1>Hello World HTML Code Returned </h1></body></html>'


@app.route('/rendertemplate')
def index():
   return render_template('hello.html')


@app.route('/flask')
def hello_flask():
	return 'Hello Flask'

@app.route('/python/')
def hello_python():
	return 'Hello Python'


@app.route("/")
def fmain():
	return "Welcome !"



if __name__ == "__main__":
	app.run()


