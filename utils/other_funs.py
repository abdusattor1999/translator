async def chizirdan_ajrat(text):
    a, b = text.split("_")
    return [a, b]

async def dubledan_ajrat(text):
    a, b = text.split(":")
    return [a, b]