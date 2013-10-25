var controller = null;

$(document).ready(inicio);

function inicio()
{

    //Debería controlar exceptions de conexión con el socket
	controller = new Controlador();

	controller.canal_socket = "socketproyecciones";

	controller.iniciarSocket(controller);
	//

	$('#slides_disponibles article button').on('click',obtenerValores);

}

function obtenerValores()
{
	var currentTarget = $(this).context.parentElement;
	controller.mensaje = currentTarget.getElementsByClassName('mensaje_form')[0].value; // Mensaje (se permiten valores nulos)
	controller.image_path = currentTarget.getElementsByTagName('img')[0].getAttribute('src'); //url imagen
	controller.enviarDatos();
}