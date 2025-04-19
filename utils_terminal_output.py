from termcolor import colored

def print_green(message):
    print(colored(message, 'green'))

def print_red(message):
    print(colored(message, 'red'))

def print_yellow(message):
    print(colored(message, 'yellow'))

def print_brew_style(message):
    print(colored(f"==> {message}", 'cyan'))