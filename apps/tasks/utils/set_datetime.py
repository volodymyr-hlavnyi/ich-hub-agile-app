from django.utils import timezone
import calendar
from datetime import datetime

def last_day_of_month(year, month):
    today = datetime(year, month, 1)
    amount_of_days = calendar.monthrange(year, month)[1]
    date = datetime(year, month, amount_of_days)
    return today.astimezone()