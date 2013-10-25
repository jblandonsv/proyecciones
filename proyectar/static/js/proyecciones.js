var controller = null;

$(document).ready(inicio);

function inicio()
{

    //Debería controlar exceptions de conexión con el socket
	controller = new Controlador();

	controller.image_id  = "#imagen_aca";
	controller.label_id  = "#label_aca";
	controller.image_width = 500;
	controller.image_height = 500;

	controller.canal_socket = "socketproyecciones";

	controller.iniciarSocket(controller);

}