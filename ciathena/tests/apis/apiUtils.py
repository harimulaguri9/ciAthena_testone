from playwright.async_api import async_playwright
#
#
# BASE_URL = "https://ciathena-dev.customerinsights.ai"
#
#
# # ---------------------------------------
# # 1️⃣ Create API Request Context Separately
# # ---------------------------------------
#
#
# async def create_api_request_context(page):
#     """
#     Creates reusable API request context
#     using token from existing logged-in UI session.
#     """
#
#     # Step 1: Extract token from UI session
#     token = await page.evaluate(
#         "() => localStorage.getItem('access_token')"
#     )
#
#     if not token:
#         raise AssertionError(
#             "Access token not found. Ensure user is logged in."
#         )
#
#     auth_token = f"Bearer {token}"
#
#     # Step 2: Create API request context
#     request_context = await page.context.request.new_context(
#         base_url=BASE_URL,
#         extra_http_headers={
#             "accept": "application/json",
#             "authorization": auth_token,
#             "content-type": "application/json"
#         }
#     )
#
#     return request_context
#
#
#
# # ---------------------------------------
# # 2️⃣ Profile API Method
# # ---------------------------------------



#88888888888888888888888888888888888888888888888888888888888888888888888888888
async def get_user_id(api_context):
    response = await api_context.get("/profile/me")
    assert response.ok, "Failed to get profile"

    data = await response.json()
    user_id = data["id"]
    print("✅ User ID:", user_id)
    return user_id

async def create_session(api_context, user_id):
    payload = {
        "app_name": "mmm",
        "user_id": user_id,
        "title": "Automation Session"
    }

    response = await api_context.post("/v1/sessions", data=payload)

    assert response.ok, "Session creation failed"

    data = await response.json()

    session_id = data["session_id"]

    print("✅ Session ID:", session_id)

    return session_id

