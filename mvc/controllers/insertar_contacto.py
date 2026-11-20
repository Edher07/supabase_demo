import os
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
        formulario = web.input(foto={}) #Recibir el archivo.
        #Obtiene el valor del input nombre
        nombre = formulario['nombre']
        #Obtiene el valor del input email
        email = formulario['email']
        #Obtiene el valor del input telefono
        telefono = formulario['telefono']

        archivo = formulario['foto'] #Accede al archivo subido
        foto = archivo.filename #Obtiene el nombre del archivo

        ruta = os.path.join("static/fotos/", foto) #Crea la ruta para guardar el archivo
        with open(ruta, "wb") as file: #Abre el archivo en modo escritura binaria
            file.write(formulario.foto.file.read()) #Escribe el contenido del archivo en la ruta especificada

        #Imprime los datos para verificar que se obtiene los valores
        #de forma correcta
        print(f"Nombre: {nombre}"), 
        print(f"Email: {email}"), 
        print(f"Teléfono: {telefono}")

        contenido_bytes = archivo.file.read()
        



        model_contactos = ModelContactos()

        datos = model_contactos.insertarContactos(nombre, email, telefono,foto)

        if not datos:
            return """
            <h1>No se pudo guardar el contacto.</h1>
            <p>Revisa los datos y los errores registrados en app.log o en la consola.</p>
            <a href="/insertar_contacto">Intentar de nuevo</a>
            """

        html = """
        <h1>Contacto almacenado correctamente</h1>
        <a href = "/contactos">Regresar</a>
        """
        return html





