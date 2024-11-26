# code from here https://dev.to/zolor/automating-advent-of-code-2dlf
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os, sys

if len(sys.argv) != 2:
  print('Missing day number. Run e.g.:')
  print('python setup')
  sys.exit(2)
  
print("sys.argv:", sys.argv)

# input format: day
day = str(sys.argv[1])
path = str(os.getcwd()) + "\day" + day

try:
  os.mkdir(path)
except OSError:
  print("Creation of %s failed" % path)

lista = ["/part2.py", "/test.py", "/testinput.txt"]
for i in lista:
  open(path + i, 'a').close()
  
part1 = path + "/part1.py"
f = open(part1, "a")
f.write('data = [x.rstrip() for x in open("input.txt").readlines()]')
f.close()

chrome_options = Options()
chrome_options.add_argument("--headless")

from dotenv import load_dotenv
load_dotenv()

session_cookie = { "name": "session", 
                  "value":  os.getenv('AOC_SESSION_COOKIE')}

driver = webdriver.Chrome()

url = "https://adventofcode.com/2024/day/"
url_input = "https://adventofcode.com/2024/day/" + day + "/input"

driver.get(url)
driver.add_cookie(session_cookie)
driver.get(url_input)

content = driver.find_elements(By.TAG_NAME, "pre")

path = path + "/input.txt"
f = open(path, "a")
for e in content:
  f.write(e.text)
  
f.close()
driver.quit()

print(str(path), "stuff created")
