import os
from flask import Flask

app = Flask(__name__)

# Variables d'environnement, chacune avec une valeur par défaut
MESSAGE = os.environ.get("APP_MESSAGE", "Bonjour depuis Docker !")
PORT = int(os.environ.get("APP_PORT", "5000"))


@app.route("/")
def home():
    return MESSAGE + "\n"


if __name__ == "__main__":
    # 0.0.0.0 = écouter sur toutes les interfaces du conteneur (exigence E5)
    app.run(host="0.0.0.0", port=PORT)