from typing import List
from datetime import date, timedelta


def today() -> str:
    return date.today().strftime('%a, %d  %b %Y')


def whole_next_week() -> List[str]:
    return [day.strftime('%a, %d  %b %Y') for day in (date.today() + timedelta(days=n) for n in range(7))]


def current_week() -> str:
    today = date.today()
    first_day = date(today.year, 1, 1)
    week = today.isocalendar()[1]
    monday = first_day + timedelta((week - 1) * 7)
    sunday = first_day + timedelta(week * 7 - 1)
    return f"{monday.strftime('%a, %d %b %Y')} - {sunday.strftime('%a, %d %b %Y')}"
