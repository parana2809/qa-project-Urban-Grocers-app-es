import configuration
import data
import requests

# Crear un nuevo usuario
def post_create_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json= body,
                         headers= data.headers)

# Crear un kit
def post_new_client_kit (kit_body, auth_token):
    current_headers = data.headers.copy()
    current_headers ["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=current_headers)