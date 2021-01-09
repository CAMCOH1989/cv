from aiohttp.web import Request, middleware, Response, HTTPForbidden


@middleware
async def check_cookies(request: Request, handler):
    if request.path.startswith('/admin'):

        return await handler(request)
    else:
        response: Response = await handler(request)
        visitor_id = response.cookies.get("visitor_id", "")
        if not visitor_id:
            response.set_cookie(name="visitor_id", value="asdasdasd", path="/")

        return response
