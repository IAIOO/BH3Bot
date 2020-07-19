from nonebot import on_command, CommandSession

import random  # 爬虫库
import re  # 正则表达式处理


@on_command('24')  # 定义翻译指令及别名
async def game(session: CommandSession):
    question = init_game()
    message = session.get('message', prompt='舰长想玩24点游戏了吗，用我给的4个数字通过加减乘除算出24点就是舰长赢了哦\n(๑> ₃ <)' +
                                            '这次的4个数字是：' + question +
                                            '\n舰长做完记得@我回复完整的表达式哦，觉得无解的话回复“end”可以结束游戏。')
    nickname = session.ctx.sender.get('nickname')
    response = ''
    game_result = await wait_for_judge(message)
    if game_result == 1:
        response = nickname + '舰长答对了，真是太厉害了!\n(●･◡･●)ﾉ♥'
    elif game_result == 2:
        response = nickname + '舰长结束了游戏。'
    else:
        response = nickname + '舰长答错了，游戏结束，下次要加油哦。'
    await session.send(response)


async def wait_for_judge(message):
    return judge(message)


def judge(message):  # 翻译功能
    final_result = 0
    if message == 'end':
        return 2
    try:
        if eval(message) == 24:
            final_result = 1
    except Exception as e:
        final_result = '舰长回答的格式不对呢，下次记得要回答英文符号的表达式呀'
    return final_result


def init_game():
    a = random.randint(1, 13)
    b = random.randint(1, 13)
    c = random.randint(1, 13)
    d = random.randint(1, 13)
    return str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(d)


@game.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()  # 去除首尾空白符
    if session.is_first_run:  # 如果是第一次运行
        return
    if not stripped_arg:  # 如果用户的待翻译语句不在指令后面，则让他另行输入
        session.pause('要翻译的不能为空呢，请重新输入')
    # 将参数放入会话状态中
    session.state[session.current_key] = stripped_arg
