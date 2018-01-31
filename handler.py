#import requests
#import json
URL = "https://api.telegram.org/bot497831974:AAGQf1mIsQlgIrFSFOH09i5g-mynyAfHlVc/getUpdates"

def handle_message(message, nickname="user"):
    return()

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
