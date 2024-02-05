from datetime import datetime
import zoneinfo
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Function which handles "/" request.
    :return: show_time() function which generates needed template.
    """
    return show_time()


def unify_number(number: int) -> str:
    """
    Function unifies integer number to a string of the following format: "xx".
    :param number: Integer number which has to be unified.
    :return: String of unified number.
    """
    if number < 10:
        return f"0{number}"
    return f"{number}"


def show_time():
    """
    Function renders HTML template with current time and date.
    :return: Rendered template.
    """

    # Getting current time of the defined timezone
    # (in this case, "Europe/Moscow")
    moscow_tz = zoneinfo.ZoneInfo("Europe/Moscow")
    time_now = datetime.now(moscow_tz)

    # Converting datetime attributes to string in the formats:
    # "hh:mm:ss" for time,
    # "yyyy / mm / dd" for the date.
    hour = unify_number(time_now.hour)
    minute = unify_number(time_now.minute)
    second = unify_number(time_now.second)

    year = time_now.year
    month = unify_number(time_now.month)
    day = unify_number(time_now.day)

    current_time = f"{hour}:{minute}:{second}"
    current_date = f"{year} / {month} / {day}"

    return render_template('index.html', time=current_time, date=current_date)


if __name__ == '__main__':
    app.run(debug=True)
