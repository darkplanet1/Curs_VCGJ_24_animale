from flask import Flask

import librarie.biblioteca_vulpe


app = Flask(__name__)

print('442D_vulpe')

@app.route("/" , methods=['GET'])
def index():
    ret = "<h1></h1>Informatii despre vulpi 442D</h1>"
    return ret

@app.route("/vulpe_rosie/", methods=['GET'])
def get_vulpe_rosie():
    ret = "<h1>vulpe_rosie<h1>"
    ret += "Specie: "
    ret += librarie.biblioteca_vulpe.specie_vulpe_rosie()
    ret += "<br>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_vulpe.zona_vulpe_rosie()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_vulpe.clasificare_vulpe_rosie()
    ret += "<br>"
    
    return ret
    
@app.route("/vulpe_rosie/specie", methods=['GET'])
def ia_specie_vulpe_rosie():
    ret = ""
    ret += librarie.biblioteca_vulpe.specie_vulpe_rosie()
    
    return ret
    
@app.route("/vulpe_rosie/zona", methods=['GET'])
def ia_zona_vulpe_rosie():
    ret = ""
    ret += librarie.biblioteca_vulpe.zona_vulpe_rosie()
    
    return ret
    
@app.route("/vulpe_rosie/clasificare", methods=['GET'])
def ia_clasificare_vulpe_rosie():
    ret = ""
    ret += librarie.biblioteca_vulpe.clasificare_vulpe_rosie()
    
    return ret
    
@app.route("/vulpe_polara/", methods=['GET'])
def get_vulpe_polara():
    ret = "<h1>vulpe_polara<h1>"
    ret += "specie: "
    ret += librarie.biblioteca_vulpe.specie_vulpe_polara()
    ret += "<br>"
    
    ret += "zona: "
    ret += librarie.biblioteca_vulpe.zona_vulpe_polara()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_vulpe.clasificare_vulpe_polara()
    ret += "<br>"
    
    return ret
    
@app.route("/vulpe_polara/specie", methods=['GET'])
def ia_specie_vulpe_polara():
    ret = ""
    ret += librarie.biblioteca_vulpe.specie_vulpe_polara()
    
    return ret
    
@app.route("/vulpe_polara/zona", methods=['GET'])
def ia_zona_vulpe_polara():
    ret = ""
    ret += librarie.biblioteca_vulpe.zona_vulpe_polara()
    
    return ret
    
@app.route("/vulpe_polara/clasificare", methods=['GET'])
def ia_clasificare_vulpe_polara():
    ret = ""
    ret += librarie.biblioteca_vulpe.clasificare_vulpe_polara()
    
    return ret
    
    
app.run(host = "127.0.0.1", port = 5001)
