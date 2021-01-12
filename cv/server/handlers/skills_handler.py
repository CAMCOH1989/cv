from aiohttp.web import json_response, HTTPOk, HTTPClientError
from sqlalchemy import select

from cv.server.handlers.base import BaseView


class SkillsView(BaseView):
    async def get(self):
        test_skills = [
            ["Python", 91],
            ["PostgreSQL", 81],
            ["Mongo", 71],
            ["Linux", 61],
            ["Python", 51],
            ["IN", 41],
            ["sadas", 31],
            ["zxcxzc", 21],
            ["xczxc", 11],
            ["Vue", 1]]
        render_data = {"skills": test_skills}
        print(await self.pg.fetchrow(select()))
        return json_response(render_data)

    async def post(self):
        skill_id = int(self.request.match_info.get("skill_id", 0))
        post_data = await self.request.post()
        print(post_data)
        if skill_id:
            print("update skill")
        else:
            skill_id = 1
            print("create skill")
        if skill_id:
            return HTTPOk()
        else:
            return HTTPClientError()
