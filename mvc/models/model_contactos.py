import os
from supabase import create_client, Client
from dotenv import load_dotenv
import hashlib
import hmac
from typing import Any, cast
import logging


load_dotenv()

logger = logging.getLogger(__name__)


class ModelContactos:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
            )
            self.SECRET_KEY = b"hola"
        except Exception as error:
            print(f"ERROR 100: {str(error)}")

    def obtenerContactos(self):
        try:
            response = self.supabase.table("contactos").select("*").execute()
            return response.data
        except Exception as error:
            print(f"ERROR 106: {str(error)}")
            return ""

    def buscarContactos(self, id_contactos: int):
        try:
            response = self.supabase.table("contactos").select("*").eq("id", id_contactos).execute()
            return response.data
        except Exception as error:
            logger.error("ERROR 102: %s", error)
            print(f"ERROR 102: {str(error)}")
            return []

    def insertarContactos(self, nombre: str, email: str, telefono: str,foto: str ):
        try:
            response = self.supabase.table("contactos").insert({"nombre": nombre, "email": email, "telefono": telefono,"foto": foto}).execute()
            return response.data
        except Exception as error:
            logger.error("ERROR 103: %s", error)
            print(f"ERROR 103: {str(error)}")

    def borrarContactos(self, id_contactos: int):
        try:
            response = self.supabase.table("contactos").delete().eq("id", id_contactos).execute()
            return response.data
        except Exception as error:
            logger.error("ERROR 104: %s", error)
            print(f"ERROR 104: {str(error)}")

    def actualizarContactos(self, id_contactos: int, nombre: str, email: str, telefono: str,foto: str):
        try:

            response = self.supabase.table("contactos").update({"nombre": nombre, "email": email, "telefono": telefono,"foto": foto}).eq("id", id_contactos).execute()
            return response.data
        except Exception as error:
            logger.error("ERROR 105: %s", error)
            print(f"ERROR 105: {str(error)}")


if __name__ == "__main__":
    model_contactos = ModelContactos()  # Crea una instancia
    print(model_contactos.obtenerContactos())
    print(model_contactos.buscarContactos(2))
    print(model_contactos.insertarContactos("Carthoris", "carthoris@gmail", "333333","foto.png"))
    print(model_contactos.borrarContactos(4))
    print(model_contactos.actualizarContactos(5, "Juan", "juan@gmail", "8888888","foto.png"))