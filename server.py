from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'hello world!',200

@app.route("/calculator/add", methods=['POST'])
def add():
    data=request.json
    n1=data["first"]
    n2=data["second"]
    res={"result":n1+n2}
    return res

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    return ''

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
