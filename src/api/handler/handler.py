from fastapi import HTTPException, status


class BaseHandler:
    def handle_exceptions(func):
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)

            except HTTPException as e:
                raise e
            except Exception as e:
                print(f"Error: {e}")
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="An error occurred while processing your request."
                )
        return wrapper
