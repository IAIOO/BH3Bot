from nonebot import on_command, CommandSession

import random


@on_command('rp', aliases='人品', only_to_me=False)
async def hello(session: CommandSession):
    num = random.randint(0, 100)
    nickname = session.ctx.sender.get('nickname')
    return_text = nickname + '舰长的人品值是：' + str(num)
    if 0 < num <= 10:
        return_text = return_text + '\n' + '舰长的运气可真差呀，非酋还是别抽卡了！'
    elif 10 < num <= 35:
        return_text = return_text + '\n' + '舰长的运气不太好哦，脸黑请谨慎抽卡！'
    elif 35 < num <= 65:
        return_text = return_text + '\n' + '舰长的运气一般般呀，建议适当抽卡。'
    elif 65 < num <= 90:
        return_text = return_text + '\n' + '舰长的运气还不错哦，出货率应该不错！'
    elif 90 < num <= 99:
        return_text = return_text + '\n' + '舰长的运气可真棒呀，快去抽卡吧！'
    elif num == 0:
        return_text = return_text + '\n' + '(￣口￣)!!这里有一只非酋舰长，大家快跑！'
    elif num == 100:
        return_text = return_text + '\n' + '!!!这里有一只欧皇舰长，大家快来吸欧气o(^▽^)o'
    else:
        return_text = '机器娘出错了，请稍后再试'
    await session.send(return_text)
