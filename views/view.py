
class View:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    def __init__(self,model):
        self.model=model

    """ methode display options for the user """
    def options_for_the_user(self):
        print("veulliez choisir une option 'post' || 'get' :")
        print("post: pour poster un message")
        print("get: pour obtenir un message")
        return input()
    
    """ option post """
    def post_message_view(self,email,password):
        if self.model.authentification(email,password):
            self.model.insert_message(input("what is in your mind: "),email,password)
        else:
            print("ton emira n'est pas valide il faut creer un compte pour pouvoir poster message")
    
    """ option get """
    def get_message_view(self):
        print("salam alikoum voici la liste: ")
        for r in self.model.all_messages():
            print(View.OKGREEN + "-----------------------------------------------------------------------------------------" )
            print(f"nom: {r[0]} | prenom: {r[1]} | contenu: {r[2]} | date: {r[3]}")
            print(View.UNDERLINE+ "----------------------------------------------------------------------------------------" )
    def creation_new_user(self):
        #name,firstname,pseudo,email,age,password
        pass



    