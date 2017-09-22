@client.event
#when message is sent to server
async def on_message(message):
    #if message addresses bot
    if message.content.startswith('s!'):
        if message.content.startswith('s!help'):
            if message.content.startswith('s!help bank'):
                await client.send_message(message.channel, """`s!bank list`: lists the current banks in the server
`s!bank transfer (account no.) (amount`: sends money to the selected account
`s!bank deposit (account
`s!bank loan list"""
            elif message.content.startswith('s!help business'):
                await client.send_message(message.channel, """`s!business list`: list all businesses available and their prices
`s!business buy (business name)`: purchases a business for the user
`s!business sell (business name)`: sells a business for half the purchase price
`s!business hire (business name) (player to hire)`: offers a job to the seleccted player to  work  at your business
`s!business fire (business name) (player to fire)`: fires the selected player from your business
`s!business setup (business name)`: starts setup process for selected business (e.g. wages, etc."""
            else:
                await client.send_message(message.channel, """`s!help bank`: bank help
`s!help business`: business help

`s!bank`: bank functions (more details in s!help bank)
`s!business`: business functions (more details in s!help business)"""
        #bank functions
        elif message.content.startswith('s!bank') or message.content.startswith('s!ba'):
            if message.content.startswith('s!bank list'):
            elif message.content.startswith('s!bank transfer'):
            elif message.content.startswith('s!bank create'):
            elif message.content.startswith('s!bank deposit'):
            elif message.content.startswith('s!bank withdraw'):
            elif message.content.startswith('s!bank loan'):
                if message.content.startswith('s!bank loan list'):
                elif message.content.startswith('s!bank loan get'):
                elif message.content.startswith('s!bank loan current'):
                elif messgae.content.startswith('s!bank loan repay'):
            elif message.content.startswith('s!bank balance') or message.content.startswith('s!bank bal'):
        #business functions
        elif message.content.startswith('s!business') or message.content.startswith('s!bu'):
            if message.content.startswith('s!business list'):
            elif message.content.startswith('s!business buy'):
            elif message.content.startswith('s!business sell'):
            elif message.content.startswith('s!business hire'):
            elif message.content.startswith('s!business fire'):
        
