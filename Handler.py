#import requests
#import json
URL = "https://api.telegram.org/bot497831974:AAGQf1mIsQlgIrFSFOH09i5g-mynyAfHlVc/getUpdates"

def handle_message(message, nickname="user"):
    if message[:5] == "Что в":
        day = message.split()[2][:len(message.split()[2])-1]
        return schedule[day]["lessons"]
    if message[:20] == "Когда заканчивается ":
        if messgage[22] == " ":
            endtime = lesson_time[int(messgage[21])][1]
        else:
            endtime = lesson_time[int(message[20:22])][1]
        return 'в '+str(endtime)
    if message[:16] == "Сколько уроков в":
        day = message.split()[3]
        number = len(schedule[day][lessons])
        return number
    if message[:6] == "Когда " and int(message[6]) < 10:
        starttime = lesson_time[int(message.split()[1]])][0]
        return 'в '+str(starttime)

if __name__ == "__main__":
    # dirty python magic, will talk about on the next lesson
    # just ignore for now

    nick = input("Enter your nickname: ")

    while True:
        msg = input("Your message: ")
        ans = handle_message(msg, nick)
        if msg[:5] == "Что в":
            print(*ans, sep = ', ')
        else:
            print(ans)
