import discord

client = discord.Client()
errorcode1 = "GX013"
help = "명령어 :\n/해군 설명\n/해군 맵 링크\n/해군 오류코드 설명\n/해군 봇 개발자"
@client.event
async def on_ready():
    print("Ready")
    game = discord.Game("/해군 명령어")
    await client.change_presence(status=discord.Status.online, activity=game)
@client.event
async def on_message(message):
    if message.content.startswith('/해군 설명'):
        await message.channel.send("국가 - 대한민국\n활동 기간 - 2019년 4월 11일 ~ 현재\n종류 - 해군\n규모 - 29명\n명령 체계 - 해군참모총장\n참전 - 오류 : GX013\n지휘관 - 도드\n")
    if message.content.startswith('/해군 명령어'):
        await message.channel.send(help)
    if message.content.startswith('/해군 맵 링크'):
        await message.channel.send("명령어를 실행도중 알 수 없는 오류가 발생하였습니다 - 코드 : "+errorcode1)
    if message.content.startswith('/해군 오류코드 설명'):
        await message.channel.send("GX013 - 지정된 링크나 파일을 찾을 수 없을때\nHP013 - 명령어 목록이 없을때")
    if message.content.startswith('/해군 봇 개발자'):
        await message.channel.send("본명 비공개\n아이디 : 스폰\n문의 :\n디스코드 : spawntj#3364\n이메일 : spawntj521@gmail.com\n이 봇의 저작권은 스폰(가명)에게 있으며 2차 배포가 불가능하고 해군과 관련된 디스코드 서버에서만 사용이 가능")
    if message.content.startswith('/해군 규칙'):
        file = open("rules1.txt")
        file.read()
        await message.channel.send(file.read())
        file.close()


client.run("NjIyNTc4MjU0ODg4NDM1NzIy.XX1_VA.rpMsDTH-E0Bw_gFoOpWLu4MWPjE")
