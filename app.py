from flask import Flask, jsonify

app = Flask(__name__)

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def hello():
    return "Hello Flask-Heroku"


@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)

@app.route('/name')
def name():
    return "<font color=purple>น</font><font color=blue>รี<font color=green>ก</font>รี<font color=yellow>า</font><font color=orange>น</font><font color=orange>ต์</font> ท่าพริก <br>เลขที่ 14 ชั้น ม.4/10"

if __name__ == "__main__":
    app.run(debug=False)
