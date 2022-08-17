"""main"""
from logging import config

config.fileConfig("logging.conf", disable_existing_loggers=False)

def main():
    """main"""
    print("hello world!")

if __name__ == "__main__":
    main()
