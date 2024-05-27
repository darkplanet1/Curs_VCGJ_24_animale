from flask import Flask
import librarie.biblioteca_Crocodil

app = Flask(__name__)

print('442D_Crocodil')

@app.route("/", methods=['GET'])
def index():
    ret = "<h1>Informatii despre Crocodil 442D</h1>"
    return ret

@app.route("/Crocodil/", methods=['GET'])
def get_Crocodil():
    ret = "<h1>Crocodil<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_Crocodil.specie_Crocodil()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_Crocodil.zona_Crocodil()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_Crocodil.clasificare_Crocodil()
    ret += "<br>"
    
    return ret
    
@app.route("/Crocodil/specie", methods=['GET'])
def ia_specie_Crocodil():
    ret = ""
    ret += librarie.biblioteca_Crocodil.specie_Crocodil()
    
    return ret
    
@app.route("/Crocodil/zona", methods=['GET'])
def ia_zona_Crocodil():
    ret = ""
    ret += librarie.biblioteca_Crocodil.zona_Crocodil()
    
    return ret
    
@app.route("/Crocodil/clasificare", methods=['GET'])
def ia_clasificare_Crocodil():
    ret = ""
    ret += librarie.biblioteca_Crocodil.clasificare_Crocodil()
    
    return ret
    
@app.route("/African/", methods=['GET'])
def get_Arabian():
    ret = "<h1>African<h1>"
    ret += "specie: "
    ret += librarie.biblioteca_Crocodil.specie_African()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_Crocodil.zona_African()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_Crocodil.clasificare_African()
    ret += "<br>"
    
    return ret
    
@app.route("/African/specie", methods=['GET'])
def ia_specie_African():
    ret = ""
    ret += librarie.biblioteca_Crocodil.specie_African()
    
    return ret
    
@app.route("/African/zona", methods=['GET'])
def ia_zona_African():
    ret = ""
    ret += librarie.biblioteca_Crocodil.zona_African()
    
    return ret
    
@app.route("/African/clasificare", methods=['GET'])
def ia_clasificare_African():
    ret = ""
    ret += librarie.biblioteca_Crocodil.clasificare_African()
    
    return ret

app.run(host="127.0.0.1", port=5001)
