import psycopg2
class ConnectToBdd:

   def __init__(self,bdd="ecole",user="postgres",password="as122014",host="localhost",port="5432"):
      try:
         self.con=psycopg2.connect(database=bdd,user=user,password=password,host=host,port=port)
         self.curseur=None
      except(Exception ,psycopg2.Error):
         print("erreur while connecting to postgresSQL")

   
   """ methodes  to select all of data from messages """
   def all_messages(self):
      self.curseur=self.con.cursor()
      self.curseur.execute("select u.name,u.firstname,m.contenu,m.date_publication from users as u join messages as m on u.id=m.id_auteur;")
      rows=self.curseur.fetchall()
      self.curseur.close()
      return rows

   """ methodes to select message depending user """
   def one_message(self,author):
      self.curseur=self.con.cursor()
      self.curseur.execute("SELECT * FROM messages WHERE auteur='"+author+"';")
      rows=self.curseur.fetchall()
      self.curseur.close()
      return rows

   """ methodes to insert message depending user """
   def insert_message(self,contenu,email,password):
      self.curseur=self.con.cursor()
      from datetime import date
      today = date.today()
      self.curseur.execute("SELECT id FROM users where email='"+email+"' and password="+"'"+password+"';")
      id_auteur=self.curseur.fetchone()[0]
      self.curseur.execute("INSERT INTO messages(contenu,date_publication,id_auteur) VALUES(%s,%s,%s);",(contenu,today,id_auteur))
      self.con.commit()
      self.curseur.close()
      
   """ authentification of user """
   def authentification(self,email,password):
      self.curseur=self.con.cursor()
      self.curseur.execute("select emira(%s,%s)",(email,password))
      emira=self.curseur.fetchone()
      self.curseur.close()
      return emira[0]
   def creation_count(self,name,firstname,pseudo,email,age,password):
      self.curseur=self.con.cursor()
      self.curseur.execute("INSERT INTO users(name,firstname,email,age,password) VALUES(%s,%s,%s,%s,%s);",(name,firstname,pseudo,age,password))
      self.con.commit()
      self.curseur.close()

