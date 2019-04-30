#flask_web/app.py

from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')

def hello():
    #return "running flask inside a container"
    user={'username':'Kanchan'}
    return render_template('index.html',title='Home',user=user)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=int("5000"))
