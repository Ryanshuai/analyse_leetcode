seen = set()
with open("top100/amazon.txt", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    number = int(line.split(".")[0])
    seen.add(number)

with open("todo/todo.txt", encoding="utf-8") as f:
    lines = f.readlines()

with open("locked_todo.txt", "w", encoding="utf-8") as f:
    for line in lines:
        number = int(line.split(".")[0])
        if number not in seen:
            f.write(line)
