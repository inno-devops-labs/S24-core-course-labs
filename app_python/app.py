import bottle
import datetime

app = bottle.Bottle()


@app.route("/")
def current_time_in_moscow():
    moscow_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        hours=3
    )
    return f"Current time in Moscow: {moscow_time.strftime('%Y-%m-%d %H:%M:%S')}"


if __name__ == "__main__":
    bottle.run(app, host="0.0.0.0", port=8080)