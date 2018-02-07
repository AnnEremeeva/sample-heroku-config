#import requests
#import json
#import emotions
URL = "https://api.telegram.org/bot497831974:AAGQf1mIsQlgIrFSFOH09i5g-mynyAfHlVc/getUpdates"

def handle_message(message, nickname="user"):
    a = []
    if message == 'ПОЗИТИВ!':

        return'igbbhreb'
    elif message == 'БОЛЬ!':
        return'gfbnrthw'
    else:
        return 'У нас такого нет('

if __name__ == "__main__":
    # dirty python magic, will talk about on the next lesson
    # just ignore for now

    nick = input("Как вас называть?")

    while True:
        msg = input("Если вы хотите позитивный смайлик, то напишите: 'ПОЗИТИВ!'. Если вы хотите отрицательный смайлик, то напишите: 'БОЛЬ!'")
        ans = handle_message(msg, nick)
        print(ans)
