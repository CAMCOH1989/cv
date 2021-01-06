from aiohttp.web import json_response, HTTPOk
from sqlalchemy import select

from cv.server.handlers.base import BaseView


class SkillsView(BaseView):
    async def get(self):
        test_skills = [["Python", 9], ["Vue", 1]]
        render_data = {"skills": test_skills}
        # print(await self.pg.fetchrow(select()))
        return json_response(render_data)

    async def post(self):
        post_data = await self.request.post()
        print(post_data)
        return HTTPOk()
