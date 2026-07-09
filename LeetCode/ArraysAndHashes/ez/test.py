
frq = {}

frq["Hola"] = 0

if "Meow" in frq:
    frq["Meow"] = frq.get("Meow") +1
else:
    frq["Meow"] = 0

print(f" The dict has {frq}")
