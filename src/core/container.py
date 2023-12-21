from typing import Type

from core.settings import game_message_broker_settings, message_broker_settings

from dependency_injector import containers, providers

from infrastructure import adapters, ports


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    message_consumer: Type[ports.Consumer] = providers.Factory(
        adapters.RabbitMQConsumer,
        host=message_broker_settings.host,
        port=message_broker_settings.port,
        virtual_host=message_broker_settings.virtual_host,
    )  # type: ignore

    game_message_producer: Type[ports.Producer] = providers.Factory(
        adapters.RedisProducer,
        host=game_message_broker_settings.host,
        port=game_message_broker_settings.port,
        db=game_message_broker_settings.db,
        encoding=game_message_broker_settings.encoding,
    )  # type: ignore


container = Container()
