from g4f.client import Client


def get_movie(promt):
    client = Client()
    response = client.chat.completions.create(
        model="qwen-2.5-coder-32b",
        messages=[{"role": "user", "content": f"Можешь ли ты мне дать список фильмов и сериалов, с следующим описанием {promt}, "
                                              f"leaving only name, in the one string"}],
        web_search=False
    )
    # print(response.choices[0].message.content)

    return response.choices[0].message.content


print(get_movie('film about future '))
