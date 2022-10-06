import math
import json

#n = input("insert Number\n")
#print(bin(int(n)))

def in_bin():
    n = input("insert Number\n")
    n = float(n)
    if n < 0:
        n = abs(n)
        print(n)
        vz = 1
        #global vz
        x = {}

        with open("werte.json", "r") as file:
            jvz = json.load(file)
        file.close()

        with open("werte.json", "w") as file:

            print(jvz['vz'])
            newdata = {
                "vz": 1,
                "vork": jvz['vork'],
                "nachk": jvz['nachk']
            }
            jvz.update(newdata)
            json.dump(jvz, file)
        file.close()
    else:
        vz = 0
        #global vz
    n = str(n)

    if "." in str(n):
        nu = n.split(".")
        #global nu
        print(nu)
        nu[0] = int(nu[0])

        while int(nu[0]) >= 1:
            num = int(nu[0])/2
            x = int(num)
            #print(num)
            numbe = str(num)
            numb = numbe.split(".")
            #print(numb)
            number = int(numb[1])

            if number > 0:
                print("1")

            else:
                print("0")
            num = math.floor(x)
            #print(num)
            nu[0] = int(num)
            #print(num)

        refnumber = f" 0.{nu[1]}"
        refnumber = float(refnumber)
        print(refnumber)
        refnumber = refnumber * 2
        print(refnumber)
        if float(refnumber) > 1:
            fst = "1"
            refnumber = float(refnumber) - float(1.0)
            print(refnumber)
            #na1 = round(num, int(len(str(nu[1]))))
        else:
            fst = "0"
            #na1 = round(num, int(len(str(nu[1]))))
            #Referenznummer


        loopnumber = refnumber * 2
        print(loopnumber)
        if float(loopnumber) > 1:
            sd = "1"
            loopnumber = float(loopnumber) - float(1.0)
            print(loopnumber)
            #na1 = round(num, int(len(str(nu[1]))))
        else:
            sd = "0"

        looplist = ""
        while float(loopnumber) != float(refnumber) and float(loopnumber) != float(0.0):
            number = float(loopnumber) * 2
            if float(number) > 1:
                print("1")
                looplist = looplist + str(1)
                loopnumber = float(number) - float(1.0)
                loopnumber = round(loopnumber, int(len(str(nu[1]))))

            elif float(loopnumber) < 1:
                print("0")
                looplist = looplist + str(0)
                loopnumber = round(number, int(len(str(nu[1]))))

        with open("werte.json", "r") as  file:
            jnach = json.load(file)
        file.close()

        with open("werte.json", "w") as file:

            print(jnach['nachk'])
            newdata = {
                "vz": jnach['vz'],
                "vork": jnach['vork'],
                "nachk": int(looplist)
            }
            jnach.update(newdata)
            json.dump(jnach, file)
        file.close()

    else:
        nx = n

        while int(nx) >= 1:
            num = int(nx)/2
            x = int(num)
            #print(num)
            numbe = str(num)
            numb = numbe.split(".")
            #print(numb)
            number = int(numb[1])

            if number > 0:
                print("1")

            else:
                print("0")
            num = math.floor(x)
            #print(num)
            nx = int(num)
            #print(num)



in_bin()