with open("state/done.txt", encoding="utf-8") as f:
    lines = f.readlines()

with open("state/real_done.txt", "w", encoding="utf-8") as f:
    for line in lines:
        end = line.split(" ")[-1]
        end = end.split("\t")[-1]
        if end == "1\n" and "困难" not in line:
            f.write(line)




