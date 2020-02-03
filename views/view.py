
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
            self.model.insert_message(input("what is in your mind: "),email)
        else:
            print("votre compte n'exsite pas il faut creer un compte pour pouvoir poster message")
    
    """ option get """
    def get_message_view(self):
        print(" voici la liste des post et de leurs auteur: ")
        for r in self.model.all_messages():
            print(View.HEADER + "-----------------------------------------------------------------------------------------" )
            print(f"nom: {r[0]} | prenom: {r[1]} | contenu: {r[2]} | date: {r[3]}")
            print(View.BOLD+ "----------------------------------------------------------------------------------------" )
    """ create new count """
    def creation_new_user(self):
        print("bienvenue entrez les champs ci-dessous")
        name=input("name: ")
        firstname=input("firstname: ")
        pseudo=input("pseudo: ")
        email=input("email: ")
        age=input("age: ")
        password=input("password: ")
        try:
            self.model.creation_count(name,firstname,pseudo,email,age,password)
        except(Exception ,psycopg2.Error):
            print("erreur while connecting to postgresSQL")



    