"""
Modern async/await patterns for Python applications.
Demonstrates best practices for asynchronous programming.
"""

import asyncio
import aiohttp
import logging
from typing import List, Optional, Dict, Any
from contextlib import asynccontextmanager
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class APIResponse:
    """Structured response from API calls."""
    status: int
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None


class AsyncHTTPClient:
    """
    Async HTTP client with connection pooling, retries, and error handling.
    
    Example usage:
        async with AsyncHTTPClient() as client:
            response = await client.get("https://api.example.com/data")
    """
    
    def __init__(self, timeout: int = 30, max_connections: int = 100):
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.connector = aiohttp.TCPConnector(limit=max_connections)
        self.session: Optional[aiohttp.ClientSession] = None
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            connector=self.connector,
            timeout=self.timeout
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def get(self, url: str, **kwargs) -> APIResponse:
        """Make GET request with error handling and retries."""
        return await self._request("GET", url, **kwargs)
    
    async def post(self, url: str, json_data: Dict = None, **kwargs) -> APIResponse:
        """Make POST request with JSON data."""
        return await self._request("POST", url, json=json_data, **kwargs)
    
    async def _request(self, method: str, url: str, retries: int = 3, **kwargs) -> APIResponse:
        """Internal method for making HTTP requests with retries."""
        last_exception = None
        
        for attempt in range(retries + 1):
            try:
                async with self.session.request(method, url, **kwargs) as response:
                    if response.status < 400:
                        data = await response.json() if response.content_type == 'application/json' else await response.text()
                        return APIResponse(status=response.status, data=data)
                    else:
                        error_text = await response.text()
                        return APIResponse(status=response.status, error=error_text)
                        
            except Exception as e:
                last_exception = e
                if attempt < retries:
                    wait_time = 2 ** attempt  # Exponential backoff
                    logger.warning(f"Request failed (attempt {attempt + 1}), retrying in {wait_time}s: {e}")
                    await asyncio.sleep(wait_time)
                else:
                    logger.error(f"Request failed after {retries + 1} attempts: {e}")
        
        return APIResponse(status=0, error=str(last_exception))


async def fetch_multiple_urls(urls: List[str]) -> List[APIResponse]:
    """
    Fetch multiple URLs concurrently with semaphore for rate limiting.
    
    Args:
        urls: List of URLs to fetch
        
    Returns:
        List of API responses
    """
    semaphore = asyncio.Semaphore(10)  # Limit concurrent requests
    
    async def fetch_with_semaphore(client: AsyncHTTPClient, url: str) -> APIResponse:
        async with semaphore:
            return await client.get(url)
    
    async with AsyncHTTPClient() as client:
        tasks = [fetch_with_semaphore(client, url) for url in urls]
        return await asyncio.gather(*tasks, return_exceptions=True)


@asynccontextmanager
async def database_transaction():
    """
    Async context manager for database transactions.
    Ensures proper cleanup and rollback on errors.
    """
    # Mock database connection - replace with actual DB client
    db_connection = None
    transaction = None
    
    try:
        # db_connection = await get_db_connection()
        # transaction = await db_connection.begin()
        yield db_connection
        # await transaction.commit()
        logger.info("Transaction committed successfully")
        
    except Exception as e:
        # if transaction:
        #     await transaction.rollback()
        logger.error(f"Transaction rolled back due to error: {e}")
        raise
    finally:
        # if db_connection:
        #     await db_connection.close()
        pass


class AsyncTaskManager:
    """
    Manages long-running async tasks with cancellation and monitoring.
    """
    
    def __init__(self):
        self.tasks: Dict[str, asyncio.Task] = {}
    
    def start_task(self, task_id: str, coro) -> None:
        """Start a new background task."""
        if task_id in self.tasks:
            self.cancel_task(task_id)
        
        task = asyncio.create_task(coro)
        task.add_done_callback(lambda t: self._task_completed(task_id, t))
        self.tasks[task_id] = task
        logger.info(f"Started task: {task_id}")
    
    def cancel_task(self, task_id: str) -> bool:
        """Cancel a running task."""
        if task_id in self.tasks:
            task = self.tasks[task_id]
            if not task.done():
                task.cancel()
                logger.info(f"Cancelled task: {task_id}")
                return True
        return False
    
    def _task_completed(self, task_id: str, task: asyncio.Task) -> None:
        """Handle task completion."""
        if task_id in self.tasks:
            del self.tasks[task_id]
        
        if task.cancelled():
            logger.info(f"Task cancelled: {task_id}")
        elif task.exception():
            logger.error(f"Task failed: {task_id}, error: {task.exception()}")
        else:
            logger.info(f"Task completed successfully: {task_id}")
    
    async def wait_for_all(self, timeout: Optional[float] = None) -> None:
        """Wait for all tasks to complete."""
        if self.tasks:
            await asyncio.wait(self.tasks.values(), timeout=timeout)
    
    def cancel_all(self) -> None:
        """Cancel all running tasks."""
        for task_id in list(self.tasks.keys()):
            self.cancel_task(task_id)


# Example usage patterns
async def main():
    """Demonstrate async patterns in action."""
    
    # Pattern 1: Concurrent API calls
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]
    
    print("Fetching multiple URLs concurrently...")
    responses = await fetch_multiple_urls(urls)
    for i, response in enumerate(responses):
        print(f"URL {i+1}: Status {response.status}")
    
    # Pattern 2: Database transaction
    print("\nDatabase transaction example...")
    try:
        async with database_transaction() as db:
            # Simulate database operations
            print("Performing database operations...")
            await asyncio.sleep(0.1)  # Simulate work
    except Exception as e:
        print(f"Transaction failed: {e}")
    
    # Pattern 3: Task management
    print("\nTask management example...")
    task_manager = AsyncTaskManager()
    
    # Start some background tasks
    task_manager.start_task("task1", asyncio.sleep(2))
    task_manager.start_task("task2", asyncio.sleep(1))
    
    # Wait a bit then cancel one
    await asyncio.sleep(0.5)
    task_manager.cancel_task("task1")
    
    # Wait for remaining tasks
    await task_manager.wait_for_all(timeout=5)
    
    print("All async patterns demonstrated!")


if __name__ == "__main__":
    asyncio.run(main())
