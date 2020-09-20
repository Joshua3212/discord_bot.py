import time

while True:
  f = open("demofile2.txt", "a")
  f.write("yikes.please..")
  f.close()
  time.sleep(5)
