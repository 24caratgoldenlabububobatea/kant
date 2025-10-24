from flask import Flask, render_template
import datetime

app = Flask(__name__)

regular_meals = ["Pizza", "Kyllingnuggets", "Spaghetti"] #the food for every day

weekly_specials = [ #all the food for the week
    ["Taco", "Chili", "Burritos"],                     
    ["Hamburger", "Pølse med brød", "Pommes frites"],  
    ["Fiskepinner", "Mac and Cheese", "Salat"],        
    ["Kjøttkake", "Potetmos", "Mais"],                 
    ["Lasagne", "Kebab", "Cæsarsalat"]                 
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
    day_name = "Alle dager"
    return render_template("varer.html", meals=regular_meals, day=day_name) #enforces the variables meals and day in varer.html

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html") 

if __name__ == "__main__":
    app.run(debug=True)
