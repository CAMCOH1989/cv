from datetime import datetime, date

from aiohttp.web import json_response

from cv.server.handlers.base import BaseView


class CVView(BaseView):
    async def get(self):
        age = (date.today() - date(1989, 11, 20))
        age = int(age.days / 365.25)
        print(age)

        if await self.locale == "ru":
            if 5 <= age <= 20:
                age_postfix = "лет"
            elif age % 10 == 1:
                age_postfix = "год"
            elif age % 10 in [2, 3, 4]:
                age_postfix = "года"
            elif age % 10 in [5, 6, 7, 8, 9, 0]:
                age_postfix = "лет"
            else:
                age_postfix = "лет"

            render_data = {"cv": {
                "surName": "Захарчук",
                "firstName": "Василий",
                "middleName": "Владимирович",
                "birthDate": "20 ноября 1989",
                "age": f"{age} {age_postfix}",
                "experience": [
                    "11 лет инженер на телевидении",
                    "с мая 2018 бекэнд разраотчик в KamaGames Studio"
                ],
                "personalData": "",
                "education": "",
                "languages": [
                    {
                        "language": "русский",
                        "experience": "носитель",
                    },
                    {
                        "language": "английский",
                        "experience": "C1",
                    },
                    {
                        "language": "немецкий",
                        "experience": "базовый",
                    },
                    {
                        "language": "японский",
                        "experience": "базовый",
                    },
                ],
                "sex": "муж."
            }}
        else:
            if 2 <= age <= 20:
                age_postfix = "years"
            elif age % 10 == 1:
                age_postfix = "year"
            else:
                age_postfix = "years"
            render_data = {"cv": {
                "surName": "Zakharchuk",
                "firstName": "Vasily",
                "middleName": "Vladimirovich",
                "birthDate": "20 november 1989",
                "age": f"{age} {age_postfix} old",
                "experience": [
                    "11 years as a TV engineer",
                    "backend developer at KamaGames Studio since may 2018",
                ],
                "personalData": "",
                "education": "",
                "languages": [
                    {
                        "language": "russian",
                        "experience": "native",
                    },
                    {
                        "language": "english",
                        "experience": "C1",
                    },
                    {
                        "language": "german",
                        "experience": "beginner",
                    },
                    {
                        "language": "japanese",
                        "experience": "beginner",
                    },
                ],
                "sex": "male",
            }}

        international_data = {
            "phone": "+7 903 99 74 20",
            "email": "camcoh1989@gmail.com",
            "telegram": "@camcoh1989",
            "skype": "camcoh1989_1",
        }
        render_data["cv"].update(international_data)

        return json_response(render_data)
