from flask import Flask

import librarie.biblioteca_delfin


app = Flask(__name__)

print('442D_delfin')

@app.route("/" , methods=['GET'])
def index():
    ret = "<h1></h1>Informatii despre delfini 442D</h1>"
    return ret

@app.route("/delfin/", methods=['GET'])
def get_delfin():
    ret = "<h1>delfin<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_delfin.specie_delfin()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_delfin.zona_delfin()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_delfin.clasificare_delfin()
    ret += "<br>"
    
    return ret
    
@app.route("/delfin/specie", methods=['GET'])
def ia_specie_delfin():
    ret = ""
    ret += librarie.biblioteca_delfin.specie_delfin()
    
    return ret
    
@app.route("/delfin/zona", methods=['GET'])
def ia_zona_delfin():
    ret = ""
    ret += librarie.biblioteca_delfin.zona_Baiji()
    
    return ret
    
@app.route("/delfin/clasificare", methods=['GET'])
def ia_clasificare_delfin():
    ret = ""
    ret += librarie.biblioteca_delfin.clasificare_delfin()
    
    return ret
    
@app.route("/Baiji/", methods=['GET'])
def get_Baiji():
    ret = "<h1>Baiji<h1>"
    ret += "specie: "
    ret += librarie.biblioteca_delfin.specie_Baiji()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_delfin.zona_Baiji()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_delfin.clasificare_Baiji()
    ret += "<br>"
    
    return ret
    
@app.route("/Baiji/specie", methods=['GET'])
def ia_specie_Baiji():
    ret = ""
    ret += librarie.biblioteca_delfin.specie_Baiji()
    
    return ret
    
@app.route("/Baiji/zona", methods=['GET'])
def ia_zona_Baiji():
    ret = ""
    ret += librarie.biblioteca_delfin.zona_Baiji()
    
    return ret
    
@app.route("/Baiji/clasificare", methods=['GET'])
def ia_clasificare_Baiji():
    ret = ""
    ret += librarie.biblioteca_delfin.clasificare_Baiji()
    
    return ret
    
    
app.run(host = "127.0.0.1", port = 5001)
