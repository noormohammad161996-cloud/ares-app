def get_data():
    names = []
    with open("names.txt", "r") as file:
        for line in file:
            name = line.strip()
            if name:
                names.append(name)
    return names
