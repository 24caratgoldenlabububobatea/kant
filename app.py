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
        {"name": "Burritos med kristene bønner 2kr", "image": "bilder/burrito.png"}
    ],
    [   # Tuesday
        {"name": "Hamburger fra hamburg 1000kr", "image": "bilder/hamburger.png"},
        {"name": "Pølse med brød 23kr", "image": "bilder/polse.png"},
        {"name": "Pommes frites med ekstra pommes", "image": "bilder/pommes.png"}
    ],
    [   # Wednesday
        {"name": "Fiskepinner uten pinne 234kr", "image": "bilder/fiskepinne.png"},
        {"name": "Macbok and Cheese 2323kr", "image": "bilder/macncheese.png"},
        {"name": "Salat med salsa danser 93982kr", "image": "bilder/salat.png"}
    ],
    [   # Thursday
        {"name": "Kjøttkake med stor kake 82839kr", "image": "bilder/kjottkake.png"},
        {"name": "Potetmos moset potet 232kr", "image": "bilder/potetmos.png"},
        {"name": "Mais er kult 2323kr", "image": "bilder/mais.png"}
    ],
    [   # Friday
        {"name": "Lasagne med lala 933kr", "image": "bilder/lasagne.png"},
        {"name": "Kebab med bob habab 23kr", "image": "bilder/kebab.png"},
        {"name": "Cæsarsalat med ekstra cæsar 94kr", "image": "bilder/caesar.png"}
    ]
]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/meny')
def meny():
    today_index = datetime.datetime.now().weekday()  # Monday = 0, Sunday = 6

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
    days = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]
    return render_template("varer.html", weekly_specials=zip(days, weekly_specials))

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")

if __name__ == "__main__":
    app.run(debug=True)
