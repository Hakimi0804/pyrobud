import asyncio
from typing import Callable, TypeVar, Any

Result = TypeVar("Result")


async def run_sync(func: Callable[..., Result], *args: Any, **kwargs: Any) -> Result:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, lambda: func(*args, **kwargs))
