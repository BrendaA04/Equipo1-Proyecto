# cerrar.py

def logout(usuario):
    print(f"👋 {usuario}, tu sesión se ha cerrado correctamente.")

if __name__ == "__main__":
    # Ejemplo de uso:
    usuario = "admin"  # normalmente vendría de la sesión activa
    logout(usuario)
