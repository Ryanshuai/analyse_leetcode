
# with open("lock/locked.txt", encoding="utf-8") as f:
#     lines = f.readlines()
#
# with open("lock/locked_formatted.txt", "w", encoding="utf-8") as f:
#     for a, b, c in zip(lines[::3], lines[1::3], lines[2::3]):
#         f.write(a[:-1]+"\t"+b[:-1]+"\t"+c)

with open("lock/locked_formatted.txt", encoding="utf-8") as f:
    lines = f.readlines()

lock = set()
for line in lines:
    number = int(line.split(".")[0])
    lock.add(number)

with open("todo/todo.txt", encoding="utf-8") as f:
    lines = f.readlines()

with open("todo/locked_todo.txt", "w", encoding="utf-8") as f:
    for line in lines:
        number = int(line.split(".")[0])
        if number in lock:
            f.write(line)

with open("todo/no_lock_todo.txt", "w", encoding="utf-8") as f:
    for line in lines:
        number = int(line.split(".")[0])
        if number not in lock:
            f.write(line)
