# import logging
#
# from .config import PORT
# from .logger import setup_logging
# from .router import router
# from flask import Flask
#
# from waitress import serve
#
# app = Flask(__name__)
# app.register_blueprint(router)
#
# if __name__ == '__main__':
#     setup_logging()
#     logger = logging.getLogger(__name__)
#     serve(app, host='0.0.0.0', port=PORT)
