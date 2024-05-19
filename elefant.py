from flask import Flask, url_for




app = Flask(__name__)





@app.route("/", methods=['GET'])



def index():

	ret = "<h1> Elefanti </h1>"

	ret += f"<a href={url_for('elefant')}>Elefant -Dobre Ionut-Bogdan</a>"

	return ret



@app.route("/elefant", methods=['GET'])

def elefant():

	descriere = descriere_elefant()

	culoare = culoare_elefant()

	

	ret = "<h1>elefant</h1>"

	

	ret += f"<a href={url_for('index')}>[Flori]</a>"

	ret += f"<a href={url_for('descriere')}>[Descriere]</a>"

	ret += f"<a href={url_for('culoare')}>[Culoare]</a>"

	

	ret += "<h2>Descriere: </h2>"

	ret += descriere

	

	ret += "<h2>Culoare: </h2>"

	ret+= culoare

	

	return ret



@app.route("/elefant/descriere", methods=['GET'])

def descriere():



	descriere = descriere_elefant()

	

	ret = f"<a href={url_for('index')}>[Flori]</a>"

	ret += f"<a href={url_for('elefant')}>[elefant]</a>"

	ret += f"<a href={url_for('culoare')}>[Culoare]</a>"

	

	ret += "<h2>Descriere: </h2>"

	ret += descriere

	

	return ret

	

@app.route("/elefant/culoare", methods=['GET'])

def culoare():

	culoare = culoare_elefant()

		

	ret = f"<a href={url_for('index')}>[Flori]</a>"

	ret += f"<a href={url_for('elefant')}>[elefant]</a>"

	ret += f"<a href={url_for('descriere')}>[Descriere]</a>"

	ret += "<h2>Culoare: </h2>"

	ret += culoare

	return ret


if __name__ == '__main__':
        app.run()


