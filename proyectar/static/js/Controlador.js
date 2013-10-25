//IMPORTANTE PARA ENVIAR DATOS AL WEBSOCKET
SockJS.prototype.send_json = function(data) {
  this.send(JSON.stringify(data));
};

function Controlador()
{
	this.puerto_socket = 9000;
	this.canal_socket = "";
	this.host_socket = "localhost";

	this.socket = null;

	this.mensaje = "";
	this.image_path = "";
	this.image_id = "";
	this.label_id = "";
	this.image_width = 150;
	this.image_height = 150;

	this.refresh = function()
	{
		$(this.image_id).attr('src',this.image_path);
		$(this.image_id).attr('width',this.image_width);
		$(this.image_id).attr('height',this.image_height);
		$(this.label_id).html(this.mensaje);
	}

}

Controlador.prototype.iniciarSocket = function(controlador)
{
	this.socket = new SockJS('http://'+this.host_socket+':'+this.puerto_socket+'/'+this.canal_socket);
	console.log("Se creó la conexión :D");
	console.log(this.socket);

	//Eventos del Socket Client

	this.socket.onopen = function(){
		//validando conexión
		if(this.socket.readyState !== SockJS.OPEN)
		{
			console.log("No hay conexión con el Socket :( ");
		}else{
			console.log("Here we go !!");
			//callback(this.socket);
		}
	}

	this.socket.onclose = function()
	{
		console.log("socket cerrado");
	}

	this.socket.onmessage = function(e)
	{
		controlador.mensaje = e.data.mensaje;
		controlador.image_path = e.data.image_path;
		controlador.refresh();
	}

}

Controlador.prototype.enviarDatos = function()
{
	this.socket.send_json({
		mensaje:this.mensaje,
		image_path:this.image_path
	});
}

Controlador.prototype.test = function()
{
	alert("mensaje = " + this.mensaje + " imagen = " + this.image_path);
}

Controlador.prototype.refresh = function()
{
	$(this.image_id).attr('src',this.image_path);
	$(this.image_id).attr('width',this.image_width);
	$(this.image_id).attr('height',this.image_height);
	$(this.label_id).html(this.mensaje);
}