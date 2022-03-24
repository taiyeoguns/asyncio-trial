"""Run module."""

import asyncio

from loguru import logger

import app

if __name__ == "__main__":
    logger.info(asyncio.run(app.run()))
