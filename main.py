from request import champion

if __name__ == '__main__':
    champion = champion()
    list = []
    for i in range(0, 10):
        list.append(champion.json_build(i))
    print(list)
    # i = champion.localizar("Renata")
    # if isinstance(i, int):
    #     json = champion.json_build(int(i))
    #     print(json)
    # else:
    #     print("erro")
