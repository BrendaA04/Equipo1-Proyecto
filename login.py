# index.py

# Diccionario de usuarios de prueba (usuario: contraseña)
usuarios = {
    "admin": "1234",
    "juan": "abcd",
    "maria": "qwerty"
}

def login():
    print("=== LOGIN ===")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario in usuarios and usuarios[usuario] == contraseña:
        print(f"✅ Bienvenido {usuario}, has iniciado sesión correctamente.")
    else:
        print("❌ Usuario o contraseña incorrectos.")

if __name__ == "__main__":
    login()
