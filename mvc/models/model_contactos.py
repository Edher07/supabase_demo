import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class ModelContactos:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
            )
        except Exception as error:
            print(f"ERROR 100:{error.args[0]}")

    def obtenerContactos(self):
        # SELECT * FROM contactos;
        response = self.supabase.table("contactos").select("*").execute()
        return response.data

    def buscarContactos(self, id_contactos: int):
        # SELECT * FROM contactos WHERE id_contacto = <id>;
        response = self.supabase.table("contactos").select("*").eq("id_contactos", id_contactos).execute()
        return response.data

    def insertarContactos(self, id_contactos: int):
        # SELECT * FROM contactos WHERE id_contacto = <id>;
        response = self.supabase.table("contactos").select("*").eq("id_contactos", id_contactos).execute()
        return response.data

    def borrarContactos(self, id_contactos: int):
        # SELECT * FROM contactos WHERE id_contacto = <id>;
        response = self.supabase.table("contactos").select("*").eq("id_contactos", id_contactos).execute()
        return response.data

    def actualizarContactos(self, id_contactos: int):
        # SELECT * FROM contactos WHERE id_contacto = <id>;
        response = self.supabase.table("contactos").select("*").eq("id_contactos", id_contactos).execute()
        return response.data

if __name__ == "__main__":
    model_contactos = ModelContactos()  # Crea una instancia
    print(model_contactos.obtenerContactos())
    print(model_contactos.buscarContactos())
    print(model_contactos.insertarContactos())
    print(model_contactos.borrarContactos())
    print(model_contactos.actualizarContactos())
