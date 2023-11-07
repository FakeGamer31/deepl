import time

currentTime =time.localtime().tm_hour

if currentTime <= 12 and currentTime >= 6:
    print('Guten Morgen')
elif currentTime <= 18 and currentTime >= 12:
    print('Guten Tag')
else:
    print('Guten Abend')