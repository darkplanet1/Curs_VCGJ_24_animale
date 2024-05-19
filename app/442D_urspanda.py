from flask import Flask

import librarie.biblioteca_urspanda


app = Flask(__name__)

print('442D_urspanda')

@app.route("/" , methods=['GET'])
def index():
    ret = "<h1></h1>Informatii despre urs panda 442D</h1>"
    return ret

@app.route("/urspanda/", methods=['GET'])
def get_urspanda():
    ret = "<h1>Urs panda<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_urspanda.specie_urspanda()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_urspanda.zona_urspanda()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_urspanda.clasificare_urspanda()
    ret += "<br>"
    
    return ret
    
@app.route("/urspanda/specie", methods=['GET'])
def ia_specie_urspanda():
    ret = ""
    ret += librarie.biblioteca_urspanda.specie_urspanda()
    
    return ret
    
@app.route("/urspanda/zona", methods=['GET'])
def ia_zona_urspanda():
    ret = ""
    ret += librarie.biblioteca_urspanda.zona_urspanda()
    
    return ret
    
@app.route("/urspanda/clasificare", methods=['GET'])
def ia_clasificare_urspanda():
    ret = ""
    ret += librarie.biblioteca_urspanda.clasificare_urspanda()
    
    return ret
    
@app.route("/pandarosu/", methods=['GET'])
def get_african():
    ret = "<h1>Panda rosu<h1>"
    ret += "specie: "
    ret += librarie.biblioteca_urspanda.specie_pandarosu()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_urspanda.zona_pandarosu()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_urspanda.clasificare_pandarosu()
    ret += "<br>"
    
    return ret
    
@app.route("/pandarosu/specie", methods=['GET'])
def ia_specie_pandarosu():
    ret = ""
    ret += librarie.biblioteca_urspanda.specie_pandarosu()
    
    return ret
    
@app.route("/pandarosu/zona", methods=['GET'])
def ia_zona_pandarosu():
    ret = ""
    ret += librarie.biblioteca_urspanda.zona_pandarosu()
    
    return ret
    
@app.route("/pandarosu/clasificare", methods=['GET'])
def ia_clasificare_pandarosu():
    ret = ""
    ret += librarie.biblioteca_urspanda.clasificare_pandarosu()
    
    return ret
    
    
app.run(host = "127.0.0.1", port = 5001)
