import bottle
import datetime

app = bottle.Bottle()

VISIT_COUNT_FILE = 'visits'

def load_visits():
    try:
        with open(VISIT_COUNT_FILE, 'r') as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0

def save_visits(count):
    with open(VISIT_COUNT_FILE, 'w') as file:
        file.write(str(count))

# Load the visit count from the file on start-up
visit_count = load_visits()

@app.route("/")
def current_time_in_moscow():
    global visit_count
    visit_count += 1  # Increment the visit count
    save_visits(visit_count)  # Save the updated count to the file
    moscow_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)
    return f"Current time in Moscow: {moscow_time.strftime('%Y-%m-%d %H:%M:%S')}"

@app.route("/visits")
def show_visits():
    return f"Total visits: {visit_count}"

if __name__ == "__main__":
    bottle.run(app, host="0.0.0.0", port=8080)
