import math as m
import numpy as np
import os
import openai
openai.api_key = os.environ['openAi']
openai.Model.list()
#playerNames = []

#how many players are going to play?

#playerNum = int(input("How many players are there?\n"))

#initializing the number of pictues rounds the user wants to play

#rounds = input("How many rounds would you like to play? :)\n")

#creates a list of player names

#for i in range(1,playerNum + 1):
  #playerNames += input("username for player " + str(i) + "\n")


#the ai shit
def ai(playerPrompt):  
  response = openai.Image.create(
    prompt=playerPrompt,
    n=1,
    size="256x256"
  )
  image_url = response['data'][0]['url']
  return image_url
  
#list for prompt
prompList = []

#list for urls
urlList = []

#cycle variable
indi = 0

#store how many players
playerDone = 0

#how many rounds will be played
roundPlaying = 0
