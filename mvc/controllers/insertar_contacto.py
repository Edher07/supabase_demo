import web 
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class InsertarContacto:

    #Renderiza el achivo insertar_contacto.html

    def GET(self):
        return render.insertar_contacto() #type: ignore

    #Recibe los input del formulario y accede a cada uno 
    #utilizando el atributo 'name'

    def POST(self):
        #Accede a los datos del formulario 'contactos'
        formulario = web.input()
        #Obtiene el valor del input nombre
        nombre = formulario.get['nombre']
        #Obtiene el valor del input email
        email = formulario.get['email']
        #Obtiene el valor del input telefono
        telefono = formulario.get['telefono']

        #Imprime los datos para verificar que se obtiene los valores
        #de forma correcta
        print(f"Nombre: {nombre}"), 
        print(f"Email: {email}"), 
        print(f"Teléfono: {telefono}")



        model_contactos = ModelContactos()

        datos = model_contactos.insertarContactos(nombre, email, telefono)

        #print(datos)

        html = """
        <h1>Contacto almacenado correctamente</h1>
        <a href = "/contactos">Regresar</a>
        """
        return html





