import asyncio
from g4f.client import AsyncClient


async def main():
    client = AsyncClient()

    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": "Say this is a test"
            }
        ],
        web_search=False
    )

    print(response.choices[0].message.content)


asyncio.run(main())