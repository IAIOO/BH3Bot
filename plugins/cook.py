from bs4 import BeautifulSoup
from nonebot import on_command, CommandSession

import requests  # 爬虫库
import random
import json

KEY = "950bcc32d0324423b0efc1f6272d32f0"


@on_command('cook', aliases=('菜谱'), only_to_me=False)  # 定义翻译指令及别名
async def translate(session: CommandSession):
    message = session.get('message', prompt='舰长想吃什么呢？')  # 获取待查询的武器
    translate_send = await get_translate(message)  # 将待查询的武器传给查询函数
    await session.send(translate_send)  # 发送翻译后的语句


async def get_translate(message):  # 异步的查询函数
    translate_sentence = get_content(message)
    return translate_sentence


def get_content(message):  # 武器查询功能
    url = 'https://www.xinshipu.com//doSearch.html?q=' + message
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('a')
    finalUrl = ''
    resultUrl = []
    result = ''
    try:
        for link in links:
            if message in link.get_text():
                resultUrl.append(link['href'])
    except Exception as e:
        print(e)
        return '舰长想要的菜谱，芽衣做不了呢\n(＞﹏＜)'
    finalUrl = resultUrl[random.randint(0, len(resultUrl) - 1)]
    if finalUrl is not None and finalUrl != '':
        res2 = requests.get('https://www.xinshipu.com/' + finalUrl)
        res2.encoding = res2.apparent_encoding
        html2 = res2.text
        soup2 = BeautifulSoup(html2, 'lxml')
        src = soup2.select('script')[9]
        src = src.string
        materials = json.loads(src, strict=False)['recipeIngredient']
        result = '菜名：' + json.loads(src, strict=False)['name'] + '\n\n' + \
                 '配料：'
        for material in materials:
            result = result + material + '、'
        result = result + '\n\n步骤：' + json.loads(src, strict=False)['recipeInstructions']
    else:
        return '舰长想要的菜谱，芽衣做不了呢\n(＞﹏＜)'
    if result == '':
        return '舰长想要的菜谱，芽衣做不了呢\n(＞﹏＜)'
    return result


@translate.args_parser  # sh命令的参数解析器
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()  # 去除首尾空白符
    if session.is_first_run:  # 如果是第一次运行
        if stripped_arg:  # 如果用户的待翻译语句跟在指令后面，则直接传参
            session.state['message'] = stripped_arg
        return
    if not stripped_arg:  # 如果用户的待翻译语句不在指令后面，则让他另行输入
        session.pause('要查询的武器不能为空呢，请舰长重新输入')
    # 将参数放入会话状态中
    session.state[session.current_key] = stripped_arg
