from flask import Flask, render_template
import datetime

app = Flask(__name__)

regular_meals = [
    {"name": "Pizza med ost", "image": "/bilder/pizza.png"},
    {"name": "Kyllingnuggets med microplast", "image": "/bilder/nugget.png"},
    {"name": "Spaghetti med spaghet", "image": "/bilder/spagetti.png"}
]
 #the food for every day

weekly_specials = [
    [   # Monday
        {"name": "Taco som er ok - 2kr", "image": "bilder/taco.png"},
        {"name": "Chili uten chill 34kr", "image": "bilder/chili.png"},
        {"name": "Burritos med kristene bønner", "image": "bilder/burrito.png"}
    ],
    [   # Tuesday
        {"name": "Hamburger fra hamburg", "image": "bilder/hamburger.png"},
        {"name": "Pølse med brød", "image": "bilder/polse.png"},
        {"name": "Pommes frites med ekstra pommes", "image": "bilder/pommes.png"}
    ],
    [   # Wednesday
        {"name": "Fiskepinner uten pinne", "image": "bilder/fiskepinne.png"},
        {"name": "Macbok and Cheese", "image": "bilder/macncheese.png"},
        {"name": "Salat med salsa danser", "image": "bilder/salat.png"}
    ],
    [   # Thursday
        {"name": "Kjøttkake med stor kake", "image": "bilder/kjottkake.png"},
        {"name": "Potetmos moset potet", "image": "bilder/potetmos.png"},
        {"name": "Mais er kult", "image": "bilder/mais.png"}
    ],
    [   # Friday
        {"name": "Lasagne med lala", "image": "bilder/lasagne.png"},
        {"name": "Kebab med bob habab", "image": "bilder/kebab.png"},
        {"name": "Cæsarsalat med ekstra cæsar", "image": "bilder/caesar.png"}
    ]
]
             


@app.route('/')
def home():
    return render_template("index.html") #this one just looks pretty :p

@app.route('/meny')
def meny():
    today_index = datetime.datetime.now().weekday() #the variable today_index gets the current day of the week as an integer :D

    
    if today_index < 5:  
        meals_today = regular_meals + weekly_specials[today_index]
        day_name = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"][today_index] #0 to 4 is the weekdays so if it's less than 5 we get the day name from this list
    else:
        meals_today = ["Ingen måltid i helgen!"] #if it's saturday or sunday
        day_name = "Helg"

    return render_template("meny.html", meals=meals_today, day=day_name) #enforces the variables meals and day in meny.html

@app.route('/varer')
def varer():
    day_name = "Faste varer"
    return render_template("varer.html", meals=regular_meals, day=day_name) #enforces the variables meals and day in varer.html

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html") 

if __name__ == "__main__":
    app.run(debug=True)
