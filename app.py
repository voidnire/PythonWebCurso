from flask import Flask

app = Flask("ola")

@app.route('/')
def ola():
    return "Olá Mundo"