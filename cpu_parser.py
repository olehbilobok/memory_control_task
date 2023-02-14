import psutil
import requests
import time
import machineid


def get_data(url):
    return requests.get(url)


def post_data(url, data):
    requests.post(url, json=data)


def put_data(url, data):
    requests.put(url, json=data)


def get_machine_id():
    return machineid.id()


def main():

    url = 'http://127.0.0.1:8080/api/memory'
    machine_id = get_machine_id()
    while True:
        ram_consumption = psutil.virtual_memory()

        if ram_consumption:
            if ram_consumption[2] > 30:
                db_data = get_data(f"{url}/{machine_id}")

                body = {
                    "consumption": ram_consumption[2]
                }

                if not db_data:
                    body['id'] = machine_id
                    post_data(url, body)
                else:
                    put_data(f"{url}/{machine_id}", body)

        time.sleep(20)


if __name__ == '__main__':
    main()
