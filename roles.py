# roles.py
# Diccionario de roles: user_id → rol
ROLES = {
    123456789: "admin",
    987654321: "profesional",
    555555555: "asistente"
}

def get_user_role(user_id):
    """
    Devuelve el rol del usuario según su ID.
    Si no está definido, devuelve 'profesional' por defecto.
    """
    return ROLES.get(user_id, "profesional")

