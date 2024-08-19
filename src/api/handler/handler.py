from fastapi import HTTPException, status


class BaseHandler:
    """
    Base class for handlers, providing a centralized exception handling mechanism.
    """

    @staticmethod
    def handle_exceptions(func):
        """
        A decorator to handle exceptions that may occur during the execution of handler methods.

        This decorator wraps the handler method and catches any exceptions that are raised.
        If the exception is an `HTTPException`, it is re-raised to allow FastAPI to handle it and return the appropriate HTTP status code.
        For any other exception, it logs the error and raises an HTTP 500 Internal Server Error.

        Args:
            func: The handler method to be decorated.

        Returns:
            The wrapped handler method with exception handling.
        """

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
