#!/usr/bin/python

from flask import Flask, render_template

def testweb(temp,forecast,weathericon,tubeStatus,bus93pty,bus93wim,bus39pty,bus39clp,location,coffeedata):

  app = Flask(__name__)

  @app.route('/')
  def homepage():
    return "Hello world!"

  @app.route('/testboot')
  def testboot():
    return render_template("testboot.html", title="testboot")

  @app.route('/theme')
  def theme():
    return render_template("theme.html", title="testboot")

  @app.route('/dashtest')
  def apptest():
    return render_template("nead.html", temp=temp, forecast=forecast, weathericon=weathericon, tubeStatus=tubeStatus, bus93pty=bus93pty, bus93wim=bus93wim, bus39pty=bus39pty, bus39clp=bus39clp,location=location,coffeedata=coffeedata)

  app.run(use_reloader=False,debug=False,port=5001)
