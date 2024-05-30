# ex01
with open('names.txt', "r") as file: allNames = [name.strip() for name in file]
print(max(allNames, key=len))

# ex02
with open('names.txt', "r") as file:
    print(sum(map(lambda name: len(name.strip()), file)))

# ex03
with open('names.txt', "r") as file:
    allNames = sorted((name.strip() for name in file), key=len)
    short_words = len(allNames[0])
    print("\n".join(name for name in allNames if len(name) == short_words))

# ex04
with open('names.txt') as fileToRead, open('name_length.txt', 'w') as fileToWrite: fileToWrite.write("\n".join(str(len(line.strip())) for line in fileToRead))
with open('name_length.txt') as file2: print(file2.read())


# ex05
nameInput = int(input("enter name length: "))
with open('names.txt', "r") as file:
    print("\n".join(name for name in allNames if len(name) == nameInput))