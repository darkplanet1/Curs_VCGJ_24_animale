from flask import Flask

import librarie.biblioteca_pinguin


app = Flask(__name__)

print('442D_pinguin')

@app.route("/" , methods=['GET'])
def index():
    ret = "<h1>Informatii despre pinguini 442D</h1>"
    return ret

    
    
    
    
@app.route("/pinguin/magellan", methods=['GET'])
def get_magellan():
    ret = "<h3>Pinguini Magellan<h3>"
    ret += "specie: "
    ret += librarie.biblioteca_pinguin.specie_magellan()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_pinguin.zona_magellan()
    ret += "<br>"
    
    ret += "Detalii: "
    ret += librarie.biblioteca_pinguin.detalii_magellan()
    ret += "<br>"
    
    return ret
    
@app.route("/pinguin/specie", methods=['GET'])
def ia_specie_magellan():
    ret = ""
    ret += librarie.biblioteca_pinguin.specie_magellan()
    
    return ret
    
@app.route("/pinguin/zona", methods=['GET'])
def ia_zona_magellan():
    ret = ""
    ret += librarie.biblioteca_pinguin.zona_magellan()
    
    return ret
    
@app.route("/pinguin/detalii", methods=['GET'])
def ia_detalii_magellan():
    ret = ""
    ret += librarie.biblioteca_pinguin.detalii_magellan()
    
    return ret
    

    
    
    
    
    
    
@app.route("/pinguin/gentoo", methods=['GET'])
def get_gentoo():
    ret = "<h3>Pinguini Gentoo<h3>"
    ret += "Specie: "
    ret += librarie.biblioteca_pinguin.specie_gentoo()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_pinguin.zona_gentoo()
    ret += "<br>"
    
    ret += "Detalii: "
    ret += librarie.biblioteca_pinguin.detalii_gentoo()
    ret += "<br>"
    
    return ret
    
@app.route("/pinguin/specie", methods=['GET'])
def ia_specie_gentoo():
    ret = ""
    ret += librarie.biblioteca_pinguin.specie_gentoo()
    
    return ret
    
@app.route("/pinguin/zona", methods=['GET'])
def ia_zona_gentoo():
    ret = ""
    ret += librarie.biblioteca_pinguin.zona_gentoo()
    
    return ret
    
@app.route("/pinguin/detalii", methods=['GET'])
def ia_detalii_gentoo():
    ret = ""
    ret += librarie.biblioteca_pinguin.detalii_gentoo()
    
    return ret
    
    
    
    
app.run(host = "127.0.0.1", port = 5001)
