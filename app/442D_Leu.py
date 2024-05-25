from flask import Flask
import librarie.biblioteca_Leu

app = Flask(__name__)

print('442D_Leu')

@app.route("/", methods=['GET'])
def index():
    ret = "<h1>Informatii despre Leu 442D</h1>"
    return ret

@app.route("/Leu/", methods=['GET'])
def get_Leu():
    ret = "<h1>Leu<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_Leu.specie_Leu()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_Leu.zona_Leu()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_Leu.clasificare_Leu()
    ret += "<br>"
    
    return ret
    
@app.route("/Leu/specie", methods=['GET'])
def ia_specie_Leu():
    ret = ""
    ret += librarie.biblioteca_Leu.specie_Leu()
    
    return ret
    
@app.route("/Leu/zona", methods=['GET'])
def ia_zona_Leu():
    ret = ""
    ret += librarie.biblioteca_Leu.zona_Leu()
    
    return ret
    
@app.route("/Leu/clasificare", methods=['GET'])
def ia_clasificare_Leu():
    ret = ""
    ret += librarie.biblioteca_Leu.clasificare_Leu()
    
    return ret
    
@app.route("/American/", methods=['GET'])
def get_American():
    ret = "<h1>American<h1>"
    ret += "specie: "
    ret += librarie.biblioteca_Leu.specie_American()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_Leu.zona_American()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_Leu.clasificare_American()
    ret += "<br>"
    
    return ret
    
@app.route("/American/specie", methods=['GET'])
def ia_specie_American():
    ret = ""
    ret += librarie.biblioteca_Leu.specie_American()
    
    return ret
    
@app.route("/American/zona", methods=['GET'])
def ia_zona_American():
    ret = ""
    ret += librarie.biblioteca_Leu.zona_American()
    
    return ret
    
@app.route("/American/clasificare", methods=['GET'])
def ia_clasificare_American():
    ret = ""
    ret += librarie.biblioteca_Leu.clasificare_American()
    
    return ret

app.run(host="127.0.0.1", port=5001)
