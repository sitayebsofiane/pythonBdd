
class Controller:

    def __init__(self,model,view):
       self.model=model
       self.view=view
       self.option=None

    """ header """
    def begin(self):
        self.option=self.view.options_for_the_user()
    
    """ dispatcher """
    def dispatcher(self):
        if self.option=="post":
            self.view.post_message_view()
        if self.option=="get":
            self.view.get_message_view()

        