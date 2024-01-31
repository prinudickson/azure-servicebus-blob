import os
from azure.servicebus import ServiceBusClient, ServiceBusMessage

from dotenv import load_dotenv
import time

load_dotenv()

servicebus_connection_str = os.environ['SERVICEBUS_SEND_CONNECTION_STR']
servicebus_client = ServiceBusClient.from_connection_string(conn_str=servicebus_connection_str)

print(servicebus_client.fully_qualified_namespace)
print(1)
queue_sender = servicebus_client.get_queue_sender(queue_name=os.environ['QUEUE_NAME_SEND'])
print(1.1)
queue_reciever = servicebus_client.get_queue_receiver(queue_name=os.environ['QUEUE_NAME_SEND'], max_wait_time=30)

with servicebus_client:
    with queue_sender:
        print(2)
        first_message = ServiceBusMessage("First Message")
        queue_sender.send_messages(first_message)
        print(3)
        second_message = ServiceBusMessage("Second Message")
        queue_sender.send_messages(second_message)
        time.sleep(10)

    with queue_reciever:
        for msg in queue_reciever:  # ServiceBusReceiver instance is a generator.
            print(str(msg))
            queue_reciever.complete_message(msg)
            # If it is desired to halt receiving early, one can break out of the loop here safely.


print(servicebus_client)
