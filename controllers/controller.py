
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
            print("befor to post message you have to connect with your password and mail or create au new compte")
            choice=input("typing on your keyboard cr to create or co to connect: ").lower()
            if choice=="co":
                self.view.post_message_view(input("enter your email: "),input("enter your password: "))
            if choice=="cr":
                self.view.creation_new_user()
        if self.option=="get":
            self.view.get_message_view()
   
    

        