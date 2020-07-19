from bs4 import BeautifulSoup
from nonebot import on_command, CommandSession

import requests  # 爬虫库


@on_command('sh', aliases=('圣痕'), only_to_me=False)  # 定义翻译指令及别名
async def translate(session: CommandSession):
    message = session.get('message', prompt='舰长想要查询什么圣痕呢？')  # 获取待查询的圣痕
    translate_send = await get_translate(message)  # 将待查询的圣痕传给查询函数
    await session.send(translate_send)  # 发送翻译后的语句


async def get_translate(message):  # 异步的查询函数
    translate_sentence = get_content(message)
    return translate_sentence


def get_content(message):  # 圣痕查询功能
    url = 'https://wiki.biligame.com/bh3/%E5%9C%A3%E7%97%95%E5%9B%BE%E9%89%B4'
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find('div', class_='mw-parser-output').find_all('a')
    finalUrl = ''
    result = ''
    try:
        for link in links:
            if message in link.get_text():
                finalUrl = 'https://wiki.biligame.com' + link['href']
    except Exception as e:
        print(e)
        return '出错了，请舰长换个圣痕试试'
    if finalUrl is not None and finalUrl != '':
        res2 = requests.get(finalUrl)
        res2.encoding = res2.apparent_encoding
        html2 = res2.text
        soup2 = BeautifulSoup(html2, 'lxml')
        links2 = soup2.find('div', class_='box-poke-left').find_all('td')
        result = '圣痕名：' + links2[0].get_text() + \
                 '位置：' + links2[1].get_text() + \
                 '稀有度：' + links2[2].get_text() + \
                 '单件技能：' + links2[11].get_text()
        if links2[13].get_text() != '\n':
            result = result + '两件套技能：' + links2[13].get_text() + '三件套技能：' + links2[14].get_text()
    else:
        return '舰长查询的圣痕不存在或名字有误，请注意圣痕名字中间的符号呀'
    if result == '':
        return '该圣痕暂无描述哦'
    return result


@translate.args_parser  # sh命令的参数解析器
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()  # 去除首尾空白符
    if session.is_first_run:  # 如果是第一次运行
        if stripped_arg:  # 如果用户的待翻译语句跟在指令后面，则直接传参
            session.state['message'] = stripped_arg
        return
    if not stripped_arg:  # 如果用户的待翻译语句不在指令后面，则让他另行输入
        session.pause('要查询的圣痕不能为空呢，请舰长重新输入')
    # 将参数放入会话状态中
    session.state[session.current_key] = stripped_arg
