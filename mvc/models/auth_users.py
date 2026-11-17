import os
from supabase import create_client, Client
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger(__name__)

class AuthUsers:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
            )
            self.SECRET_KEY = b"hola"
        except Exception as error:
            print(f"ERROR 100: {str(error)}")

    def iniciarSesion(self, email: str, password: str):
        try:
            response = self.supabase.auth.sign_in_with_password(
                 {
                    "email": email,
                "password": password
                }
            )
            #print(f"Inicio de sesión exitoso: {response.session.access_token}")
            return str(response.session.access_token) #type: ignore
        except Exception as error:
            logger.error("ERROR 102:{str(error)}")
            print(f"ERROR 102: {str(error)}")
            return None

    def registrarUsuario(self, email: str, password: str)->str:
        try:
            response = self.supabase.auth.sign_up(
                {
                    "email": email,
                    "password": password
                }
            )
            #print(f"Usuario registrado: {response.user.id}")
            return response.user.id #type: ignore
        except Exception as error:
            logger.error("ERROR 102:{str(error)}")
            print(f"ERROR 102: {str(error)}")
            return None

if __name__ == "__main__":
     print("Autencticación de usuarios")
     objeto = AuthUsers()
     #objeto.iniciarSesion("dejah@email.com", "12345678") #Contraseña valida
     #objeto.iniciarSesion("dejah@email.com", "12345678") #Contraseña no valida



     #objeto.registrarUsuario("john@email.com", "12345678") #Registro de usuario
