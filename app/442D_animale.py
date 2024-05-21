# app/442D_animale.py
from flask import Flask
from app.lib.biblioteca_animale import culoare_Camila, descriere_CAmila

app = Flask(__name__)

@app.route('/')
def home():
    return "Bine ați venit la aplicația pentru tema animale!"

@app.route('/Camila')
def Camila():
    return "Aceasta este pagina pentru Camila."

@app.route('/culoare_Camila')
def culoare():
    return culoare_Camila()

@app.route('/descriere_Camila')
def descriere():
    return descriere_Camila()

if __name__ == '__main__':
    app.run(debug=True)

