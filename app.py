from flask import Flask, render_template
import random

app = Flask(__name__)

regular_meals = ["Pizza", "Chicken Nuggets", "Spaghetti"]

weekly_specials = [
    ["Tacos", "Chili", "Burritos"],
    ["Hamburgers", "Hot Dogs", "Fries"],
    ["Fish Sticks", "Mac and Cheese", "Salad"],
    ["Meatloaf", "Mashed Potatoes", "Corn"]
]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/meny')
def meny():
    current_week = random.randint(1, 4)
    meals_this_week = regular_meals + weekly_specials[current_week - 1]
    return render_template("meny.html", meals=meals_this_week, week=current_week)

@app.route('/varer')
def varer():
    return render_template("varer.html")

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")

if __name__ == "__main__":
    app.run(debug=True)
