import g4f

g4f.debug.logging = False # enable logging
g4f.check_version = False # Disable automatic version checking


def chat_completion(contraindications, text):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": f'''У меня противопоказания ({contraindications}), купил продукт с текстом на упаковке  "{text}" можно ли употребить, дай чёткий ответ (да или нет), не поясняя его содержание!'''}],
    )
    return response