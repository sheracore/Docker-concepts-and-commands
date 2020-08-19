from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
    return("Hello world\n")

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
