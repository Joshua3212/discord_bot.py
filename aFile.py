import time

while True:
  f = open("demofile2.txt", "a")
  f.write("more content please")
  f.close()
  time.sleep(5)
