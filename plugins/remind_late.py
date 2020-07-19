from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError


@nonebot.scheduler.scheduled_job('cron', hour='18')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    if now.weekday() == 2 or now.weekday() == 6:
        try:
            await bot.send_group_msg(group_id=707441115,
                                     message=f'我是本群深渊提醒小助手，今晚深渊结算！\n舰长们能打深渊的时间不多了，要加油哦！\n(ง •̀_•́)ง')
        except CQHttpError:
            pass
