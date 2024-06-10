from flask import Flask
from tournois_routes import tournois_bp
from joueur_routes import joueur_bp
from equipe_route import equipe_bp
from calcule_routes import calcule_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(joueur_bp, url_prefix='/api/joueur')
app.register_blueprint(tournois_bp, url_prefix='/api/tournois')
app.register_blueprint(equipe_bp, url_prefix='/api/equipe')
app.register_blueprint(calcule_bp, url_prefix='/api/calcule')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
