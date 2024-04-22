import fcntl
from functools import wraps
from threading import Lock
from typing import Callable


def increment(filename: str) -> None:
    with open(filename, 'rb+') as f:
        try:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            cur = int.from_bytes(f.read(), byteorder='little')
            f.seek(0)
            cur += 1
            f.write(cur.to_bytes(byteorder='little', length=(cur.bit_length() // 8 + 1)))
            f.truncate()  # Not necessary, as larger numbers take more bytes
        finally:
            # Note: will be unlocked anyway when the file is closed
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)


def increment_on_call(filename: str) -> Callable[[Callable, ...], Callable]:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def with_increment(*args, **kwargs):
            increment(filename)
            return func(*args, **kwargs)
        return with_increment
    return decorator
