"""
This file provides utility decorators for caching results
of calls to python functions.
"""

from typing import Any, Callable
from time import time
from functools import wraps
from threading import Lock


def cache_for(timeout_ms: int) -> \
        Callable[[Callable[Any, Any]], Callable[Any, Any]]:
    """
    Decorator to cache runs of a function for the given time
    period. All arguments and keyword arguments given to the
    function must be hashable.

    Before the timeout expired since the last run with the specified
    arguments set, last cached result is returned. Once the timeout
    is expired, next call to the decorated function results to an
    actual call to the underlying function and an update of cache.
    """

    timeout_s = timeout_ms / 1000

    def decorator(func: Callable[Any, Any]) -> Callable[Any, Any]:
        cached_result = {}
        expires_at = {}
        cache_lock = Lock()

        @wraps(func)
        def decorated(*args, **kwargs) -> Any:
            # Note: args and kwargs are assumed hashable, just like
            # the standard library (`funtools.lru_cache`) does
            frozen_args = tuple(args)
            frozen_kwargs = tuple(sorted(kwargs.items()))
            all_args = (frozen_args, frozen_kwargs)

            now = time()
            with cache_lock:
                if expires_at.get(all_args, now) <= now:
                    expires_at[all_args] = now + timeout_s
                    cached_result[all_args] = func(*args, **kwargs)
            return cached_result[all_args]

        return decorated

    return decorator
