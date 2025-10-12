def update(names: list[str]):

    if not names:
        print('Usage: "pxpm update <...packages | *>"')
        return

    names = list(set(names))