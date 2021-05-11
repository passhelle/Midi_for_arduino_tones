tones_dict = dict()
with open("for_dict.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = line.split("\t")
        tones_dict[line[0]] = line[1]
