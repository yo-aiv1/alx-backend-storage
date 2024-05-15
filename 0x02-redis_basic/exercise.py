#!/usr/bin/env python3

"""redis basic usage"""


import redis
import uuid
from typing import Union, Callable


class Cache:
    def __init___(self) -> None:
        """
        initialize method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store method:
        takes a data argument and returns a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
