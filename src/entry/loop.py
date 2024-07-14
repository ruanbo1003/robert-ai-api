
import time
from libs.env import Env


def main():
    print("POSTGRES_URL:", Env.POSTGRES_URL)

    while True:
        print("...")
        time.sleep(60)


if __name__ == '__main__':
    main()
