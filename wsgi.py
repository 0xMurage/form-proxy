from flask import Flask
from dotenv import load_dotenv, dotenv_values


def create_app():
    load_dotenv()  # explicit call for prod use

    app = Flask(__name__)

    app.config.from_mapping(dotenv_values())

    return app


if __name__ == "__main__":
    create_app().run()
