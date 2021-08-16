from tags import tags

n = len(tags)

tags_k = list(tags.keys())
tags_v = list(tags.values())

for i in range(n):
    for j in range(n):
        if i != j:
            intersection = set(tags_v[i]) & set(tags_v[j])
            # if len(intersection) > 0.05 * min(len(tags_v[i]), len(tags_v[j])):
            if len(intersection) > 10:
                print(tags_k[i], len(tags_v[i]), tags_k[j], len(tags_v[j]), '\t-->', len(intersection))
# print(set(tags["bfs"]) - set(tags["dfs"]))
print(set(tags["dfs"]) & set(tags["dp"]))

# num = 351
# for k, v in tags.items():
#     if num in v:
#         print(k)
