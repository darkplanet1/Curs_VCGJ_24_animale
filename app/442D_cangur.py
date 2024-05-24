from flask import Flask

import librarie.biblioteca_cangur


app = Flask(__name__)

print('442D_cangur')

@app.route("/" , methods=['GET'])
def index():
    ret = "<h1>Informatii despre cangur 442D</h1>"
    return ret

@app.route("/cangur/", methods=['GET'])
def get_cangur():
    ret = "<h1>cangur<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_cangur.specie_cangur()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_cangur.zona_cangur()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_cangur.clasificare_cangur()
    ret += "<br>"
    
    return ret
    
@app.route("/cangur/specie", methods=['GET'])
def ia_specie_cangur():
    ret = ""
    ret += librarie.biblioteca_cangur.specie_cangur()
    
    return ret
    
@app.route("/cangur/zona", methods=['GET'])
def ia_zona_cangur():
    ret = ""
    ret += librarie.biblioteca_cangur.zona_cangur()
    
    return ret
    
@app.route("/cangur/clasificare", methods=['GET'])
def ia_clasificare_cangur():
    ret = ""
    ret += librarie.biblioteca_cangur.clasificare_cangur()
    
    return ret
    
    
       
app.run(host = "127.0.0.1", port = 5001)
