import datetime
from time import sleep

for i in range(100):
    file_builder = open("logger.txt", "a+")
    file_builder.write(f'{datetime.datetime.now()}\n')
    file_builder.close()

    sleep(2.0)
