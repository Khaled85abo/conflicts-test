from flask import Flask
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


###detta är kärnan i flask / the endpoint/ funktionen som ska triggas när man kommer till URL:en /
##kallas routs - som är olika funktioner som korresponderar till olika adresser/URLer
@app.route("/")
def home():
    return "<p>Hello World</p>"

@app.route("/movies")
def movies():
    return "<p>Hello movies</p>"



#oaksofksgpdgakospgoksapgko