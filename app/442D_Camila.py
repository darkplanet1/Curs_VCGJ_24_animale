from flask import Flask
import librarie.biblioteca_Camila

app = Flask(__name__)

print('442D_Camila')

@app.route("/", methods=['GET'])
def index():
    ret = "<h1>Informatii despre Camila 442D</h1>"
    return ret

@app.route("/Camila/", methods=['GET'])
def get_Camila():
    ret = "<h1>Camila<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_Camila.specie_Camila()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_Camila.zona_Camila()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_Camila.clasificare_Camila()
    ret += "<br>"
    
    return ret
    
@app.route("/Camila/specie", methods=['GET'])
def ia_specie_Camila():
    ret = ""
    ret += librarie.biblioteca_Camila.specie_Camila()
    
    return ret
    
@app.route("/Camila/zona", methods=['GET'])
def ia_zona_Camila():
    ret = ""
    ret += librarie.biblioteca_Camila.zona_Camila()
    
    return ret
    
@app.route("/Camila/clasificare", methods=['GET'])
def ia_clasificare_Camila():
    ret = ""
    ret += librarie.biblioteca_Camila.clasificare_Camila()
    
    return ret
    
@app.route("/Arabian/", methods=['GET'])
def get_Arabian():
    ret = "<h1>Arabian<h1>"
    ret += "specie: "
    ret += librarie.biblioteca_Camila.specie_Arabian()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_Camila.zona_Arabian()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_Camila.clasificare_Arabian()
    ret += "<br>"
    
    return ret
    
@app.route("/Arabian/specie", methods=['GET'])
def ia_specie_Arabian():
    ret = ""
    ret += librarie.biblioteca_Camila.specie_Arabian()
    
    return ret
    
@app.route("/Arabian/zona", methods=['GET'])
def ia_zona_Arabian():
    ret = ""
    ret += librarie.biblioteca_Camila.zona_Arabian()
    
    return ret
    
@app.route("/Arabian/clasificare", methods=['GET'])
def ia_clasificare_Arabian():
    ret = ""
    ret += librarie.biblioteca_Camila.clasificare_Arabian()
    
    return ret

app.run(host="127.0.0.1", port=5001)

