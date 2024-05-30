def check_id_valid(id_number):
    str_id = str(id_number)
    multiplied = [int(str_id[i]) * (2 if i % 2 else 1) for i in range(len(str_id))]
    processed = [sum(divmod(d, 10)) if d > 9 else d for d in multiplied]
    return sum(processed) % 10 == 0


class IDIterator:
    def __init__(self, start_id):
        self.id = start_id

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.id > 999999999:
                raise StopIteration
            if check_id_valid(self.id):
                valid_id = self.id
                self.id += 1
                return valid_id
            self.id += 1


def id_generator(start_id):
    id = start_id
    while id <= 999999999:
        if check_id_valid(id):
            yield id
        id += 1


def main():
    user_id = int(input("Enter ID: "))
    choice = input("Generator or Iterator? (gen/it)? ")

    if choice == "it":
        iterator = IDIterator(user_id + 1)
        for i in range(10):
            try:
                print(next(iterator))
            except StopIteration:
                break
    elif choice == "gen":
        generator = id_generator(user_id + 1)
        for i, id in enumerate(generator):
            if i == 10:
                break
            print(id)


if __name__ == "__main__":
    main()
