from abc import ABC, abstractmethod
from typing import AsyncIterator

from infrastructure.adapters.messages import Message


class Consumer(ABC):
    @abstractmethod
    async def listen(self, group: str) -> AsyncIterator[Message]:
        pass

    @abstractmethod
    async def commit(self) -> None:
        pass
