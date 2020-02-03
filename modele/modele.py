import psycopg2
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
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
      self.curseur.execute("SELECT u.name,u.firstname,m.contenu,m.date_publication FROM users AS u JOIN messages AS m ON u.id=m.id_auteur;")
      rows=self.curseur.fetchall()
      self.curseur.close()
      return rows

   """ methodes to insert message depending user """

   def insert_message(self,contenu,email):
      self.curseur=self.con.cursor()
      from datetime import date
      today = date.today()
      self.curseur.execute("SELECT id FROM users WHERE email=%s;",(email,))
      id_auteur=self.curseur.fetchone()[0]
      self.curseur.execute("INSERT INTO messages(contenu,date_publication,id_auteur) VALUES(%s,%s,%s);",(contenu,today,id_auteur))
      self.con.commit()
      self.curseur.close()
      
   """ authentification of user """

   def authentification(self,email,password):
      emira=False
      decrypted=""
      password_provided = "password" # This is input in the form of a string
      pwc = password_provided.encode() # Convert to type bytes
      salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
      kdf = PBKDF2HMAC(
         algorithm=hashes.SHA256(),
         length=32,
         salt=salt,
         iterations=100000,
         backend=default_backend()
      )
      key = base64.urlsafe_b64encode(kdf.derive(pwc)) # Can only use kdf once
      self.curseur=self.con.cursor()
      self.curseur.execute("select email,password from users")
      rows=self.curseur.fetchall()
      for row in rows:
         f = Fernet(key)
         decrypted = f.decrypt(row[1].encode())
         if row[0]==email and decrypted.decode("utf-8")==password:
            emira=True
            break
      self.curseur.close()
      return emira

   """ create count """

   def creation_count(self,name,firstname,pseudo,email,age,password):
      password_provided = "password" # This is input in the form of a string
      pwc = password_provided.encode() # Convert to type bytes
      salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
      kdf = PBKDF2HMAC(
         algorithm=hashes.SHA256(),
         length=32,
         salt=salt,
         iterations=100000,
         backend=default_backend()
      )
      key = base64.urlsafe_b64encode(kdf.derive(pwc)) # Can only use kdf once
      password = password.encode()
      f = Fernet(key)
      encrypted = f.encrypt(password)
      password = encrypted.decode("utf-8")
      self.curseur = self.con.cursor()
      self.curseur.execute("INSERT INTO users(name,firstname,pseudo,email,age,password) VALUES(%s,%s,%s,%s,%s,%s);",(name,firstname,pseudo,email,age,password))
      self.con.commit()
      self.curseur.close()

