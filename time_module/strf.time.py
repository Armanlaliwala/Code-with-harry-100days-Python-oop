import time
t = time.localtime()
# formatted_time= time.strftime("%y-%m-%d %h:%m:%s",t)
formatted_time = time.strftime("%y-%m-%d %H:%M:%S", t)
formatted_time = time.strftime("%d-%m-%y %H:%M:%S", t)
print(formatted_time)