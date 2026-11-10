import web 
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class BorrarContactos:

    def GET(self,id_contacto):

        model_contactos = ModelContactos()  

        #Almacena en los datos los registros recibidos de Supabase 
        datos = model_contactos.borrarContactos(int(id_contacto))

        print(datos)

        #Envia los datos a contactos.html los datos de Supabase 
        return render.borrar_contactos(datos) #type: ignore