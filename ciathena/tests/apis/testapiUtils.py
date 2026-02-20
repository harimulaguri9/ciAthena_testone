import asyncio
import json
from playwright.async_api import async_playwright

STREAM_URL = "https://ciathena-qa-be.customerinsights.ai/v1/query/stream"

async def fetch_final_stream_response(page, trigger_x=150, trigger_y=150, timeout=60000):
    """
    Captures the final 'raw_sql_result' from the streaming API endpoint.
    Handles partial/empty responses safely.
    """
    raw_sql_result = None
    future = asyncio.get_event_loop().create_future()

    async def handle_response(response):
        nonlocal raw_sql_result
        if STREAM_URL in response.url:
            try:
                text = await response.text()
                if not text.strip():
                    return  # ignore empty responses
                data = json.loads(text)
                # Only capture the final response
                if data.get("step") == "Final Response" and data.get("is_final") is True:
                    final_response = data.get("final_response", {})
                    raw_sql_result = final_response.get("raw_sql_result")
                    if raw_sql_result is not None and not future.done():
                        future.set_result(raw_sql_result)
            except json.JSONDecodeError:
                # Ignore partial/invalid JSON chunks
                pass
            except Exception as e:
                print("Error processing stream response:", e)

    # Listen for all responses
    page.on("response", handle_response)

    # Trigger the stream API
    await page.mouse.click(trigger_x, trigger_y)

    try:
        # Wait for the final raw_sql_result or timeout
        raw_sql_result = await asyncio.wait_for(future, timeout=timeout / 1000)
    except asyncio.TimeoutError:
        print("Timeout waiting for final stream response")
    finally:
        # Remove listener to prevent memory leaks
        page.remove_listener("response", handle_response)

    return raw_sql_result
