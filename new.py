import math
import json

given_number = input("Insert Number\n")
calc_number = float(given_number)
if calc_number < 0:
    absolute_number = abs(calc_number)
    print(absolute_number)
    vz = 1
    x = {}

    with open("werte.json", "r") as file:
        json_vz = json.load(file)
    file.close()

    with open("werte.json", "w") as file:
        print(json_vz['vz'])
        new_data = {
            "vz": 1,
            "vork": json_vz['vork'],
            "nachk": json_vz['nachk']
        }
        json_vz.update(new_data)
        json.dump(json_vz, file)
    file.close()
else:
    absolute_number = calc_number
    vz = 0
absolute_number = str(absolute_number)

#^^ Checked if Number is positive or negative and changed to absolute if needed ^^

if "." in str(absolute_number):
    split_number = absolute_number.split(".")
    print(split_number)

    while int(split_number[0]) >= 1:
        bin_number = int(split_number[0]) / 2
        x = int(bin_number)
        bin_number_1 = str(bin_number)
        bin_number_2 = bin_number_1.split(".")
        bin_number_3 = int(bin_number_2[1])

        if bin_number_3 > 0:
            print("1")

        else:
            print("0")
        bin_number = math.floor(x)
        split_number[0] = int(bin_number)

#^^ Converts all numbers befor "." to binary ^^

    ref_number = f"0.{split_number[1]}"
    ref_number = float(ref_number)
    #ref_number = round(ref_number, len(split_number[1]))

    looplist = ""
    looplist_2 = []

    print(ref_number)

    ref_number_1 = ref_number * 2
    print(ref_number)
    #ref_number_1 = round(ref_number_1, str(split_number[1]))

    if float(ref_number_1) > 1:
        fst = "1"
        looplist = looplist + str(1)

        ref_number_1 = float(ref_number) - float(1.0)
        print(ref_number_1)
        #ref_number_1 = round(ref_number_1, len(split_number[1]))

    else:
        fst = "0"
        looplist = looplist + str(0)
        #ref_number_1 = round(ref_number_1, len(split_number[1]))


    loopnumber = ref_number * 2
    print(loopnumber)

    if float(loopnumber) > 1:
        sd = "1"
        loopnumber = float(loopnumber) - float(1.0)
        print(loopnumber)
        looplist = looplist + str(1)
        loopnumber_1 = loopnumber
        #loopnumber_1 = round(loopnumber_1, len(split_number[1]))


    else:
        sd = "2"
        looplist = looplist + str(0)
        loopnumber_1 = loopnumber
        #loopnumber_1 = round(loopnumber_1, len(split_number[1]))



    while float(loopnumber_1) != [float(ref_number),  float(ref_number_1), float(loopnumber),float(0.00)] and float(loopnumber_1) not in looplist_2:
        number = float(loopnumber_1) * 2

        if float(number) > 1:
            print("1")
            looplist = looplist + str(1)
            loopnumber_1 = float(number) - float(1.0)
            loopnumber_1 = round(loopnumber_1, 2)
            looplist_2.append(loopnumber_1)

        elif float(loopnumber_1) < 1:
            print("0")
            looplist = looplist + str(0)
            loopnumber_1 = round(number, 2)
            looplist_2.append(loopnumber_1)

        print(looplist)
        print(looplist_2)

    with open("werte.json", "r") as file:
        json_nach = json.load(file)
    file.close()

    with open("werte.json", "w") as file:
        print(json_nach['nachk'])
        new_data = {
            "vz" : json_nach['vz'],
            "vork": json_nach['vork'],
            "nachk": int(looplist)
        }
        json_nach.update(new_data)
        json.dump(json_nach, file)
    file.close()

else:
    x_number = absolute_number

    while int(x_number) >= 1:
        number = int(x_number) / 2
        x = int(number)
        number_1 = str(number)
        number_2 = number_1.split(".")
        number_3 = int(number_2[1])

        if number_3 > 0:
            print("1")

        else:
            print("0")
        number = math.floor(x)
        x_number = int(number)