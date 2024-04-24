"""Veriffy token is not expired or invalid."""
from fastapi import Request, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute

from app.auth.services import validate_token


class ValidateTokenRoute(APIRoute):
    """Token validation middleware."""
    def get_route_handler(self):
        original_route_handler = super().get_route_handler()
        async def custom_route_handler(request: Request):
            token = self.get_authtorization_header(request)
            if validation_response := validate_token(token):
                return validation_response
            return await original_route_handler(request)
        return custom_route_handler


    def get_authtorization_header(self, request: Request):
        """Check if authorization header is included."""
        try:
            return request.headers["Authorization"].split(" ")[1]
        except Exception as exc:
            raise HTTPException(detail="No Authorization header found.",
                                status_code=status.HTTP_404_NOT_FOUND) from exc
