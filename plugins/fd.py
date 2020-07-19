from nonebot import on_command, CommandSession

import requests  # 爬虫库
import re  # 正则表达式处理


@on_command('fd', aliases=('复读'), only_to_me=False)  # 定义翻译指令及别名
async def translate(session: CommandSession):
    message = session.get('message', prompt='舰长想让机器娘复读的语句是？')  # 获取待翻译的语句
    translate_send = await get_translate(message)  # 将待翻译的语句传给翻译函数
    await session.send(translate_send)  # 发送翻译后的语句


async def get_translate(message):  # 异步的翻译函数
    translate_sentence = get_content(message)
    return translate_sentence


def get_content(message):  # 复读功能
    return message


@translate.args_parser  # translate命令的参数解析器
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()  # 去除首尾空白符
    if session.is_first_run:  # 如果是第一次运行
        if stripped_arg:  # 如果用户的待翻译语句跟在指令后面，则直接传参
            session.state['message'] = stripped_arg
        return
    if not stripped_arg:  # 如果用户的待翻译语句不在指令后面，则让他另行输入
        session.pause('要翻译的不能为空呢，请重新输入')
    # 将参数放入会话状态中
    session.state[session.current_key] = stripped_arg
