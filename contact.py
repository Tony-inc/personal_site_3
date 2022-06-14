import requests, os


class Contact:
    @staticmethod
    def send_message(data):
        return requests.post(os.getenv('END_POINT'),
                             auth=('api', os.getenv('KEY')),
                             data={'from': os.getenv('MY_EMAIL'),
                                   'to': os.getenv('MY_EMAIL'),
                                   'subject': 'Site Response',
                                   'text': f"Name: {data['name']}\nEmail: {data['email']}\nMessage: {data['message']}"})