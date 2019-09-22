from flask import Flask
from flask import render_template

app = Flask(__name__)

"""
@app.route('/hello')
def hello_world():
    values = {"val1": 100, "val2" :200}
    return render_template('index.html',values=values)
"""

@app.route('/index')
def index():
    return  render_template('index.html')

    
if __name__ == '__main__':
    app.run()