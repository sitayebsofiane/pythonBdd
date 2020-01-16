from modele.modele import  *
from views.view import  *
from controllers.controller import  *

if __name__ == "__main__":

    model=ConnectToBdd()
    view=View(model)
    controller=Controller(model,view)

    controller.begin()
    controller.dispatcher()
