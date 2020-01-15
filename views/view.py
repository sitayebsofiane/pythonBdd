
class View:

    def __init__(self,model):
        self.model=model

    """ methode display options for the user """
    def options_for_the_user(self):
        print("veulliez choisir une option 'post' || 'get' :")
        print("post: pour poster un message")
        print("get: pour obtenir un message")
        return input()
    
    """ option post """
    def post_message_view(self):
        contenu=input("what is in your mind: ")
        author=input("what is your name: ")
        self.model.insert_message(contenu,author)
    
    """ option get """
    def get_message_view(self):
        print("salam alikoum voici la liste: ")
        for r in self.model.all_messages():
            print(f"message: {r[1]} date: {r[2]} auteur: {r[3]}")



    