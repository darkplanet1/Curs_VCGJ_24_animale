from flask import Flask

import librarie.biblioteca_koala


app = Flask(__name__)

print('442D_koala')

@app.route("/" , methods=['GET'])
def index():
    ret = "<h1></h1>Informatii despre koala 442D</h1>"
    return ret

@app.route("/koala/", methods=['GET'])
def get_koala():
    ret = "<h1>koala<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_koala.specie_koala()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_koala.zona_koala()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_koala.clasificare_koala()
    ret += "<br>"
    
    return ret
    
@app.route("/koala/specie", methods=['GET'])
def ia_specie_koala():
    ret = ""
    ret += librarie.biblioteca_koala.specie_koala()
    
    return ret
    
@app.route("/koala/zona", methods=['GET'])
def ia_zona_koala():
    ret = ""
    ret += librarie.biblioteca_koala.zona_koala()
    
    return ret
    
@app.route("/koala/clasificare", methods=['GET'])
def ia_clasificare_koala():
    ret = ""
    ret += librarie.biblioteca_koala.clasificare_koala()
    
    return ret
    
@app.route("/australian/", methods=['GET'])
def get_australian():
    ret = "<h1>australian<h1>"
    ret += "specie: "
    ret += librarie.biblioteca_koala.specie_australian()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_koala.zona_australian()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_koala.clasificare_australian()
    ret += "<br>"
    
    return ret
    
@app.route("/australian/specie", methods=['GET'])
def ia_specie_australian():
    ret = ""
    ret += librarie.biblioteca_koala.specie_australian()
    
    return ret
    
@app.route("/australian/zona", methods=['GET'])
def ia_zona_australian():
    ret = ""
    ret += librarie.biblioteca_koala.zona_australian()
    
    return ret
    
@app.route("/australian/clasificare", methods=['GET'])
def ia_clasificare_australian():
    ret = ""
    ret += librarie.biblioteca_koala.clasificare_australian()
    
    return ret
    
    
app.run(host = "127.0.0.1", port = 5001)
