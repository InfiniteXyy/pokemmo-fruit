TYPES = ["异常果", "恢复果", "亲密度果", "努力果", "临时属性果", "方块原料果", "plus果", "减伤果"]


def type_of_fruit(description):
    if "HP果" in description or "PP果" in description:
        return TYPES[1]
    if "亲密果" in description:
        return TYPES[2]
    if "努力" in description:
        return TYPES[3]
    if "方块原料" in description:
        return TYPES[5]
    if "plus" in description:
        return TYPES[6]
    if "减受" in description:
        return TYPES[7]
    for i in ["临时", "随机", "加成", "一次先手", "回复", "反伤"]:
        if i in description:
            return TYPES[4]
    else:
        return TYPES[0]


class Fruit:

    def __init__(self, name, description, seeds):
        self.name = name
        self.description = description
        self.seeds = seeds
        self.fruit_type = type_of_fruit(self.description)

    def __str__(self):
        return "{}: {}\t {}\t {}".format(self.name, self.description, self.seeds, self.fruit_type)

    def get_type(self):
        return self.fruit_type


class Seed:
    types = ["酸", "甜", "苦", "辣", "涩"]
    degrees = ["超", "微"]

    def __init__(self, seed_list):
        self.seed_list = [x for x in seed_list if x != ""]
        self.seed_mat = [0 for x in range(5)]
        for i in self.seed_list:
            index = Seed.types.index(i[1])
            if i[0] == Seed.degrees[0]:
                self.seed_mat[index] += 2
            else:
                self.seed_mat[index] += 1

    def __str__(self):
        return "+".join(self.seed_list)
