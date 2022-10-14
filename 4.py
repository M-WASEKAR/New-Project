"""
Command needs to be executed as
python 3.py url
url is manfatory
"""
import requests
import sys

try:
    response = requests.get(sys.argv[1])
except IndexError:
    print("Please enter value for url")
    sys.exit(0)
# response.encoding = "utf-8"
file_read = response.text
print(file_read)
