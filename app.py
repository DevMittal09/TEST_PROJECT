from flask import Flask, render_template, jsonify

app = Flask(__name__)


FOOD =[
    {
        'id':1,
        'title': "Panner Tikka",
        "hehe": "indian cottage cheese",
        "Price": "₹200"
    },
    {
        'id':2,
        'title': "Tandoori Soyabeen",
        "hehe": "tandoori soyabeen chaap",
        "Price": "₹200"
    },
    {
        'id':3,
        'title': "Panner makhni",
        "hehe": "indian main course",
        "Price": "₹200"
    },

    {
        'id':4,
        'title': "Panner Tikka",
        "hehe": "indian cottage cheese",
        "Price": "₹200"
    }
]


@app.route("/")
def hello_world():
    return render_template("home.html",foods=FOOD)

@app.route("/api/food")
def list_foods():
    return jsonify(FOOD)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)