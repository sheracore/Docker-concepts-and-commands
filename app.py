from flask import Flask
import redis

app = Flask(__name__)

@app.route('/')
def say_hello():
    r = redis.Redis(host='localhost', port=6379, db=0)
    name = r.get('name').decode()
    #print(name)
    return name

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
