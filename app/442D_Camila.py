from flask import Flask
import librarie.biblioteca_camila

app = Flask(__name__)

print('442D_camila')

@app.route("/", methods=['GET'])
def index():
    ret = "<h1>Informatii despre camila 442D</h1>"
    return ret

@app.route("/camila/", methods=['GET'])
def get_camila():
    ret = "<h1>camila<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_camila.specie_camila()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_camila.zona_camila()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_camila.clasificare_camila()
    ret += "<br>"
    
    return ret
    
@app.route("/camila/specie", methods=['GET'])
def ia_specie_camila():
    ret = ""
    ret += librarie.biblioteca_camila.specie_camila()
    
    return ret
    
@app.route("/camila/zona", methods=['GET'])
def ia_zona_camila():
    ret = ""
    ret += librarie.biblioteca_camila.zona_camila()
    
    return ret
    
@app.route("/camila/clasificare", methods=['GET'])
def ia_clasificare_camila():
    ret = ""
    ret += librarie.biblioteca_camila.clasificare_camila()
    
    return ret
    
@app.route("/siberian/", methods=['GET'])
def get_siberian():
    ret = "<h1>siberian<h1>"
    ret += "specie: "
    ret += librarie.biblioteca_camila.specie_siberian()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_camila.zona_siberian()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_camila.clasificare_siberian()
    ret += "<br>"
    
    return ret
    
@app.route("/siberian/specie", methods=['GET'])
def ia_specie_siberian():
    ret = ""
    ret += librarie.biblioteca_camila.specie_siberian()
    
    return ret
    
@app.route("/siberian/zona", methods=['GET'])
def ia_zona_siberian():
    ret = ""
    ret += librarie.biblioteca_camila.zona_siberian()
    
    return ret
    
@app.route("/siberian/clasificare", methods=['GET'])
def ia_clasificare_siberian():
    ret = ""
    ret += librarie.biblioteca_camila.clasificare_siberian()
    
    return ret

app.run(host="127.0.0.1", port=5001)

