from flask import Flask

import librarie.biblioteca_foca


app = Flask(__name__)

print('442D_foca')

@app.route("/" , methods=['GET'])
def index():
    ret = "<h1></h1>Informatii despre foca 442D</h1>"
    return ret

@app.route("/foca/", methods=['GET'])
def get_foca():
    ret = "<h1>foca<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_foca.specie_foca()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_foca.zona_foca()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_foca.clasificare_foca()
    ret += "<br>"
    
    return ret
    
@app.route("/foca/specie", methods=['GET'])
def ia_specie_foca():
    ret = ""
    ret += librarie.biblioteca_foca.specie_foca()
    
    return ret
    
@app.route("/foca/zona", methods=['GET'])
def ia_zona_foca():
    ret = ""
    ret += librarie.biblioteca_foca.zona_foca()
    
    return ret
    
@app.route("/foca/clasificare", methods=['GET'])
def ia_clasificare_foca():
    ret = ""
    ret += librarie.biblioteca_foca.clasificare_foca()
    
    return ret
    
@app.route("/polara/", methods=['GET'])
def get_polara():
    ret = "<h1>polara<h1>"
    ret += "specie: "
    ret += librarie.biblioteca_foca.specie_polara()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_foca.zona_polara()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_foca.clasificare_polara()
    ret += "<br>"
    
    return ret
    
@app.route("/polara/specie", methods=['GET'])
def ia_specie_polara():
    ret = ""
    ret += librarie.biblioteca_foca.specie_polara()
    
    return ret
    
@app.route("/polara/zona", methods=['GET'])
def ia_zona_polara():
    ret = ""
    ret += librarie.biblioteca_foca.zona_polara()
    
    return ret
    
@app.route("/polara/clasificare", methods=['GET'])
def ia_clasificare_polara():
    ret = ""
    ret += librarie.biblioteca_foca.clasificare_polara()
    
    return ret
    
    
app.run(host = "127.0.0.1", port = 5001)
