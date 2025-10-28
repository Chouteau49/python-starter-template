# Trigger CI: commit mineur pour relancer le pipeline
import sys

from app.application import Application


def main():
    app = Application()
    success = app.run()
    sys.exit(not success)


if __name__ == "__main__":
    main()
