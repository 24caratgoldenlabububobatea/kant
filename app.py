from flask import Flask, render_template
import datetime

app = Flask(__name__)

regular_meals = ["Pizza", "Kyllingnuggets", "Spaghetti"]

weekly_specials = [
    ["Taco", "Chili", "Burritos"],                     
    ["Hamburger", "Pølse med brød", "Pommes frites"],  
    ["Fiskepinner", "Mac and Cheese", "Salat"],        
    ["Kjøttkake", "Potetmos", "Mais"],                 
    ["Lasagne", "Kebab", "Cæsarsalat"]                 
]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/meny')
def meny():
    today_index = datetime.datetime.now().weekday()

    
    if today_index < 5:  
        meals_today = regular_meals + weekly_specials[today_index]
        day_name = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"][today_index]
    else:
        meals_today = ["Ingen måltid i helgen!"]
        day_name = "Helg"

    return render_template("meny.html", meals=meals_today, day=day_name)

@app.route('/varer')
def varer():
    day_name = "Alle dager"
    return render_template("varer.html", meals=regular_meals, day=day_name)

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")

if __name__ == "__main__":
    app.run(debug=True)
