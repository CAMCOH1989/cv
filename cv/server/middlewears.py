from aiohttp.web import Request, middleware, Response, HTTPForbidden

from cv.utils.utils import generate_visitor_id
from cv.utils.config import config


@middleware
async def check_cookies(request: Request, handler):
    if request.path.startswith('/admin'):
        admin_id = request.cookies.get("admin_id", "")
        if admin_id == config.ADMIN_TOKEN:
            return await handler(request)
        else:
            return HTTPForbidden()
    else:
        response: Response = await handler(request)
        visitor_id = request.cookies.get("visitor_id", "")
        if not visitor_id:
            visitor_id = await generate_visitor_id()
            response.set_cookie(name="visitor_id", value=visitor_id, path="/")

        return response
