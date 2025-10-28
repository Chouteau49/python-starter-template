# Trigger CI: commit mineur pour relancer le pipeline
import sys

from app.application import Application
from app.core.settings import Settings


def main():
    settings = Settings()
    app = Application(settings)
    success = app.run()
    sys.exit(not success)


if __name__ == "__main__":
    main()
