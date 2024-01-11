from flask import Flask, url_for, request, redirect, abort

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
   return('hello')


if __name__ == "__main__":
    print("in if")
    app.run(debug=True)