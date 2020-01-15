from modele.connectToBdd import  *
from views.view import  *
from controllers.controller import  *



model=ConnectToBdd()
view=View(model)
controller=Controller(model,view)

controller.begin()
controller.dispatcher()
