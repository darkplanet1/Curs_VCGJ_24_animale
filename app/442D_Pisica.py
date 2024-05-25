from flask import Flask
import librarie.biblioteca_Pisica

app = Flask(__name__)

print('442D_Pisica')

@app.route("/", methods=['GET'])
def index():
    ret = "<h1>Informatii despre Pisica 442D</h1>"
    return ret

@app.route("/Pisica/", methods=['GET'])
def get_Pisica():
    ret = "<h1>Pisica<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_Pisica.specie_Pisica()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_Pisica.zona_Pisica()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_Pisica.clasificare_Pisica()
    ret += "<br>"
    
    return ret
    
@app.route("/Pisica/specie", methods=['GET'])
def ia_specie_Pisica():
    ret = ""
    ret += librarie.biblioteca_Pisica.specie_Pisica()
    
    return ret
    
@app.route("/Pisica/zona", methods=['GET'])
def ia_zona_Pisica():
    ret = ""
    ret += librarie.biblioteca_Pisica.zona_Pisica()
    
    return ret
    
@app.route("/Pisica/clasificare", methods=['GET'])
def ia_clasificare_Pisica():
    ret = ""
    ret += librarie.biblioteca_Pisica.clasificare_Pisica()
    
    return ret
    
@app.route("/European/", methods=['GET'])
def get_European():
    ret = "<h1>European<h1>"
    ret += "specie: "
    ret += librarie.biblioteca_Pisica.specie_European()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_Pisica.zona_European()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_Pisica.clasificare_European()
    ret += "<br>"
    
    return ret
    
@app.route("/European/specie", methods=['GET'])
def ia_specie_European():
    ret = ""
    ret += librarie.biblioteca_Pisica.specie_European()
    
    return ret
    
@app.route("/European/zona", methods=['GET'])
def ia_zona_European():
    ret = ""
    ret += librarie.biblioteca_Pisica.zona_European()
    
    return ret
    
@app.route("/European/clasificare", methods=['GET'])
def ia_clasificare_European():
    ret = ""
    ret += librarie.biblioteca_Pisica.clasificare_European()
    
    return ret

app.run(host="127.0.0.1", port=5001)
