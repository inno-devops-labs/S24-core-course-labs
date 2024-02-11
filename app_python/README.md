## Python web app

This is simple python flask web application for obtaining current time in Europe/Moscow timezone

Install dependencies:
```bash
pip install -r requirements.txt
```
Start server:
```bash
python main.py
```
This will start a local web server, and you can access the current time in Moscow by going to http://127.0.0.1:5000/ in your web browser.

Example result:
```The current time in Moscow is 2024-02-06 15:40:22```


Additionaly you can run unittests by command:
```bash
python test.py
```

### Running with docker

You may use already built image:

```bash
docker pull pgrammer/app_python
docker run -p 5000:5000 pgrammer/app_python
```

Or build it yourself:

```bash
docker build -t app_python .
docker run -p 5000:5000 app_python
```

Now you can see Moscow time at http://localhost:5000