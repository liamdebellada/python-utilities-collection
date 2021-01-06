mutate = (lambda character, position, string: "".join(list(map(lambda c: character if c[0] == position else c[1], list(enumerate(string))))))
print(mutate("c", 0, "test"))


