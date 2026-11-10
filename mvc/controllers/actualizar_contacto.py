import web 
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class ActualizarContacto:

    #Renderiza el achivo actualizar_contacto.html

    def GET(self,id_contacto):
        model_contactos = ModelContactos()
        contacto = model_contactos.buscarContactos(int(id_contacto))
        return render.actualizar_contacto(contacto) #type: ignore

    #Recibe los input del formulario y accede a cada uno 
    #utilizando el atributo 'name'

    def POST(self,id_contacto):
        #Accede a los datos del formulario 'contactos'
        formulario = web.input()
        #Obtiene el valor del input nombre
        nombre = formulario['nombre']
        #Obtiene el valor del input email
        email = formulario['email']
        #Obtiene el valor del input telefono
        telefono = formulario['telefono']

        #Imprime los datos para verificar que se obtiene los valores
        #de forma correcta
        print(f"Nombre: {nombre}"), 
        print(f"Email: {email}"), 
        print(f"Teléfono: {telefono}")

        model_contactos = ModelContactos()

        datos = model_contactos.actualizarContactos(int(id_contacto), nombre, email, telefono)

        #print(datos)

        html = """
        <h1>Contacto actualizado correctamente</h1>
        <a href = "/contactos">Regresar</a>
        """
        return html