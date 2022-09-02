
new_user = {}
users = []

def validate_user(usuario):
    unique = True
    for user in users:
        if usuario == user['user']:
            unique = False
    return unique

def register(user, psw):
    new_user ={}
    new_user['user']= user
    new_user['password']= psw
    try:
        users.append(new_user)
        print('Tu usuario se ha registrado exitosamente!')
    except:
        print('Ho!.. Ha ocurrido un error al intentar registrarte...')



def login(usr, pws):
    for user in users:
        if  usr in user.values(): 
            if user['password'] == pws:
                print('Bienvenido', usr)
            else:
                print('Contraseña o usuario invalido!')



def main():
    menu = """
    1.- Registrarse
    2.- Iniciar sesion
    0.- salir

    """
    
    while True:
        option = input(menu)

        if option == '1':
            user = input('Ingresa tu usuario:  ')
            unique = validate_user(user)
            if unique:
                psw = input('Ingresa una contraseña segura:  ')
                register(user, psw)
            else:
                print('Usuario no disponible crea uno nuevo :( ')
        elif option == '2':
            user = input('Ingresa tu usuario:  ')
            psw = input('Ingresa tu contraseña:  ')
            login(user, psw)
        elif option == '0':
            print('Hasta pronto :)')
            break
        elif option > '2' or option < '0':
            print('Selecciona una opcion valida :(...')
def run():
    main()

if __name__ == '__main__':
    run()