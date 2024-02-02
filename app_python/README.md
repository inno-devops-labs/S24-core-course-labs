# Simple Flask app
The idea of the app is really simple, it just shows the current time in Moscow

# Set up
1. Firstly it is preferable to use virtual environment for `python`:
```bash
python3 -m venv env
```
2. Activate the virtual environment
```bash
source env/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the application
```bash
python app.py
```

# Testing
All tests can be found in the directory `tests`, to run them use the following command:
```bash
pytest tests/*.py
```

# Stack
- Python
- Flask
- Pytests
- BeautifulSoup (for tests)
- Requests (for tests)
– Logging (standard library)