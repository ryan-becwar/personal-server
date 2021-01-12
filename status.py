from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    print("returned hello")
    return 'Hello, World!'

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        content = 1
        return update_status(content)
    else:
        return show_status_form()
    
def show_status_form():
    return "Status form here"

def update_status(content):
    print(content)
    return 'Content is %s' % str(content)
