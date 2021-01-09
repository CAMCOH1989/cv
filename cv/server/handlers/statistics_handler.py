from datetime import datetime

from aiohttp.web import json_response, HTTPOk
from sqlalchemy import select, func
from user_agents import parse

from cv.server.handlers.base import BaseView
from cv.models import visits_table


class StatisticsView(BaseView):
    async def get(self):
        locations_query = select([
            func.sum(visits_table.c.id),
            visits_table.c.location
        ]).group_by(visits_table.c.location)
        locations = await self.pg.fetch(locations_query)

        os_query = select([
            func.sum(visits_table.c.id),
            visits_table.c.os
        ]).group_by(visits_table.c.os)
        oses = await self.pg.fetch(os_query)

        render_data = {"statistics": {
            "locations": [],
            "oses": [],
        }}

        for location in locations:
            render_data["statistics"]["locations"].append(dict(location))

        for os in oses:
            render_data["statistics"]["oses"].append(dict(os))

        return json_response(render_data)

    async def post(self):
        post_data = await self.request.json()
        user_agent = self.request.headers.get("user-agent")
        visits_que = visits_table.insert(
            {
                "ip": self.request.remote,
                "user_agent": user_agent,
                "visit_datetime": datetime.now(),
                "location": post_data.get("location"),
                "os": parse(user_agent).get_os(),
            }
        )
        await self.pg.execute(visits_que)
        return HTTPOk()
