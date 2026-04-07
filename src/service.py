# from src.storage import save_name

# def validate_name(name):
#     return isinstance(name, str) and len(name.strip()) >= 2

# def register_name(names, name):
#     if not validate_name(name):
#         raise ValueError("Nombre no válido")
#     return save_name(names, name)

#Codigo para error de test unitario
from src.storage import save_name

def validate_name(name):
    return True

def register_name(names, name):
    if not validate_name(name):
        raise ValueError("Nombre no válido")
    return save_name(names, name)