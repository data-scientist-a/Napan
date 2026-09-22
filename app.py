from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    cakes = [
        {"name": "Chocolate Cake", "price": 120, "image": "chocolate.jpg"},
        {"name": "Vanilla Cake", "price": 100, "image": "vanilla.jpg"},
        {"name": "Fruit Cake", "price": 150, "image": "fruit.jpg"}
    ]
    return render_template("index.html", cakes=cakes)

if __name__ == "__main__":
    app.run(debug=True)
