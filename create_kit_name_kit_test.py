import sender_stand_request
import data

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body ["name"] = name
    return current_kit_body

def get_new_user_token():
    user_body = data.user_body
    response = sender_stand_request.post_create_new_user(user_body)
    return response.json()["authToken"]

# Prueba positiva: Kit con nombre válido
def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

# Prueba negativa: Kit con nombre inválido
def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

# Casos de prueba

# El número permitido de caracteres (1)
def test1_create_kit_1_character_in_the_name():
    current_kit_body = get_kit_body(data.test1_kit_name)
    positive_assert(current_kit_body)

# El número permitido de caracteres (511)
def test2_create_kit_511_characters_in_the_name():
    current_kit_body = get_kit_body(data.test2_kit_name)
    positive_assert(current_kit_body)

# 	El número de caracteres es menor que la cantidad permitida
def test3_create_kit_empty_in_the_name():
    current_kit_body = get_kit_body(data.test3_kit_name)
    negative_assert_code_400(current_kit_body)

#	El número de caracteres es mayor que la cantidad permitida (512)
def test4_create_kit_512_characters_in_the_name():
    current_kit_body = get_kit_body(data.test4_kit_name)
    negative_assert_code_400(current_kit_body)

#	Se permiten caracteres especiales
def test5_create_kit_special_characters_in_the_name():
    current_kit_body = get_kit_body(data.test5_kit_name)
    positive_assert(current_kit_body)

#   Se permiten espacios
def test6_create_kit_with_spaces_in_the_name():
    current_kit_body = get_kit_body(data.test6_kit_name)
    positive_assert(current_kit_body)

# 	Se permiten números
def test7_create_kit_with_numbers_in_the_name():
    current_kit_body = get_kit_body(data.test7_kit_name)
    positive_assert(current_kit_body)

# 	El parámetro no se pasa en la solicitud
def test8_create_kit_missing_in_the_name():
    current_kit_body = data.kit_body.copy()
    current_kit_body.pop("name")
    negative_assert_code_400(current_kit_body)

# 	Se ha pasado un tipo de parámetro diferente (número)
def test9_create_kit_invalid_type_in_the_name():
    current_kit_body = get_kit_body(data.test9_kit_name)
    negative_assert_code_400(current_kit_body)