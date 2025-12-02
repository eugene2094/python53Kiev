import json
from datetime import datetime


def load_chat(filename='chat.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("File error!")
        return []


def save_chat(messages, filename='chat.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)


def add_message(messages):
    author = input("Name - ")
    text = input("text - ")
    time = datetime.now().strftime("%Y-%m-%d %H:%M")

    message = {
        "auther": author,
        "time": time,
        "text": text
    }
    messages.append(message)
    save_chat(messages)
    print("Add new sms!")


def show_messages(messages):
    print("All dialog")
    if not messages:
        print("No sms!")
        return

    for msg in messages:
        print(f"{msg['time']} | {msg['auther']}: {msg['text']}")


messages = load_chat()
add_message(messages)
show_messages(messages)

add_message(messages)
show_messages(messages)
