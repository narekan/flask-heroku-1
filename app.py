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
    return "<font color=pink>นรีกานต์</font> <font color=purple>ท่าพริก</font> <br><font color=green>เลขที่ 14</font> <font color=yellow>ชั้น ม.4/10</font>"

if __name__ == "__main__":
    app.run(debug=False)
