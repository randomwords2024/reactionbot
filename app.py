from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Your file is hosted now. Now you can start your bot.'

if __name__ == '__main__':
    app.run()
