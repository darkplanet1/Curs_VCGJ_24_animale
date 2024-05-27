from flask import Flask
import librarie.biblioteca_Rinocer

app = Flask(__name__)

print('442D_Rinocer')

@app.route("/", methods=['GET'])
def index():
    ret = "<h1>Informatii despre Rinocer 442D</h1>"
    return ret

@app.route("/Rinocer/", methods=['GET'])
def get_Rinocer():
    ret = "<h1>Rinocer<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_Rinocer.specie_Rinocer()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_Rinocer.zona_Rinocer()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_Rinocer.clasificare_Rinocer()
    ret += "<br>"
    
    return ret
    
@app.route("/Rinocer/specie", methods=['GET'])
def ia_specie_Rinocer():
    ret = ""
    ret += librarie.biblioteca_Rinocer.specie_Rinocer()
    
    return ret
    
@app.route("/Rinocer/zona", methods=['GET'])
def ia_zona_Rinocer():
    ret = ""
    ret += librarie.biblioteca_Rinocer.zona_Rinocer()
    
    return ret
    
@app.route("/Rinocer/clasificare", methods=['GET'])
def ia_clasificare_Rinocer():
    ret = ""
    ret += librarie.biblioteca_Rinocer.clasificare_Rinocer()
    
    return ret
    
@app.route("/African/", methods=['GET'])
def get_African():
    ret = "<h1>African<h1>"
    ret += "specie: "
    ret += librarie.biblioteca_Rinocer.specie_African()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_Rinocer.zona_African()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_Rinocer.clasificare_African()
    ret += "<br>"
    
    return ret
    
@app.route("/African/specie", methods=['GET'])
def ia_specie_African():
    ret = ""
    ret += librarie.biblioteca_Rinocer.specie_African()
    
    return ret
    
@app.route("/African/zona", methods=['GET'])
def ia_zona_African():
    ret = ""
    ret += librarie.biblioteca_Rinocer.zona_African()
    
    return ret
    
@app.route("/African/clasificare", methods=['GET'])
def ia_clasificare_African():
    ret = ""
    ret += librarie.biblioteca_Rinocer.clasificare_African()
    
    return ret

app.run(host="127.0.0.1", port=5001)
