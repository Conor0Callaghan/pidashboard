from random import randint
from flask import Flask, render_template
import threading
import time

testvar=1

app = Flask(__name__)

def genrandint():

  global testvar

  while True:
    testvar=randint(2,100)
    print ( "Now seeing " + str(testvar) )
    time.sleep(60)

threadprep = threading.Thread(name='genrandint', target=genrandint)
genrandint.daemon = True
threadprep.start()

@app.route('/var/<testvar>')
def varset(testvar=None):
  return testvar

@app.route('/')
def apptest():
  return render_template("test.html",testvar=testvar)

app.run(use_reloader=False,debug=True,port=5001)
