from bs4 import BeautifulSoup
from nonebot import on_command, CommandSession

import requests  # 爬虫库


@on_command('wq', aliases=('武器'), only_to_me=False)  # 定义翻译指令及别名
async def translate(session: CommandSession):
    message = session.get('message', prompt='舰长要查询什么武器呢？')  # 获取待查询的武器
    translate_send = await get_translate(message)  # 将待查询的武器传给查询函数
    await session.send(translate_send)  # 发送翻译后的语句


async def get_translate(message):  # 异步的查询函数
    translate_sentence = get_content(message)
    return translate_sentence


def get_content(message):  # 武器查询功能
    url = 'https://wiki.biligame.com/bh3/%E6%AD%A6%E5%99%A8%E5%9B%BE%E9%89%B4'
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('a')
    finalUrl = ''
    result = ''
    try:
        for link in links:
            if message in link.get_text():
                finalUrl = 'https://wiki.biligame.com' + link['href']
    except Exception as e:
        print(e)
        return '出错了，舰长换个武器试试嘛'
    if finalUrl is not None and finalUrl != '':
        res2 = requests.get(finalUrl)
        res2.encoding = res2.apparent_encoding
        html2 = res2.text
        soup2 = BeautifulSoup(html2, 'lxml')
        links2 = soup2.find('div', class_='box-poke-left').find_all('td')
        wq_name = '武器名：' + links2[0].get_text()
        wq_type = '类型：' + links2[1].get_text()
        wq_star = '星级：' + links2[2].get_text()
        attack = '攻击力：' + links2[3].get_text()
        huixin = '会心：' + links2[4].get_text()
        wq_content = '描述：' + links2[7].get_text()
        wq_skill1 = '技能1：' + links2[11].get_text()
        wq_skill2 = ''
        wq_skill3 = ''
        if links2[12].get_text() != '\n':
            wq_skill2 = '技能2：' + links2[12].get_text()
        if links2[13].get_text() != '\n':
            wq_skill3 = '技能3：' + links2[13].get_text()
        result = wq_name + wq_type + wq_star + attack + huixin + wq_content + wq_skill1 + wq_skill2 + wq_skill3
    else:
        return '舰长查询的武器不存在或名字有误，请注意武器名字中间的符号呀'
    if result == '':
        return '该武器暂无资料哦'
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
