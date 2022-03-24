"""Test app."""
import pytest

from app import run


@pytest.mark.asyncio
async def test_run():
    """Test run."""
    result = await run(num=1)
    assert isinstance(result, list)
    assert len(result) == 1
