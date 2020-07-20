from nonebot import on_command, CommandSession
from nonebot import permission as perm

import nonebot


@on_command('send', permission=perm.SUPERUSER)
async def controller(session: CommandSession):
    message = session.get('message')
    bot = nonebot.get_bot()
    await bot.send_group_msg(group_id=707441115, message=message)
