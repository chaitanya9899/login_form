from flask import Flask, render_template, request, send_file
import pandas as pd


app=Flask(__name__)



@app.route('/')
def home():
	return "hello "




if __name__ == '__main__':
	app.run(debug=True)