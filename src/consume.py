import asyncio
import logging
from pathlib import Path

from core.container import container
from core.settings import message_broker_settings


BASE_DIR = Path(__file__).parent

logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler(BASE_DIR / 'consume.log', encoding='utf-8'))


async def main() -> None:
    message_consumer = container.message_consumer()
    game_message_producer = container.game_message_producer()
    async for message in message_consumer.listen(message_broker_settings.game_events_queue):
        try:
            game_id = message.payload.pop('game_id')
            await game_message_producer.publish(game_id, message)
            await message_consumer.commit()
        except KeyError:
            logger.error(f'Invalid message: {message}')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
