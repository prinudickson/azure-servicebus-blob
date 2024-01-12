import os
from azure.servicebus import ServiceBusClient

from dotenv import load_dotenv

load_dotenv()

servicebus_connection_str = os.environ['SERVICEBUS_SEND_CONNECTION_STR']
servicebus_client = ServiceBusClient.from_connection_string(conn_str=servicebus_connection_str)

print(servicebus_client.fully_qualified_namespace)

with servicebus_client:
    queue_receiver = servicebus_client.get_queue_receiver(queue_name=os.environ['QUEUE_NAME_SEND'])
    print(queue_receiver._auth_uri)

servicebus_client.close()

print(servicebus_client)
