from flask import Flask

import librarie.biblioteca_elefant


app = Flask(__name__)

print('442D_elefant')

@app.route("/" , methods=['GET'])
def index():
    ret = "<h1></h1>Informatii despre elefanti 442D</h1>"
    return ret

@app.route("/elefant/", methods=['GET'])
def get_elefant():
    ret = "<h1>elefant<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_elefant.specie_elefant()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_elefant.zona_elefant()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_elefant.clasificare_elefant()
    ret += "<br>"
    
    return ret
    
@app.route("/elefant/specie", methods=['GET'])
def ia_specie_elefant():
    ret = ""
    ret += librarie.biblioteca_elefant.specie_elefant()
    
    return ret
    
@app.route("/elefant/zona", methods=['GET'])
def ia_zona_elefant():
    ret = ""
    ret += librarie.biblioteca_elefant.zona_elefant()
    
    return ret
    
@app.route("/elefant/clasificare", methods=['GET'])
def ia_clasificare_elefant():
    ret = ""
    ret += librarie.biblioteca_elefant.clasificare_elefant()
    
    return ret
    
@app.route("/african/", methods=['GET'])
def get_african():
    ret = "<h1>african<h1>"
    ret += "specie: "
    ret += librarie.biblioteca_elefant.specie_african()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_elefant.zona_african()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_elefant.clasificare_african()
    ret += "<br>"
    
    return ret
    
@app.route("/african/specie", methods=['GET'])
def ia_specie_african():
    ret = ""
    ret += librarie.biblioteca_elefant.specie_african()
    
    return ret
    
@app.route("/african/zona", methods=['GET'])
def ia_zona_african():
    ret = ""
    ret += librarie.biblioteca_elefant.zona_african()
    
    return ret
    
@app.route("/african/clasificare", methods=['GET'])
def ia_clasificare_african():
    ret = ""
    ret += librarie.biblioteca_elefant.clasificare_african()
    
    return ret
    
    
app.run(host = "127.0.0.1", port = 5001)
