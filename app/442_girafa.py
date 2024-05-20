from flask import Flask

import librarie.biblioteca_girafa


app = Flask(__name__)

print('442D_girafa')

@app.route("/" , methods=['GET'])
def index():
    ret = "<h1></h1>Informatii despre girafai 442D</h1>"
    return ret

@app.route("/girafa/", methods=['GET'])
def get_girafa():
    ret = "<h1>girafa<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_girafa.specie_girafa()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_girafa.zona_girafa()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_girafa.clasificare_girafa()
    ret += "<br>"
    
    return ret
    
@app.route("/girafa/specie", methods=['GET'])
def ia_specie_girafa():
    ret = ""
    ret += librarie.biblioteca_girafa.specie_girafa()
    
    return ret
    
@app.route("/girafa/zona", methods=['GET'])
def ia_zona_girafa():
    ret = ""
    ret += librarie.biblioteca_girafa.zona_girafa()
    
    return ret
    
@app.route("/girafa/clasificare", methods=['GET'])
def ia_clasificare_girafa():
    ret = ""
    ret += librarie.biblioteca_girafa.clasificare_girafa()
    
    return ret
    
@app.route("/african/", methods=['GET'])
def get_african():
    ret = "<h1>african<h1>"
    ret += "specie: "
    ret += librarie.biblioteca_girafa.specie_african()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_girafa.zona_african()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_girafa.clasificare_african()
    ret += "<br>"
    
    return ret
    
@app.route("/african/specie", methods=['GET'])
def ia_specie_african():
    ret = ""
    ret += librarie.biblioteca_girafa.specie_african()
    
    return ret
    
@app.route("/african/zona", methods=['GET'])
def ia_zona_african():
    ret = ""
    ret += librarie.biblioteca_girafa.zona_african()
    
    return ret
    
@app.route("/african/clasificare", methods=['GET'])
def ia_clasificare_african():
    ret = ""
    ret += librarie.biblioteca_girafa.clasificare_african()
    
    return ret
    
    
app.run(host = "127.0.0.1", port = 5001)
