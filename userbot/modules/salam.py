from time import sleep

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.utils import edit_or_reply, man_cmd


@man_cmd(pattern="p(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Assalamualaikum Dulu Biar Sopan**")


@man_cmd(pattern="kalem(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**KALEM OP ANJENGGG**")


@man_cmd(pattern="P(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**Haii Salken Saya {owner}**")
    sleep(2)
    await xx.edit("**Assalamualaikum...**")


@man_cmd(pattern="l(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Wa'alaikumsalam**")


@man_cmd(pattern="a(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**Haii Salken Saya {owner}**")
    sleep(2)
    await xx.edit("**Assalamualaikum**")


@man_cmd(pattern="oc(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "**🌨️🌈☔💞💓💜💗💖🖤💝♥️💕💌💋❣️💔**")
    sleep(3)
    await xx.edit("**✨MALVINECENNA KALEM✨**")


@man_cmd(pattern="sekutot(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**KE KOTA PERU MAKAN MENGKUDU**")
    sleep(2)
    await xx.edit("**ALIANSI SEKUTU UDA MATI KUTU 🤭🤙**")


@man_cmd(pattern="ass(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "**Salam Dulu Biar Sopan**")
    sleep(2)
    await xx.edit("**السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ**")


CMD_HELP.update(
    {
        "salam": f"**Plugin : **`salam`\
        \n\n  •  **Syntax :** `{cmd}p`\
        \n  •  **Function : **Assalamualaikum Dulu Biar Sopan..\
        \n\n  •  **Syntax :** `{cmd}pe`\
        \n  •  **Function : **salam Kenal dan salam\
        \n\n  •  **Syntax :** `{cmd}l`\
        \n  •  **Function : **Untuk Menjawab salam\
        \n\n  •  **Syntax :** `{cmd}ass`\
        \n  •  **Function : **Salam Bahas arab\
        \n\n  •  **Syntax :** `{cmd}semangat`\
        \n  •  **Function : **Memberikan Semangat.\
        \n\n  •  **Syntax :** `{cmd}ywc`\
        \n  •  **Function : **nMenampilkan Sama sama\
        \n\n  •  **Syntax :** `{cmd}sayang`\
        \n  •  **Function : **Kata I Love You.\
        \n\n  •  **Syntax :** `{cmd}k`\
        \n  •  **Function : **LU SEMUA NGENTOT 🔥\
        \n\n  •  **Syntax :** `{cmd}j`\
        \n  •  **Function : **NIMBRUNG GOBLOKK!!!🔥\
    "
    }
)
