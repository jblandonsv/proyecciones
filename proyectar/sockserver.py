import json
from sockjs.tornado import SockJSConnection
from proyectar.models import Presentacion, Slides

class ProyeccionConnection(SockJSConnection):
	_connected = set()

	def on_open(self,request):
		print "CONECTADO"
		self._connected.add(self)

	def on_message(self,datos):
		datos = json.loads(datos)
		print repr(datos)
		self.broadcast(self._connected,self._enviando_datos(datos))

	def on_close(self):
		print "CONEXION CERRADA"
		self._connected.remove(self)

	def _enviando_datos(self,parametros):
		mensaje = parametros['mensaje']
		image_path = parametros['image_path']
		return {'mensaje':mensaje,'image_path':image_path}