from flask import Flask
import librarie.biblioteca_Rechin

app = Flask(__name__)

print('442D_Rechin')

@app.route("/", methods=['GET'])
def index():
    ret = "<h1>Informatii despre Rechin 442D</h1>"
    return ret

@app.route("/Rechin/", methods=['GET'])
def get_Rechin():
    ret = "<h1>Rechin<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_Rechin.specie_Rechin()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_Rechin.zona_Rechin()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_Rechin.clasificare_Rechin()
    ret += "<br>"
    
    return ret
    
@app.route("/Rechin/specie", methods=['GET'])
def ia_specie_Rechin():
    ret = ""
    ret += librarie.biblioteca_Rechin.specie_Rechin()
    
    return ret
    
@app.route("/Rechin/zona", methods=['GET'])
def ia_zona_Rechin():
    ret = ""
    ret += librarie.biblioteca_Rechin.zona_Rechin()
    
    return ret
    
@app.route("/Rechin/clasificare", methods=['GET'])
def ia_clasificare_Rechin():
    ret = ""
    ret += librarie.biblioteca_Rechin.clasificare_Rechin()
    
    return ret
    
@app.route("/European/", methods=['GET'])
def get_European():
    ret = "<h1>European<h1>"
    ret += "specie: "
    ret += librarie.biblioteca_Rechin.specie_European()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_Rechin.zona_European()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_Rechin.clasificare_European()
    ret += "<br>"
    
    return ret
    
@app.route("/European/specie", methods=['GET'])
def ia_specie_European():
    ret = ""
    ret += librarie.biblioteca_Rechin.specie_European()
    
    return ret
    
@app.route("/European/zona", methods=['GET'])
def ia_zona_European():
    ret = ""
    ret += librarie.biblioteca_Rechin.zona_European()
    
    return ret
    
@app.route("/European/clasificare", methods=['GET'])
def ia_clasificare_European():
    ret = ""
    ret += librarie.biblioteca_Rechin.clasificare_European()
    
    return ret

app.run(host="127.0.0.1", port=5001)
