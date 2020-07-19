from nonebot import on_notice, NoticeSession


# 将函数注册为群成员增加通知处理器
@on_notice('group_increase')
async def _(session: NoticeSession):
    # 发送欢迎消息
    await session.send('欢迎新舰长～\n我是机器娘芽衣，@我说“hi”或者“你好”可以和我交流哦！')
