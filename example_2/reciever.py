import os
import time
import json
import asyncio
from azure.servicebus.aio import ServiceBusClient
from icecream import ic
from dotenv import load_dotenv
from reactivex.subject import Subject

load_dotenv()

servicebus_connection_str = os.environ['SERVICEBUS_SEND_CONNECTION_STR']
QUEUE_NAME = os.environ['QUEUE_NAME_SEND']

subject = Subject()


async def run():
    time_before_refreshing_receiver = 10
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
                        for message in received_msgs:
                            ic(format(message))
                            print("Receiving: {}".format(message))
                            print("Time to live: {}".format(message.time_to_live))
                            print("Sequence number: {}".format(message.sequence_number))
                            print("Enqueued Sequence number: {}".format(message.enqueued_sequence_number))
                            print("Partition Key: {}".format(message.partition_key))
                            print("Application Properties: {}".format(message.application_properties))
                            print("Delivery count: {}".format(message.delivery_count))
                            print("Message ID: {}".format(message.message_id))
                            print("Locked until: {}".format(message.locked_until_utc))
                            print("Lock Token: {}".format(message.lock_token))
                            print("Enqueued time: {}".format(message.enqueued_time_utc))

                            print("Received: " + str(message))
                            #data = json.loads(str(msg))
                            ic(type(message))
                            ic(message)
                            #ic(data)

                            # complete the message so that the message is removed from the queue
                            await receiver.complete_message(message)
                # async with servicebus_client.get_queue_receiver(
                #     queue_name=QUEUE_NAME) as receiver:
                #     async for message in receiver:
                #         data = json.dumps(message)
                #         ic(data)
                #         try:
                #             subject.on_next(data)
                #             ic(subject)
                #         except ValueError:
                #             print("Value Error Blahh")

                #         await receiver.complete_message(message)
                             

                    # async for message in receiver:
                    #     data = json.loads(str(message))
                    #     try:
                    #         subject.on_next(data)
                    #     except ValueError:
                    #         ic(
                    #             f"Failed to process message with payload: [{str(message)}]\n "
                    #         )
                    #     await message.complete()
        except Exception as e:
                    print(
                        f"Failed when trying to connect to the ServiceBusClient with error: {e}"
                    )

                # Closes connection if an error occures or if time_before_refreshing_receiver has passed
        finally:
            await servicebus_client.close()
            print("Successfully closed the ServiceBusClient")

#loop.create_task(run())
#asyncio.run(run())

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
loop.close()