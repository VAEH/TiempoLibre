import discord
import os
import requests 
import json
import random 
#Utiliza la base de datos de replit
from replit import db
from keep_alive import keep_alive


client = discord.Client()

sad_words = ["sad","depressed", "unhappy", "angry", "miserable", "depressing", "suicidacion"]

started_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "Yu are a great person / bot!"]

#Creamos una nueva clave en la bd llamada "responding"
#Para determinar si el bot responde a palabras tristes
if "responding" not in db.keys():
  db["responding"] = True

#Obtiene frases motivacionales de una APi
def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  #Convertiremos esa respuesta en json
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

#La función acepta un mensaje alentador como argumento
def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

#Fnción elimina mensaje de aliento
def delete_encouragements(index):
  #Obtuvimos la lista encouragement de laBD
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements
@client.event


async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#Evento por si recibe un mensaje directamente en el
#Servidot de Discord

@client.event

#Nombre de las funciones son de la Api de discord
#Se activa cada que recibe un mensaje
async def on_message(message):
  #Comprueba si el mensaje es de nosotros
  if message.author == client.user:
    return
  #Se abrevia el nombre de la variable ya que se a a utilizar mucho 
  msg = message.content

  #Va a responder 'Hello' cada que alguien escriba
  #'$hello'
  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    #Nueva variable
    #Estamos haciendo una copia de "started_encouragements"
    options = started_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]
    
    #Verifica si os mensajes contienen alguna palabra de 'sad_words'
    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))
  #Agregar un nuevo mensaje
  if msg.startswith('$new'):
    #Separa el mensaje del comando "$new "
    encouraging_message = msg.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  #Verifica si un nuevo mensaje comienza con "$del"
  if msg.startswith("$del"):
    encouragements = [] #Matriz vacia
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_encouragements(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  #Envia la lista como un mensaje de Discord
  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]
    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

keep_alive()
client.run(os.getenv('TOKEN')) 