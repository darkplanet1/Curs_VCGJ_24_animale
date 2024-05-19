from flask import Flask

import librarie.biblioteca_vultur


app = Flask(__name__)

print('442D_vultur')

@app.route("/" , methods=['GET'])
def index():
    ret = "<h1></h1>Informatii despre vulturi 442D</h1>"
    return ret

@app.route("/vultur/", methods=['GET'])
def get_vultur():
    ret = "<h1>vultur<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_vultur.specie_vultur()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_vultur.zona_vultur()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_vultur.clasificare_vultur()
    ret += "<br>"
    
    return ret
    
@app.route("/vultur/specie", methods=['GET'])
def ia_specie_vultur():
    ret = ""
    ret += librarie.biblioteca_vultur.specie_vultur()
    
    return ret
    
@app.route("/vultur/zona", methods=['GET'])
def ia_zona_vultur():
    ret = ""
    ret += librarie.biblioteca_vultur.zona_vultur()
    
    return ret
    
@app.route("/vultur/clasificare", methods=['GET'])
def ia_clasificare_vultur():
    ret = ""
    ret += librarie.biblioteca_vultur.clasificare_vultur()
    
    return ret
    
@app.route("/Plesuv/", methods=['GET'])
def get_african():
    ret = "<h1>african<h1>"
    ret += "specie: "
    ret += librarie.biblioteca_vultur.specie_plesuv()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_vultur.zona_plesuv()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_vultur.clasificare_plesuv()
    ret += "<br>"
    
    return ret
    
@app.route("/african/specie", methods=['GET'])
def ia_specie_african():
    ret = ""
    ret += librarie.biblioteca_vultur.specie_plesuv()
    
    return ret
    
@app.route("/african/zona", methods=['GET'])
def ia_zona_african():
    ret = ""
    ret += librarie.biblioteca_vultur.zona_plesuv()
    
    return ret
    
@app.route("/african/clasificare", methods=['GET'])
def ia_clasificare_african():
    ret = ""
    ret += librarie.biblioteca_vultur.clasificare_plesuv()
    
    return ret
    
    
app.run(host = "127.0.0.1", port = 5001)
