from flask import Flask

import librarie.biblioteca_tigru


app = Flask(__name__)

print('442D_tigru')

@app.route("/" , methods=['GET'])
def index():
    ret = "<h1>Informatii despre tigru 442D</h1>"
    return ret

@app.route("/tigru/", methods=['GET'])
def get_tigru():
    ret = "<h1>tigru<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_tigru.specie_tigru()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_tigru.zona_tigru()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_tigru.clasificare_tigru()
    ret += "<br>"
    
    return ret
    
@app.route("/tigru/specie", methods=['GET'])
def ia_specie_tigru():
    ret = ""
    ret += librarie.biblioteca_tigru.specie_tigru()
    
    return ret
    
@app.route("/tigru/zona", methods=['GET'])
def ia_zona_tigru():
    ret = ""
    ret += librarie.biblioteca_tigru.zona_tigru()
    
    return ret
    
@app.route("/tigru/clasificare", methods=['GET'])
def ia_clasificare_tigru():
    ret = ""
    ret += librarie.biblioteca_tigru.clasificare_tigru()
    
    return ret
    
@app.route("/siberian/", methods=['GET'])
def get_siberian():
    ret = "<h1>siberian<h1>"
    ret += "specie: "
    ret += librarie.biblioteca_tigru.specie_siberian()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_tigru.zona_siberian()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_tigru.clasificare_siberian()
    ret += "<br>"
    
    return ret
    
@app.route("/siberian/specie", methods=['GET'])
def ia_specie_siberian():
    ret = ""
    ret += librarie.biblioteca_tigru.specie_siberian()
    
    return ret
    
@app.route("/siberian/zona", methods=['GET'])
def ia_zona_siberian():
    ret = ""
    ret += librarie.biblioteca_tigru.zona_siberian()
    
    return ret
    
@app.route("/siberian/clasificare", methods=['GET'])
def ia_clasificare_siberian():
    ret = ""
    ret += librarie.biblioteca_tigru.clasificare_siberian()
    
    return ret
    
    
app.run(host = "127.0.0.1", port = 5001)
