import prompt_treatment
import random
import time

import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()


# AI Functions :
def get_most_used_word(words_map) :
    most_used_word = ""
    most_used_word_score = 0
    for word in words_map.keys() :
        if words_map[word] > most_used_word_score :
            most_used_word = word
            most_used_word_score = words_map[word]
    return most_used_word

def answer(prompt) :
    words = prompt_treatment.create_words_map(prompt)
    if len(words) <= 1 :
        return "Cannot generate a proper answer with only one word entry"
    words_list = []
    for word in words.keys() :
        words_list.append(word)
    generated_words = 0
    sentence = ""
    words_score = prompt_treatment.calculate_words_map_score(words)
    answer_words_count = random.randint(words_score , words_score + words_score)
    for loop in range(answer_words_count) :
        most_used_word = get_most_used_word(words)
        sentence += most_used_word
        if words[most_used_word] >= 1 :
            words[most_used_word] -= 1
            words_list.remove(most_used_word)
            words[words_list[random.randint(0 , len(words_list) - 1)]] += 1
            words_list.append(most_used_word)
            if get_most_used_word(words)[0].isupper() :
                sentence += ". "
                generated_words = -1
            else :
                if generated_words >= random.randint(6 , 8) :
                    sentence += ", "
                    generated_words = -1
                else :
                    sentence += " "
            generated_words += 1
    return sentence


# AI Code for Discord
ai = commands.Bot(command_prefix:="!" , intents=discord.Intents.all())

@ai.event
async def on_ready() :
    # sync commandes
    try :
        # sinc
        synced = await ai.tree.sync()
        print(f"cmds sync : {len(synced)}")
    except Exception as e :
        print(e)

'''
@ai.event
async def on_message(msg : discord.Message) :
    # bot peu pas se déclencher lui-même
    if msg.author.bot :
        return
    if msg.content == 'hi' :
        channel = msg.channel
        author = msg.author

        a_c = ai.get_channel(1378470486937440317)
        # POUR SERVEUR (CHANNEL ACTUEL)
        # await channel.send("hi")
        # POUR SERVEUR (AUTRE CHANNEL)
        # await a_c.send("hi")
        # POUR MP :
        # await author.send("hi")
'''

@ai.tree.command(name="answer" , description="Generate a text based on the user's input")
async def youtube(interaction : discord.Interaction , text_input : str) :
    embed = discord.Embed(
        title="IdiotAI" ,
        description="The best AI ever" ,
        color=discord.Color.blue()
    )
    embed.add_field(name="User input" , value=text_input)
    embed.add_field(name="Ai Answer" , value=answer(text_input))
    await interaction.response.send_message(embed=embed)

ai.run(os.getenv('DISCORD_TOKEN'))
