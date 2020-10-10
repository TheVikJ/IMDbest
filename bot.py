import discord
import requests
import random
import json
import time

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

client = discord.Client()

urls = ['https://opentdb.com/api.php?amount=1&category=11',
        'https://opentdb.com/api.php?amount=1&category=32',
        'https://opentdb.com/api.php?amount=1&category=31']

@client.event
async def on_message(message):
       if message.author == client.user:
              return

       if message.content.startswith('!trivia'):
              global answer
              global type
              global question
              global r
              global answered
              answered = False
              url = random.choice(urls)
              r = requests.get(url).text
              question = json.loads(r).get('results')[0].get('question')
              answer = json.loads(r).get('results')[0].get('correct_answer')
              type = json.loads(r).get('results')[0].get('type')
              print(type)
              await message.channel.send(question)
              msg = [answer]
              for i in range(len(json.loads(r).get('results')[0].get('incorrect_answers'))):
                     msg.append(json.loads(r).get('results')[0].get('incorrect_answers')[i])
              msg.sort()
              for i in range(len(msg)):
                     await message.channel.send(msg[i])
       elif message.content.startswith('!answer'):
              u_ans = message.content.replace('!answer ', '')
              if u_ans.lower() == answer.lower() and answered == False:
                     await message.channel.send('Congratulations {0.author.mention}! That is the correct answer!'.format(message))
                     answered = True
       elif message.content.startswith('!imdb'):
              imdburl = "https://imdb8.p.rapidapi.com/title/auto-complete"
              qstring = {"q": message.content.replace('!imdb ','')}
              headers = {
                     'x-rapidapi-host': "imdb8.p.rapidapi.com",
                     'x-rapidapi-key': "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
              }
              response = requests.request("GET", imdburl, headers=headers, params=qstring).text
              cast = json.loads(response).get("d")[0].get('s')
              image = json.loads(response).get('d')[0].get('i').get('imageUrl')
              msg = image
              msg += '\n'
              msg += json.loads(response).get('d')[0].get('l')
              movieid = json.loads(response).get('d')[0].get('id')
              imdburl = 'https://imdb8.p.rapidapi.com/title/get-ratings'
              qstring = {"tconst": movieid}
              response = requests.request("GET", imdburl, headers=headers, params=qstring).text
              msg += '\nYear: '
              msg += str(json.loads(response).get('year'))
              msg += '\nRating: '
              msg += str(json.loads(response).get("rating"))
              msg += '\nTop Cast: '
              msg += cast
              await message.channel.send(msg)
       elif message.content.startswith('!rating'):
              imdburl = "https://imdb8.p.rapidapi.com/title/auto-complete"
              qstring = {"q": message.content.replace('!rating ', '')}
              headers = {
                     'x-rapidapi-host': "imdb8.p.rapidapi.com",
                     'x-rapidapi-key': "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
              }
              response = requests.request("GET", imdburl, headers=headers, params=qstring).text
              image = json.loads(response).get('d')[0].get('i').get('imageUrl')
              msg = image
              msg += '\n'
              msg += json.loads(response).get('d')[0].get('l')
              movieid = json.loads(response).get('d')[0].get('id')
              imdburl = 'https://imdb8.p.rapidapi.com/title/get-ratings'
              qstring = {"tconst": movieid}
              response = requests.request("GET", imdburl, headers=headers, params=qstring).text
              msg += '\nRating: '
              msg += str(json.loads(response).get("rating"))
              await message.channel.send(msg)
       elif message.content.startswith('!year'):
              imdburl = "https://imdb8.p.rapidapi.com/title/auto-complete"
              qstring = {"q": message.content.replace('!year ', '')}
              headers = {
                     'x-rapidapi-host': "imdb8.p.rapidapi.com",
                     'x-rapidapi-key': "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
              }
              response = requests.request("GET", imdburl, headers=headers, params=qstring).text
              image = json.loads(response).get('d')[0].get('i').get('imageUrl')
              msg = image
              msg += '\n'
              msg += json.loads(response).get('d')[0].get('l')
              movieid = json.loads(response).get('d')[0].get('id')
              imdburl = 'https://imdb8.p.rapidapi.com/title/get-ratings'
              qstring = {"tconst": movieid}
              response = requests.request("GET", imdburl, headers=headers, params=qstring).text
              msg += '\nYear: '
              msg += str(json.loads(response).get('year'))
              await message.channel.send(msg)
       elif message.content.startswith('!popceleb'):
              imdburl = 'https://imdb8.p.rapidapi.com/actors/list-most-popular-celebs'
              qstring = {"currentCountry":"US","purchaseCountry":"US","homeCountry":"US"}
              headers = {
                     'x-rapidapi-host': "imdb8.p.rapidapi.com",
                     'x-rapidapi-key': "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
              }
              response = requests.request("GET", imdburl, headers=headers, params=qstring).text
              imdburl = "https://imdb8.p.rapidapi.com/actors/get-bio"
              actors = json.loads(response)
              for i in range(0,5):
                     number = ''
                     for char in actors[i]:
                            if char.isdigit():
                                   global actorid
                                   number += char
                                   actorid = 'nm' + number
                     qstring = {"nconst":actorid}
                     response = requests.request("GET", imdburl, headers=headers, params=qstring).text
                     bio = json.loads(response).get("miniBios")[0].get("text")
                     name = json.loads(response).get("name")
                     image = json.loads(response).get("image").get("url")
                     link = 'https://www.imdb.com/name/'+actorid+'/'
                     msg = image + '\n' + name + '\n' + link
                     await message.channel.send(msg)
       elif message.content.startswith('!cast'):
              imdburl = 'https://imdb8.p.rapidapi.com/title/auto-complete'
              qstring = {"q": message.content.replace('!cast ', '')}
              headers = {
                     'x-rapidapi-host': "imdb8.p.rapidapi.com",
                     'x-rapidapi-key': "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
              }
              response = requests.request("GET", imdburl, headers=headers, params=qstring).text
              cast = json.loads(response).get("d")[0].get('s')
              name = json.loads(response).get("d")[0].get('l')
              image = json.loads(response).get("d")[0].get('i').get('imageUrl')
              msg = image + '\nName: ' + name + '\nTop Cast: ' + cast
              await message.channel.send(msg)
       elif message.content.startswith('!popmovie'):
              imdburl = "https://imdb8.p.rapidapi.com/title/get-most-popular-movies"
              qstring = {"purchaseCountry": "US", "homeCountry": "US", "currentCountry": "US"}
              headers = {
                     'x-rapidapi-host': "imdb8.p.rapidapi.com",
                     'x-rapidapi-key': "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
              }
              response = requests.request("GET", imdburl, headers=headers, params=qstring).text
              imdburl = 'https://imdb8.p.rapidapi.com/title/get-meta-data'
              movies = json.loads(response)
              for i in range(0,5):
                     number = ''
                     for char in movies[i]:
                            if char.isdigit():
                                   global movieid2
                                   number += char
                                   movieid2 = 'tt' + number
                     qstring = {"ids":movieid2}
                     response = requests.request("GET", imdburl, headers=headers, params=qstring).text
                     image = json.loads(response).get(movieid2).get('title').get('image').get('url')
                     title = json.loads(response).get(movieid2).get('title').get('title')
                     ratings = json.loads(response).get(movieid2).get('ratings').get('rating')
                     msg = image + '\n' + title + '\nRatings: ' + str(ratings)
                     await message.channel.send(msg)
       elif message.content.startswith('!like'):
              imdburl = "https://imdb8.p.rapidapi.com/title/auto-complete"
              qstring = {"q": message.content.replace('!like ', '')}
              headers = {
                     'x-rapidapi-host': "imdb8.p.rapidapi.com",
                     'x-rapidapi-key': "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
              }
              response = requests.request("GET", imdburl, headers=headers, params=qstring).text
              movieid = json.loads(response).get('d')[0].get('id')
              msg = 'Like ' + message.content.replace('!like ', '') + ': \n'
              imdburl = "https://imdb8.p.rapidapi.com/title/get-more-like-this"
              qstring = {"tconst":movieid}
              headers = {
                     'x-rapidapi-host': "imdb8.p.rapidapi.com",
                     'x-rapidapi-key': "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
              }
              response = requests.request("GET", imdburl, headers=headers, params=qstring).text
              imdburl = 'https://imdb8.p.rapidapi.com/title/get-meta-data'
              movies = json.loads(response)
              for i in range(0, 3):
                     number = ''
                     for char in movies[i]:
                            if char.isdigit():
                                   number += char
                                   movieid2 = 'tt' + number
                     qstring = {"ids": movieid2}
                     response = requests.request("GET", imdburl, headers=headers, params=qstring).text
                     print(json.loads(response))
                     image = json.loads(response).get(movieid2).get('title').get('image').get('url')
                     title = json.loads(response).get(movieid2).get('title').get('title')
                     ratings = json.loads(response).get(movieid2).get('ratings').get('rating')
                     msg += image + '\n' + title + '\nRatings: ' + str(ratings)
                     await message.channel.send(msg)

@client.event
async def on_ready():
       print('Logged in as')
       print(client.user.name)
       print(client.user.id)
       print('------')

client.run(TOKEN)
