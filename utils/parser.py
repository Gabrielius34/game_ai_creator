def analizuoti_aprasyma(aprasymas):
    aprasymas = aprasymas.lower()
    parametrai = {"engine": "pygame"}

    if "3d" in aprasymas or "erdvė" in aprasymas:
        parametrai["engine"] = "ursina"
    if "šviesa" in aprasymas or "žibintuvėlis" in aprasymas:
        parametrai["light"] = True
    if "priešai" in aprasymas or "priešas" in aprasymas:
        parametrai["enemies"] = True
    if "labirintas" in aprasymas:
        parametrai["maze"] = True

    return parametrai