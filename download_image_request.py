import requests
import os

print('Beginning file download with requests')

# 파일 저장할 폴더 경로
SHEET_PATH = os.path.join(os.path.dirname(__file__), "sheets")

# 폴더가 없으면 만들어준다
if not os.path.exists(SHEET_PATH):
    os.makedirs(SHEET_PATH)

url = 'https://docs.google.com/spreadsheets/d/16mohp33sM4PwnS0sJ6Rk1sgdoR7H2AXWjPzgKgP0iwo/edit?usp=sharing'
r = requests.get(url)

originNames = url.split("/")
renameFile = originNames[len(originNames) - 1]

with open(os.path.join(SHEET_PATH, renameFile), 'wb') as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)