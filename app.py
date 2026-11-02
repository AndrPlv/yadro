from flask import Flask, render_template, request, redirect, url_for
import folium
import sqlite3

app = Flask(__name__)

@app.route('/')
def welcome():
    return redirect(url_for('registration'))

@app.route('/registration')
def registration():
    return render_template('registration.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)