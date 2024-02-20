import datetime


def getMskTime():
    msk = datetime.timezone(datetime.timedelta(hours=3))
    time = datetime.datetime.now(msk)
    return time.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":

    class DatetimeMock(datetime.datetime):
        @classmethod
        def now(cls, tz=None):
            return cls(2077, 1, 1, 12, 0, 0)

    datetime.datetime = DatetimeMock

    print(getMskTime())
