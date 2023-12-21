import json

import aioredis

from infrastructure.adapters.messages import Message
from infrastructure.ports import Producer


class RedisProducer(Producer):
    def __init__(
        self,
        host: str,
        port: int,
        db: int,
        encoding: str,
    ) -> None:
        self._redis = aioredis.Redis(
            host=host,
            port=port,
            db=db,
            encoding=encoding,
        )

    async def publish(self, group: str, message: Message) -> None:
        await self._redis.publish(
            group,
            json.dumps(
                {
                    'type': message.type.value,
                    'payload_type': message.payload_type,
                    'payload': message.payload,
                },
            ),
        )
