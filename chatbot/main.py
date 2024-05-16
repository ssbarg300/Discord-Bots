import discord
import google.generativeai as genai

#give all permissions
intents = discord.Intents.all()
#initialize the client
client = discord.Client(intents=intents)

genai.configure(api_key="API_KEY")

#model = genai.GenerativeModel('gemini-pro')
model = genai.GenerativeModel('gemini-pro',
	safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
	]
	)




#listen for bot to be ready
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #channel = client.get_channel("993539712318980117")
    channel = discord.utils.get(client.get_all_channels(), name='general')
    await channel.send("@everyone im online!, mention me before the question to get an answer.")


# listen for messages
@client.event
async def on_message(message):
    #if message is from bot then just return
    if message.author == client.user:
        return


    # Check if the bot is mentioned
    if client.user.mentioned_in(message):
        # Extract the message content without the mention
        content = message.content.replace(f"<@{client.user.id}>", "").strip()
        response = model.generate_content(content)
        await message.channel.send(response.text)

    
#TOKEN
client.run("TOKEN")