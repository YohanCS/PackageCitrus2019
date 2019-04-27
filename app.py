from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def parse_request():
    data = request.data  # data is empty
    # need posted data here
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)