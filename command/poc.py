import discord
import random

poc_list = [
    'https://cdn.discordapp.com/attachments/595418420753727488/828110941601923113/AYOOO.PNG', 
    'https://cdn.discordapp.com/attachments/595418420753727488/828110731625889812/encastbodypillow.PNG', 
    'https://cdn.discordapp.com/attachments/595418420753727488/830596917226111027/ayo..PNG',
    'https://cdn.discordapp.com/attachments/831233601290371165/1041557223572258926/image.png',
    'https://cdn.discordapp.com/attachments/863985212974825496/1000956405953601676/unknown.png',
    'https://cdn.discordapp.com/attachments/863985212974825496/993643023428767874/unknown.png',
    'https://i.gyazo.com/thumb/1200/57079be4d4e824895ce48e8f8df107e3-png.jpg',
    'https://cdn.discordapp.com/attachments/863985212974825496/987877025618485278/xMadKing_is_RACIST.mp4',
    'https://cdn.discordapp.com/attachments/863985212974825496/983846014987407380/unknown.png',
    'https://cdn.discordapp.com/attachments/863985212974825496/980568422167478323/unknown.png',
    'https://i.gyazo.com/thumb/1200/dcf310c3b1f313d5dc7dcc72ebf6490a-png.jpg',
    'https://cdn.discordapp.com/attachments/863985212974825496/977416444486754314/unknown.png',
    'https://cdn.discordapp.com/attachments/831233601290371165/1041558624205537380/image.png',
    'https://cdn.discordapp.com/attachments/863985212974825496/969408065378078841/unknown.png',
    'https://cdn.discordapp.com/attachments/595418420753727488/904517762146267186/unknown.png',
    'https://cdn.discordapp.com/attachments/595418420753727488/908942738848882688/unknown.png',
    'https://cdn.discordapp.com/attachments/595418420753727488/900490521221398558/image.png',
    'https://cdn.discordapp.com/attachments/595418420753727488/924124140980555776/unknown.png',
    'https://cdn.discordapp.com/attachments/611611572925759576/1041559344203968512/image.png',
    'https://cdn.discordapp.com/attachments/595418420753727488/870787096011477001/unknown.png',
    'https://cdn.discordapp.com/attachments/863985212974825496/949053645532565514/Screen_Shot_2022-03-03_at_3.20.15_PM.png',
    'https://i.gyazo.com/thumb/1200/882c52f83620c8fd63bd99ac28734b5e-png.jpg',
    'https://cdn.discordapp.com/attachments/863985212974825496/941155949392052244/unknown.png',
    'https://cdn.discordapp.com/attachments/863985212974825496/933896233712496650/unknown.png',
    'https://cdn.discordapp.com/attachments/200649656802344960/859867394863792188/image0.png',
    'https://cdn.discordapp.com/attachments/611611572925759576/1041559886263230504/image.png',
    'https://cdn.discordapp.com/attachments/611611572925759576/1041559934342549514/image.png',
    'https://cdn.discordapp.com/attachments/611611572925759576/1041558140916875306/encastslave.PNG',
    'https://cdn.discordapp.com/attachments/595418420753727488/854817904012165150/context.PNG',
    'https://cdn.discordapp.com/attachments/595418420753727488/838491349959049276/unknown.png',
    'https://cdn.discordapp.com/attachments/595418420753727488/836781950332960768/Screenshot_2021-04-27_205007.png',
    'https://cdn.discordapp.com/attachments/595418420753727488/835259204603215982/encast_is_a_rude_boy.png',
    'https://cdn.discordapp.com/attachments/595418420753727488/835259086088962058/encast_is_grooming_us.PNG',
    'https://cdn.discordapp.com/attachments/595418420753727488/833867394316369961/4k.PNG',
    'https://cdn.discordapp.com/attachments/595418420753727488/827332408482201610/image0.png',
    'https://cdn.discordapp.com/attachments/595418420753727488/826277732899094548/unknown.png',
    'https://cdn.discordapp.com/attachments/595418420753727488/826243799646601266/unknown.png',
    'https://cdn.discordapp.com/attachments/863985212974825496/1041563016015130644/image.png',
    'https://cdn.discordapp.com/attachments/595418420753727488/823655519491194921/image0.png',
    'https://cdn.discordapp.com/attachments/595418420753727488/821849688617648179/unknown.png',
    'https://gyazo.com/364723e8ab5f4c6acb16f74141c3780e',
    'https://cdn.discordapp.com/attachments/257255675753660417/1043295818209316875/image.png',
    'https://cdn.discordapp.com/attachments/726253587713491015/1043302582115913768/unknown.png',
    'https://i.imgur.com/RPww7Kv.png',
    'https://cdn.discordapp.com/attachments/863985212974825496/1044786862050525214/image.png',
    'https://cdn.discordapp.com/attachments/726253587713491015/1044808576931205200/Jre-legacy_2022.11.03_-_00.35.17.05.DVR_Trim.mp4',
    'https://cdn.discordapp.com/attachments/610634069428011025/1050115320662200330/image.png',
]


@discord.app_commands.command(name="poc", description="See sus messages from members of Piper's Playhouse!")
async def poc(interaction: discord.Interaction, index: int = None):
    url = None
    list_len = len(poc_list)
    if index is not None:
        if index < 0 or index >= list_len:
            await interaction.response.send_message(f"Invalid index, must be between 0 and {list_len - 1}", ephemeral=True)
            return
        
        url = poc_list[index]
    else:
        # might rarely get exactly list_len, which is an invalid index; in this
        # case, return list_len - 1
        rand_idx = min(int(random.uniform(0, list_len)), list_len - 1)
        url = poc_list[rand_idx]

    await interaction.response.send_message(url)