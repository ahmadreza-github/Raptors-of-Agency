# pip install python-dotenv
from dotenv import load_dotenv
import os

load_dotenv()

EDEN_API_KEY = os.environ.get("EDEN_API_KEY")
if not os.environ.get("EDEN_API_KEY"):
    EDEN_API_KEY = input("Couldn't find EDEN_API_KEY, enter it\n>>> ")
else:
    print(f"successfully loaded Eden API key\nEdne API key is '{EDEN_API_KEY[:20]}'")

from dotenv import load_dotenv