"""App module."""


import asyncio
from typing import Awaitable, List, Optional

import httpx
from loguru import logger


def photos_list(num: Optional[int] = 2000) -> List[str]:
    """Return list of URLs for photos.

    Args:
        num (int, optional): Number of photo links to fetch. Defaults to 2000.

    Returns:
        List[str]: list of photo links
    """
    return [
        f"https://jsonplaceholder.typicode.com/photos/{n}" for n in range(1, num + 1)
    ]


async def process_photo(client: httpx.AsyncClient, photo_link: str) -> Awaitable:
    """Get each photo data asynchronously.

    Args:
        client (httpx.AsyncClient): AioHttp client object
        photo_link (str): photo link

    Returns:
        Awaitable: Photo json data
    """
    photo_data = await client.get(url=photo_link)
    logger.info(f"Photo data {photo_link}")
    return photo_data.json()


async def run(num: Optional[int] = 2000) -> Awaitable:
    """Runner to process photos.

    Args:
        num (int, optional): Number of photo links to fetch. Defaults to 2000.

    Returns:
        Awaitable: List of all photo data.
    """
    async with httpx.AsyncClient(timeout=30) as client:
        return await asyncio.gather(
            *[
                process_photo(client=client, photo_link=photo_link)
                for photo_link in photos_list(num=num)
            ],
        )
