from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError


@nonebot.scheduler.scheduled_job('cron', hour='12')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    if now.weekday() == 2 or now.weekday() == 6:
        try:
            await bot.send_group_msg(group_id=707441115,
                                     message=f'今晚深渊结算！\n舰长们要记得打深渊哦！\nღ( ´･ᴗ･` )比心')
        except CQHttpError:
            pass
