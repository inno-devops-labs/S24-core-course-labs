# Python web app that displays current MSK time

I decided to make it as simple as possible: no JavaScript, only the time that was recorded on the moment of the request. This way it's easier to get the data a user needs faster and without any unnecessary data.

# Framework

FastAPI framework was chosen, since it's minimal and used a lot in the industry. FastAPI allowed the use of HTMLResponse to directly display the time on a user's browser.

Formatted the datetime, so it doesn't display the exact time, but only hours, minutes, and seconds.

# Running and Testing

Uvicorn was used to run the app and Firefox to test it. The time updates upon refreshing.
