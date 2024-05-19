from flask import Flask

import librarie.biblioteca_arici


app = Flask(__name__)

print('442D_arici')

@app.route("/" , methods=['GET'])
def index():
    ret = "<h1></h1>Informatii despre aricii 442D</h1>"
    return ret

@app.route("/arici/", methods=['GET'])
def get_arici():
    ret = "<h1>arici<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_arici.specie_arici()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_arici.zona_arici()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_arici.clasificare_arici()
    ret += "<br>"
    
    return ret
    
@app.route("/arici/specie", methods=['GET'])
def ia_specie_arici():
    ret = ""
    ret += librarie.biblioteca_arici.specie_arici()
    
    return ret
    
@app.route("/arici/zona", methods=['GET'])
def ia_zona_arici():
    ret = ""
    ret += librarie.biblioteca_arici.zona_arici()
    
    return ret
    
@app.route("/arici/clasificare", methods=['GET'])
def ia_clasificare_arici():
    ret = ""
    ret += librarie.biblioteca_arici.clasificare_arici()
    
    return ret
    
@app.route("/african/", methods=['GET'])
def get_african():
    ret = "<h1>african<h1>"
    ret += "specie: "
    ret += librarie.biblioteca_arici.specie_african()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_arici.zona_african()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_arici.clasificare_african()
    ret += "<br>"
    
    return ret
    
@app.route("/african/specie", methods=['GET'])
def ia_specie_african():
    ret = ""
    ret += librarie.biblioteca_arici.specie_african()
    
    return ret
    
@app.route("/african/zona", methods=['GET'])
def ia_zona_african():
    ret = ""
    ret += librarie.biblioteca_arici.zona_african()
    
    return ret
    
@app.route("/african/clasificare", methods=['GET'])
def ia_clasificare_african():
    ret = ""
    ret += librarie.biblioteca_arici.clasificare_african()
    
    return ret
    
    
app.run(host = "127.0.0.1", port = 5001)
