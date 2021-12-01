from flask import Flask
from app.api import api
import logging

logging.basicConfig(
                    format="%(levelname)s - %(asctime)s - %(filename)s - %(message)s - line	%(lineno)d ",
                    level=logging.INFO
                    )

app = Flask(__name__)
app.register_blueprint(api)
app.config['JSON_SORT_KEYS'] = False



if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 5000, debug = True)
