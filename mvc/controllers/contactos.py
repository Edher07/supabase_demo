import web 
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class Contactos:

    def GET(self):

        model_contactos = ModelContactos()  

        #Almacena en los datos los registros recibidos de Supabase 
        datos = model_contactos.obtenerContactos()

        print(datos)

        #Envia los datos a contactos.html los datos de Supabase 
        return render.contactos(datos) #type: ignore
        

