TYPES = ["异常果", "恢复果", "亲密度果", "努力果", "临时属性果", "方块原料果", "plus果", "减伤果"]


class Fruit:
    def __init__(self, name, description, seeds, fruit_type, product_num):
        self.name = name
        self.description = description
        self.seeds = seeds
        self.fruit_type = fruit_type
        self.product_num = product_num

    def __str__(self):
        return "{}: {}\t {}\t {}".format(self.name, self.description, self.seeds, self.fruit_type)

    def get_type(self):
        return self.fruit_type

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_seeds(self):
        return self.seeds

    def get_product_num(self):
        if self.product_num[0] == 0:
            return "产量未录入"
        return "产量：{} ~ {}".format(*self.product_num)

    def get_average_product_num(self):
        return sum(self.product_num) / 2


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
