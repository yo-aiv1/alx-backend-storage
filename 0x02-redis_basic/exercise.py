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

    def get(self, key: str, fn: Callable = None) -> Union[str,
                                                          bytes, int, float]:
        """
        get method:
        take a key string argument and callback for converting
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            data = fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        automatically parametrize Cache.get
        """
        return self.get(key, lambda x: x.decode("utf-8") if x else None)

    def get_int(self, key: str) -> Union[int, None]:
        """
        automatically parametrize Cache.get
        """
        return self.get(key, lambda x: int(x) if x else None)
