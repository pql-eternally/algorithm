import chinese_calendar as calendar
import datetime


def is_holiday(date):
    """
    判断是否是节假日
    """
    return calendar.is_holiday(date)


def is_workday(date):
    """
    判断是否是工作日
    """
    return calendar.is_workday(date)


def is_weekend(date):
    """
    判断是否是周末
    """
    return date.weekday() in [5, 6]


def is_rainy_day(text):
    """
    判断是否是雨天
    """
    return '雨' in text


def is_sunny_day(text):
    """
    判断是否是晴天
    """
    return '晴' in text


def is_snowy_day(text):
    """
    判断是否是雪天
    """
    return '雪' in text


def is_overcast_day(text):
    """
    判断是否是阴天
    """
    return '阴' in text


def is_cloudy_day(text):
    """
    判断是否是多云
    """
    return '多云' in text


def test_date():
    # 2021年1月1日是元旦节，并且是周五
    d1 = datetime.date(2021, 1, 1)
    assert is_holiday(d1) is True
    assert is_workday(d1) is False
    assert is_weekend(d1) is False

    # 2023年9月14日是工作日、周四
    d2 = datetime.date(2023, 9, 14)
    assert is_holiday(d2) is False
    assert is_workday(d2) is True
    assert is_weekend(d2) is False

    # 2023年9月16日是周末、周五
    d3 = datetime.date(2023, 9, 16)
    assert is_holiday(d3) is True
    assert is_workday(d3) is False
    assert is_weekend(d3) is True

    # 2023年9月29日是中秋节、周五
    d4 = datetime.date(2023, 9, 29)
    assert is_holiday(d4) is True
    assert is_workday(d4) is False
    assert is_weekend(d4) is False

    # 2023年9月30日是国庆节、周六
    d5 = datetime.date(2023, 9, 30)
    assert is_holiday(d5) is True
    assert is_workday(d5) is False
    assert is_weekend(d5) is True
