from flask import Flask, render_template, request

api = Flask("__name__")

utenti=[["mariorossi@gmail.com", "MRORSI02M05H501Y", "pippo"], ["giuliogallo@gmail.com", "GLIGLL02G09H501T", "topolino"], ["marcodibello@gmail.com","MRCDBL02G09H501T", "minnie"]]
utente = []

    
@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/registrati', methods=['GET'])
def registrazioni():
    utente.append(request.args.get("email"))
    utente.append(request.args.get("codice_fiscale"))
    utente.append(request.args.get("password"))
    if utente in utenti:
        return render_template('regok.html')
    else:
        return render_template('regko.html')


api.run(host="0.0.0.0", port=8085)