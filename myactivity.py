

def today():
    from datetime import date
    today = date.today()
    return today


def upload_detail(up):
    try:
        if up == 1:
            diary = input("type here:-")
            with open("myDiary.txt", "a+")as diar:  # Diar == diary
                diar.write(str(str(today()))+":"+diary+"\n")
                print("successfull")
        elif up == 2:
            print("facthing data.....")
            with open("myDiary.txt",)as diar:
                for j in diar:
                    print(j)

    except Exception as err:
        print("unexcepted error ")


print("*****wellcome to My E-Diary***** ")
try:

    choies = int(
        input("press '1' for write a note and press '2' for view diary:"))
    if choies == 1:
        send = int(input("press 1 for conform:"))
        upload_detail(send)
    elif choies == 2:
        send = int(input("press 2 for confirm"))
        upload_detail(send)
except Exception as error:
    print("you press wrong key try again")
