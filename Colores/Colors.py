from sys import stdout


def red():
    RED = "\033[1;31m"
    stdout.write(RED)


def cyan():
    CYAN = "\033[1;36m"
    stdout.write(CYAN)


def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)


def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)


def bold():
    BOLD = "\033[1m"
    stdout.write(BOLD)


def reset():
    RESET = "\033[0m"
    stdout.write(RESET)
