from flask import Flask, render_template
import datetime

app = Flask(__name__)

regular_meals = [
    {"name": "Pizza med ost", "image": "/bilder/pizza.png"},
    {"name": "Kyllingnuggets med microplast", "image": "/bilder/nugget.png"},
    {"name": "Spaghetti med spaghet", "image": "/bilder/spagetti.png"}
]

weekly_specials = [
    [   # Monday
        {"name": "Taco som er ok - 2kr", "image": "bilder/taco.png"},
        {"name": "Chili uten chill 34kr", "image": "bilder/chili.png"},
        {"name": "Burritos med kristene bønner 22kr", "image": "bilder/taco.png"}
    ],
    [   # Tuesday
        {"name": "Hamburger fra hamburg 333kr", "image": "bilder/hamburger.png"},
        {"name": "Pølse med brød 123kr", "image": "bilder/polse.png"},
        {"name": "Pommes frites med ekstra pommes 12kr", "image": "bilder/pommes.png"}
    ],
    [   # Wednesday
        {"name": "Fiskepinner uten pinne 30kr", "image": "bilder/fiskepinne.jpg"},
        {"name": "Macbok and Cheese 394kr", "image": "bilder/macncheese.png"},
        {"name": "Salat med salsa danser 223kr", "image": "bilder/salat.png"}
    ],
    [   # Thursday
        {"name": "Kjøttkake med stor kake 11kr", "image": "bilder/kjottkake.png"},
        {"name": "Potetmos moset potet 23kr", "image": "bilder/potetmos.png"},
        {"name": "Mais er kult 94kr", "image": "bilder/mais.png"}
    ],
    [   # Friday
        {"name": "Lasagne med lala 94kr", "image": "bilder/lasagne.png"},
        {"name": "Kebab med bob habab 233kr", "image": "bilder/kebab.png"},
        {"name": "Cæsarsalat med ekstra cæsar 999kr", "image": "bilder/cæsar.png"}
    ]
]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/meny')
def meny():
    today_index = datetime.datetime.now().weekday()

    if today_index < 5:  # Monday to Friday
        meals_today = regular_meals + weekly_specials[today_index]
        day_name = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"][today_index]
    else:
        meals_today = [
            {"name": "Ingen måltid i helgen!", "image": "/bilder/no_food.png"}
        ]
        day_name = "Helg"

    return render_template("meny.html", meals=meals_today, day=day_name)

@app.route('/varer')
def varer():
    day_name = "Faste varer"
    return render_template("varer.html", meals=regular_meals, day=day_name)

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")

if __name__ == "__main__":
    app.run(debug=True)
