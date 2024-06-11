from flask import Flask
from flask_cors import CORS
from route_joueur import personnes_bp
from route_tournoi import tournois_bp

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(personnes_bp, url_prefix='/api/personnes', name='personnes_bp')
app.register_blueprint(tournois_bp, url_prefix='/api/tournois', name='tournois_bp')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
