import lhapp_class
import os
from wmip import get_ip
import schedule
import time


def main():
    # Get keys from env
    CONSUMER_KEY = os.environ['CONSUMER_KEY']
    CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
    ACCESS_KEY = os.environ['ACCESS_KEY']
    ACCESS_SECRET = os.environ['ACCESS_SECRET']

    # New Instance
    my_app = lhapp_class.Lhapp(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

    # Get DM List
    try:
        dm_list = my_app.get_dm_list()
    except Exception as err:
        my_app.log_write('log.txt', err)
        return None

    # Check queue length, break if len == 0
    try:
        message = dm_list[0]._json
    except IndexError:
        my_app.log_write('log.txt', 'QLEN: Zero.')
        return None

    # Extract relevant fields
    message_id = message['id']
    sender_id = message['message_create']['sender_id']
    message_text = message['message_create']['message_data']['text']

    # Debugging message
    my_app.log_write('log.txt', f"SNDR: {sender_id} | MSGID: {message_id} | MSGTXT: {message_text}")

    # if sender_id is 971535803338973185 and message_text is @ip get_ip() and destroy query message
    if sender_id == '<Your sender_id>' and message_text == '<Your hotword>':
        # Destroy message_id
        my_app.destroy_dm(message_id)
        # get_ip
        try:
            ip_address = get_ip()
        except Exception as err:
            ip_address = f'Unable to contact ipify.org because {err}.'
        # send message with IP address
        my_app.send_dm(sender_id, ip_address)
        # Debugging message
        my_app.log_write('log.txt', f"SNDR: {sender_id} | MSGTXT: {ip_address}")

if __name__ == "__main__":
    # Schedule a check of Twitter DM queue every 5 minutes
    schedule.every(5).minutes.do(main)
    # Enter event loop
    while True:
        schedule.run_pending()
        time.sleep(1)
