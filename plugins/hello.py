from nonebot import on_command, CommandSession


@on_command('hi', aliases='你好')
async def hello(session: CommandSession):
    hello_world = '舰长好！这里是崩坏3机器娘，在群内发送以下指令可以和我交流哦：\n' + \
                  'sh+空格+圣痕名称（位置）: 可以查看单件圣痕的具体信息；\n' + \
                  'wq+空格+武器名称: 可以查看武器的具体信息；\n' + \
                  'fy+空格+要翻译的内容: 可以翻译内容；\n' + \
                  'rp: 可以试试自己的运气；\n' + \
                  'sy: 可以查看本期深渊时间；\n' + \
                  'fd+内容: 可以复读这段内容；\n' + \
                  '24：进行一次24点游戏；'
    await session.send(hello_world)
