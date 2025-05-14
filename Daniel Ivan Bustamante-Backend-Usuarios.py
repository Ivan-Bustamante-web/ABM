#Definimos la lista de usuarios
users = []

#Aqui definimos la funcion donde se dan de alta los usuarios
def new_user(name, email):
    user = {
        'id': len(users) + 1,
        'name': name,
        'email': email
    }
    users.append(user)
    print("Usuario agregado.")

#Aqui definimos la funcion donde se dan las modificaciones de los usuarios
def mod_user(id_user, new_name=None, new_email=None):
    for user in users:
        if user['id'] == id_user:
            if new_name:
                user['name'] = new_name
            if new_email:
                user['email'] = new_email
            print("Usuario modificado.")
            return
    print("Usuario no encontrado.")

#Esta funcion nos permite eliminar usuarios
def del_user(id_user):
    global users
    users = [u for u in users if u['id'] != id_user]
    print("Usuario eliminado.")

#Y esta lista a los usuarios creados/modificados hasta el momento
def ls_users():
    if not users:
        print("No hay users.")
    else:
        for user in users:
            print(user)

#Aqui creamos una pequeña interfaz tipo menu para que el usuario puedsa interactuar de mejor manera con el programa
def menu():
    while True:
        print("\nMenú de usuario")
        print("1. Alta")
        print("2. Modificar")
        print("3. Eliminar")
        print("4. Listar")
        print("5. Salir")
        opc = input("Opción: ")

#Listamos todas las opciones
        if opc == "1":
            name = input("Nombre: ")
            email = input("Email: ")
            new_user(name, email)

        elif opc == "2":
            try:
                id_user = int(input("ID a modificar: "))
                new_name = input("Nuevo nombre (enter para dejar igual): ")
                new_email = input("Nuevo email (enter para dejar igual): ")
                mod_user(
                    id_user,
                    new_name if new_name else None,
                    new_email if new_email else None
                )
            except ValueError:
                print("ID inválido.")

        elif opc == "3":
            try:
                id_user = int(input("ID a eliminar: "))
                del_user(id_user)
            except ValueError:
                print("ID inválido.")

        elif opc == "4":
            ls_users()

        elif opc == "5":
            break

        else:
            print("Opción inválida.")

#El comando que permite que ejecutemos el programa
menu()