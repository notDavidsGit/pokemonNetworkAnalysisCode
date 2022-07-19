types = ["normal","fire","water","lightning","grass","ice","fighting","poison","ground","flying","psychic","bug","rock","ghost","dragon","dark","steel","fairy"]
# print(types)
types_map = {
"normal": [1,1,1,1,1,1,1,1,1,1,1,1,0.5,0,1,1,0.5,1],
"fire":[1,0.5,0.5,1,2,2,1,1,1,1,1,2,0.5,1,0.5,1,2,1],
"water":[1,2,0.5,1,0.5,1,1,1,2,1,1,1,2,1,0.5,1,1,1],
"lightning":[1,1,2,0.5,0.5,1,1,1,0,2,1,1,1,1,0.5,1,1,1],
"grass":[1,0.5,2,1,0.5,1,1,0.5,2,0.5,1,0.5,2,1,0.5,1,0.5,1],
"ice":[1,0.5,0.5,1,2,0.5,1,1,2,2,1,1,1,1,2,1,0.5,1],
"fighting":[2,1,1,1,1,2,1,0.5,1,0.5,0.5,0.5,2,0,1,2,2,0.5],
"poison":[1,1,1,1,2,1,1,0.5,0.5,1,1,1,0.5,0.5,1,1,0,2],
"ground":[1,2,1,2,0.5,1,1,2,1,0,1,0.5,2,1,1,1,2,1],
"flying":[1,1,1,0.5,2,1,2,1,1,1,1,2,0.5,1,1,1,0.5,1],
"psychic":[1,1,1,1,1,1,2,2,1,1,0.5,1,1,1,1,0,0.5,1],
"bug":[1,0.5,1,1,2,1,0.5,0.5,1,0.5,2,1,1,0.5,1,2,0.5,0.5],
"rock":[1,2,1,1,1,2,0.5,1,0.5,2,1,2,1,1,1,1,0.5,1],
"ghost":[0,1,1,1,1,1,1,1,1,1,2,1,1,2,1,0.5,1,1],
"dragon":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,0.5,0],
"dark":[1,1,1,1,1,1,0.5,1,1,1,2,1,1,2,1,0.5,1,0.5],
"steel":[1,0.5,0.5,0.5,1,2,1,1,1,1,1,1,2,1,1,1,0.5,2],
"fairy":[1,0.5,1,1,1,1,2,0.5,1,1,1,1,1,1,2,2,0.5,1]
}
# print(types_map)
to_print = ""
for t in sorted(types):
    advantage_indicies = []
    disadvantage_indicies = []
    immunity_indicies = []

    data_line = types_map[t]
    # print(t)
    for i in range(len(data_line)):
        entry = data_line[i]
        if entry == 0:
            immunity_indicies.append(types[i])
        elif entry == 2:
            advantage_indicies.append(types[i])
        elif entry == 0.5:
            disadvantage_indicies.append(types[i])

    to_print += ", " + str(disadvantage_indicies)
    # to_print += ", " + str(immunity_indicies)

print(to_print)
