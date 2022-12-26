from flask import Flask, flash, redirect, url_for, request, render_template, session

app = Flask(__name__)
app.secret_key = 'flaskapp'

@app.route('/success/<name>')
def success(name):
   return render_template('myself.html')

@app.route('/',methods = ['POST','GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      session['user'] = user
      return redirect(url_for('user'))
   else:
      user = request.args.get('nm')
      return render_template('login.html')

@app.route('/user')
def user():
   if 'user' in session:
      user = session['user']
      return redirect(url_for('success',name = user))
   else:
      return redirect(url_for(''))

@app.route('/logout')
def logout():
   session.pop('user', None)
   flash('You were successfully logged out')
   return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)
    