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
      self.curseur.execute("SELECT * FROM messages;")
      rows=self.curseur.fetchall()
      self.curseur.close()
      return rows

   """ methodes to select message depending user """
   def one_message(self,author):
      self.curseur=self.con.cursor()
      self.curseur.execute("SELECT * FROM messages WHERE auteur='"+author+"'")
      rows=self.cur.fetchall()
      self.curseur.close()
      return rows

   """ methodes to insert message depending user """
   def insert_message(self,contenu,author):
      self.curseur=self.con.cursor()
      from datetime import date
      today = date.today()
      self.curseur.execute("INSERT INTO messages(contenu,date_publication,auteur) VALUES(%s,%s,%s);",(contenu,today,author))
      self.con.commit()
      self.curseur.close()
