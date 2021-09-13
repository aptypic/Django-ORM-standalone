import datetime
import os
import django
from datetime import time, tzinfo, timedelta
from django.utils.timezone import localtime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402
from datacenter.models import Visit

fmt = '%Y-%m-%d %H:%M:%S %Z (%z)'


def main():
    security_list = Visit.objects.all()
    # print('Количество пропусков:', Passcard.objects.count())
    # print('Количество активных пропусков:', len(Passcard.objects.filter(is_active=True)))
    # print(Visit.objects.filter(leaved_at__isnull=True))
    for i in Visit.objects.filter(leaved_at__isnull=True):
        print('зашёл в хранилище: ', i.entered_at)
        print('Находится в хранилище: ', (localtime() - i.entered_at.astimezone()))
        b = (localtime() - i.entered_at.astimezone()).total_seconds()
        hours = b // 3600
        minutes = (b % 3600) // 60
        print('{}:{}:{}'.format(round(hours), round(minutes), (localtime() - i.entered_at.astimezone()).seconds))


def timedelta_to_hms(duration):
    # преобразование в часы, минуты и секунды
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return hours, minutes, seconds


if __name__ == '__main__':
    main()
    # print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
