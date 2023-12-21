import json
from typing import AsyncIterator

from infrastructure.adapters.message_types import MessageType
from infrastructure.adapters.messages import Message
from infrastructure.ports import Consumer

import pika


class RabbitMQConsumer(Consumer):
    def __init__(
        self,
        host: str,
        port: int,
        virtual_host: str,
    ) -> None:
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=host,
                port=port,
                virtual_host=virtual_host,
            ),
        )
        self._channel = self._connection.channel()
        self._delivery_tag = None

    async def listen(self, group: str) -> AsyncIterator[Message]:
        for deliver, properties, body in self._channel.consume(queue=group, auto_ack=False):
            self._delivery_tag = deliver.delivery_tag
            yield Message(
                type=MessageType(properties.headers.get('type', 'unknown')),
                payload_type=properties.headers['payload_type'],
                payload=json.loads(body),
            )

    async def commit(self) -> None:
        if self._delivery_tag is not None:
            self._channel.basic_ack(delivery_tag=self._delivery_tag)
