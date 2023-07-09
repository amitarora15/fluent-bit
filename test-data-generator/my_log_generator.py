import time
import random
while True:
  level = ["INFO", "ERROR"]
  log_message='12/02/2002T12:00:00 server.com '
  r = random.randint(0, 1)
  log_message=log_message+level[r]+" my new message\n"
  with open('../test-data/my_log.log','a') as f:
    f.write(log_message)
  time.sleep(4)