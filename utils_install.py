import os

def install_dependencies():
    print("==> Installing necessary dependencies...")
    os.system("pip install -r requirements.txt")
    print("==> Dependencies installed successfully.")