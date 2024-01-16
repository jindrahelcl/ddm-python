from inputimeout import inputimeout, TimeoutOccurred

inventar = {"klic": False,
            "penize": 56,
            "motyka": True}


if inventar["motyka"]:
    print("mam motyku")

if inventar["klic"]:
    print("mam klic")
else:
    print("nemam klic")

