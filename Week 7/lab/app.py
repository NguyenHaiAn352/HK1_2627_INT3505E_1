# import connexion

# app = connexion.FlaskApp(__name__)
# app.add_api("labapi.yaml", validate_responses=False)

import connexion

app = connexion.App(__name__)

app.add_api("labapi.yaml")

if __name__ == "__main__":
    app.run()