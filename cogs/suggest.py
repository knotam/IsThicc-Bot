#
#                          IsThicc-bot Suggest.py | 2020-2021 (c) IsThicc
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
import discord, asyncio, re
from discord import Embed as em
from discord.ext import commands
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
class Suggestions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
    @commands.Cog.listener()
    async def on_message(self, message):

        if message.channel.id != 801929449124790353 or message.author.bot: return

        # Remove Markdown Using Regex
        # **, ||, __, ~~ and `
        content = re.sub(r'~~|\|\||__|\*\*|`+', "", message.content)

        # Remove Markdown
        # content = ""
        # msg = message.content
        # for letter in msg:
        #     if letter == "`":
        #         continue
        #     elif letter in ['~', '_', "*", "|"]:
        #         if msg[msg.index(letter) + 1] == letter:  # check if **, __, or ~~
        #             continue
        #     else:
        #         content += letter

        msg = await self.bot.get_channel(801929480875802624).send(
            embed=em(
                colour=discord.Colour.blue(),
                description=f"```{content}```"
            ).set_author(
                name=f"New suggestion from {message.author}",
                icon_url=message.author.avatar_url
            )
        )

        await msg.add_reaction('👍')
        await msg.add_reaction('👎')

        await message.reply(f'{msg.jump_url}', delete_after=5, ping=False)

#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
def setup(bot):
    bot.add_cog(Suggestions(bot))
