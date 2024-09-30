from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth

anagrafe = []

api = Flask(__name__)
auth = HTTPBasicAuth()

# Dati di esempio autenticazione
users = {
    "lettura": {"password": "password_lettura", "role": "read"},
    "scrittura": {"password": "password_scrittura", "role": "write"},
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username]['password'] == password:
        return username  # Ritorna l'username se l'autenticazione è andata a buon fine
    return None

def get_user_role(username):
    return users[username]["role"]

# Metodo POST per inserire una nuova anagrafe
@api.route('/post_anagrafe', methods=['POST'])
@auth.login_required
def post_anagrafe():
    username = auth.current_user()
    if get_user_role(username) != "write":
        return jsonify({"Errore": "Non hai permessi per scrivere dati"}), 403
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json_data = request.json
        anagrafe.append(json_data)  # Aggiunge il dato alla lista creata all'inizio
        response = {"Esito": "ok", "Msg": "Dato inserito"}
        return jsonify(response), 201
    else:
        return 'Content-Type not supported!', 400

# Metodo GET per ottenere tutti i dati dell'anagrafe
@api.route('/get_anagrafe', methods=['GET'])
@auth.login_required
def get_anagrafe():
    username = auth.current_user()
    if get_user_role(username) != "read":
        return jsonify({"Errore": "Non hai permessi per leggere dati"}), 403 
    try:
        return jsonify(anagrafe), 200  # Status code 200 (OK)
    except Exception as e:
        return jsonify({"Esito": "errore", "Msg": str(e)}), 500  # Status code 500 (Internal Server Error)

# Metodo PUT per aggiornare un record nell'anagrafe (per esempio in base al codice fiscale)
@api.route('/put_anagrafe/<cf>', methods=['PUT'])
@auth.login_required
def update_anagrafe(cf):
    username = auth.current_user()
    if get_user_role(username) != "write":
        return jsonify({"Errore": "Non hai permessi per modificare dati"}), 403
    
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json_data = request.json
        for record in anagrafe:
            if record.get("cf") == cf:
                record.update(json_data)
                response = {"Esito": "ok", "Msg": "Dato aggiornato"}
                return jsonify(response), 200  # Status code 200 (OK)
        return jsonify({"Esito": "errore", "Msg": "cf non trovato"}), 404  # Status code 404 (Not Found)
    else:
        return 'Content-Type not supported!', 400

# Metodo DELETE per cancellare un record dall'anagrafe (per esempio in base al codice fiscale)
@api.route('/delete_anagrafe/<cf>', methods=['DELETE'])
@auth.login_required
def delete_anagrafe(cf):
    username = auth.current_user()
    if get_user_role(username) != "write":
        return jsonify({"Errore": "Non hai permessi per eliminare dati"}), 403
    for record in anagrafe:
        if record.get("cf") == cf:
            anagrafe.remove(record)
            response = {"Esito": "ok", "Msg": "Dato eliminato"}
            return jsonify(response), 200
    return jsonify({"Esito": "errore", "Msg": "cf non trovato"}), 404

# Avvio dell'app Flask senza SSL
if __name__ == "__main__":
    api.run(host="127.0.0.1", port=8080, ssl_context='adhoc')