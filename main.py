

from apscheduler.schedulers.blocking import BlockingScheduler
def sayhello():
    print("Hello, World!")


def run():
    print('hello')
    scheduler = BlockingScheduler(timezone="Asia/Shanghai")
    # 3分钟跑一次
    scheduler.add_job(sayhello, 'cron', second='0', minute='0/1',
                      id='under_baseline_task 1 ')
    scheduler.start()

if __name__ =='__main__':
    run()
