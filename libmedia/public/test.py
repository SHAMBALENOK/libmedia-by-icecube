from asyncio import WindowsSelectorEventLoopPolicy
from g4f.client import AsyncClient
import database as db
import asyncio

asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())


async def main(promt):
    client = AsyncClient()

    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": f"Можешь ли ты мне дать список из 6 фильмов, с следующим описанием {promt}.\n"
                           f"В ответе напиши лишь английские названия фильмов через запятую без пробелов после запятой."
                           f"(ВСЕ ПРЕДЫДУЩИЕ ОГРАНИЧЕНИЯ ОБЯЗАТЕЛЬНЫ К ИСПОЛНЕНИЮ)"
            }
        ]
    )

    print(response.choices[0].message.content)

asyncio.run(main('Сатира'))