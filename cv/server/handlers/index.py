from aiohttp.web import Response, HTTPFound, HTTPNotFound, HTTPOk
from sqlalchemy import select

from cv.server.handlers.base import BaseView


class IndexView(BaseView):
    async def get(self):
        render_data = {}
        print(await self.pg.fetchrow(select()))
        template = self.jinja_env.get_template("downloader.html")
        response = Response(
            body=template.render(render_data),
            headers={'Content-Type': 'text/html'}
        )
        return response

    async def post(self):
        post_data = await self.request.post()
        print(post_data)
        return HTTPOk()
