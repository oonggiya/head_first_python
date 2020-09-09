from datetime import datetime
import random
import time



for i in range(10):
    
    right_this_minute = datetime.today().second

    print(right_this_minute)


    wait_time = random.randint(1,3)
    time.sleep(wait_time)
    
