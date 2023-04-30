from flask import Flask,render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def Home():
    return "Jay Mataji"

app.run(debug=True,host='0.0.0.0',port=5000)