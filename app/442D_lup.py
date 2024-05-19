from flask import Flask

import librarie.biblioteca_lup


app = Flask(__name__)

print('442D_lup')

@app.route("/" , methods=['GET'])
def index():
    ret = "<h1></h1>Informatii despre lupi 442D</h1>"
    return ret

@app.route("/lup/", methods=['GET'])
def get_lup():
    ret = "<h1>lup<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_lup.specie_lup()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_lup.zona_lup()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_lup.clasificare_lup()
    ret += "<br>"
    
    return ret
    
@app.route("/lup/specie", methods=['GET'])
def ia_specie_lup():
    ret = ""
    ret += librarie.biblioteca_lup.specie_lup()
    
    return ret
    
@app.route("/lup/zona", methods=['GET'])
def ia_zona_lup():
    ret = ""
    ret += librarie.biblioteca_lup.zona_lup()
    
    return ret
    
@app.route("/lup/clasificare", methods=['GET'])
def ia_clasificare_lup():
    ret = ""
    ret += librarie.biblioteca_lup.clasificare_lup()
    
    return ret
    
@app.route("/european/", methods=['GET'])
def get_european():
    ret = "<h1>european<h1>"
    ret += "specie: "
    ret += librarie.biblioteca_lup.specie_european()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_lup.zona_european()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_lup.clasificare_european()
    ret += "<br>"
    
    return ret
    
@app.route("/european/specie", methods=['GET'])
def ia_specie_european():
    ret = ""
    ret += librarie.biblioteca_lup.specie_european()
    
    return ret
    
@app.route("/european/zona", methods=['GET'])
def ia_zona_european():
    ret = ""
    ret += librarie.biblioteca_lup.zona_european()
    
    return ret
    
@app.route("/european/clasificare", methods=['GET'])
def ia_clasificare_european():
    ret = ""
    ret += librarie.biblioteca_lup.clasificare_european()
    
    return ret
    
    
app.run(host = "127.0.0.1", port = 5001)
