from nonebot import on_command, CommandSession

import datetime


@on_command('sy', aliases='深渊', only_to_me=False)
async def hello(session: CommandSession):
    now = datetime.datetime.now()
    tip = ''
    if now.weekday() == 2 or now.weekday() == 6:
        end_time = datetime.datetime.strptime(now.strftime('%Y-%m-%d') + ' 22:00:00', '%Y-%m-%d %H:%M:%S')
        if now < end_time:
            temp_time = end_time - now
            hour = int(temp_time.seconds / 3600)
            hour_result = temp_time.seconds % 3600
            minute = int(hour_result / 60)
            second = hour_result % 60
            tip = '今晚深渊结算！\n舰长还有' + str(hour) + '小时' + str(minute) + '分钟' + str(second) + '秒可以打深渊' + \
                  '\n舰长加油呀！'
        if now >= end_time:
            tip = '今天的深渊已经结算了，舰长打得怎么样呢？\n不管怎样，下期深渊舰长要加油哦，干巴爹！'
    elif now.weekday() < 2:
        wednesday = now
        one_day = datetime.timedelta(days=1)
        while wednesday.weekday() != 2:
            wednesday += one_day
        end_time = datetime.datetime.strptime(wednesday.strftime('%Y-%m-%d') + ' 22:00:00', '%Y-%m-%d %H:%M:%S')
        temp_time = end_time - now
        hour = int(temp_time.seconds / 3600)
        hour_result = temp_time.seconds % 3600
        minute = int(hour_result / 60)
        second = hour_result % 60
        tip = '离本期深渊结算还有' + str(temp_time.days) + '天' + str(hour) + '小时' + str(minute) + '分钟' + str(second) + '秒' \
              + '\n舰长有空多打打深渊哦'
    elif 2 < now.weekday() < 6:
        sunday = now
        one_day = datetime.timedelta(days=1)
        while sunday.weekday() != 6:
            sunday += one_day
        end_time = datetime.datetime.strptime(sunday.strftime('%Y-%m-%d') + ' 22:00:00', '%Y-%m-%d %H:%M:%S')
        temp_time = end_time - now
        hour = int(temp_time.seconds / 3600)
        hour_result = temp_time.seconds % 3600
        minute = int(hour_result / 60)
        second = hour_result % 60
        tip = '离本期深渊结算还有' + str(temp_time.days) + '天' + str(hour) + '小时' + str(minute) + '分钟' + str(second) + '秒' \
              + '\n舰长有空多打打深渊哦'
    else:
        tip = '哎呀，芽衣出错了，别欺负芽衣了'
    await session.send(tip)
