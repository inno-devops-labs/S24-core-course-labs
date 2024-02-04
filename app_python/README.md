# Python application for displaying Moscow time
## Overview
The server simply responds to one root route and returns an HTML page that is styled to display time in the middle of the screen and (for convenience) it includes a JS script to refresh the page automatically every second. For getting the time, it uses Russian NTP servers that can calculate time reliably by accounting the RTT to servers and back. If for some reason, NTP servers are unavailable, the server fallbacks to using local time. For the timezone conversion, the server assumes that the environment already has Europe/Moscow timezone defined. 
# Launch instructions
After installing the requirements, the project can be started as any other flask application.
Commands for launching from app\_python/ folder
```
pip install -r requirements.txt
flask --app main run
```

