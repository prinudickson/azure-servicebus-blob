import os
import time
import asyncio
from azure.servicebus.aio import ServiceBusClient

from dotenv import load_dotenv
from reactivex.subject import Subject

load_dotenv()

servicebus_connection_str = os.environ['SERVICEBUS_SEND_CONNECTION_STR']
QUEUE_NAME = os.environ['QUEUE_NAME_SEND']

subject = Subject()
loop = asyncio.get_event_loop()

async def run():
    time_before_refreshing_receiver = 3600
    while True:  
    # create a Service Bus client using the connection string
        try:
            async with ServiceBusClient.from_connection_string(
                conn_str=servicebus_connection_str,
                logging_enable=True) as servicebus_client:

                async with servicebus_client:
                    # get the Queue Receiver object for the queue
                    receiver = servicebus_client.get_queue_receiver(queue_name=QUEUE_NAME)
                    async with receiver:
                        received_msgs = await receiver.receive_messages(max_wait_time=5) #, max_message_count=30)
                        for msg in received_msgs:
                            print("Received: " + str(msg))
                            # complete the message so that the message is removed from the queue
                            await receiver.complete_message(msg)
        except Exception as e:
                    print(
                        f"Failed when trying to connect to the ServiceBusClient with error: {e}"
                    )

                # Closes connection if an error occures or if time_before_refreshing_receiver has passed
        finally:
            await servicebus_client.close()
            print("Successfully closed the ServiceBusClient")

#loop.create_task(run())
asyncio.run(run())