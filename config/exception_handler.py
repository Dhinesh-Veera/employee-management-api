from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):

    # Let DRF handle known exceptions first
    response = exception_handler(exc, context)

    if response is not None:

        logger.warning(
            f"Handled exception: {exc} | View: {context.get('view')}"
        )

        return Response(
            {
                "success": False,
                "message": response.data.get("detail", response.data)
            },
            status=response.status_code
        )

    # Unexpected exceptions
    logger.exception("Unhandled exception occurred.")

    return Response(
        {
            "success": False,
            "message": "Something went wrong. Please try again later."
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )