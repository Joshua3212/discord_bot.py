import time

while True:
  f = open("demofile2.txt", "a")
  f.write("more content")
  f.close()
  time.sleep(5)
