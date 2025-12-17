# Playfab Account Creator by MamaMonkeSTAFF
# Этот скрипт создает кучу аккаунтов с использованием Custom ID и Playfab secret key.
# Использовать только на скид играх.
# Мамамонке не несет ответственности за использование этого скрипта.

import requests
import uuid
import time

TITLE_ID = "1" #Title ID
SECRET_KEY = "1" #Secret Key

API_URL = f"https://{TITLE_ID}.playfabapi.com/Server/LoginWithCustomID"

def create_account():
    custom_id = "ACC_" + uuid.uuid4().hex 
    payload = {
        "CustomId": custom_id,
        "CreateAccount": True,
        "TitleId": TITLE_ID
    }

    headers = {
        "Content-Type": "application/json",
        "X-SecretKey": SECRET_KEY
    }

    try:
        r = requests.post(API_URL, json=payload, headers=headers)

        if r.status_code == 200:
            data = r.json()
            playfab_id = data["data"]["PlayFabId"]
            print(f"PlayFabId={playfab_id}, CustomId={custom_id}")
            return True
        else:
            print("Ошибка:", r.text)
            return False

    except Exception as e:
        print("Ошибка запроса:", e)
        return False


def create_many_accounts(count):
    for i in range(count):
        create_account()
        #time.sleep(0.5)

    print(f"\nСоздано {count} аккаунтов.")


if __name__ == "__main__":


    n = int(input("Сколько аккаунтов создать?"))
    create_many_accounts(n)
