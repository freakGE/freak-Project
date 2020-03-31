command = ""
started = False
while True:
# while command != "quit": aseve esec sheidzleba while trues nacvlad
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Avtomobils dzrava chairto")
        else:
            started = True
            print("Avtomobilma daiwyo mushaoba...")
    elif command == "off":
        if not started:
            print("Avtomobilis dzrava gatishulia!")
        else:
            started = False
            print("Avtomobilis dzrava gamoirto")
    elif command == "help":
        print("""
start - rom chartot dzrava
off - rom gatishot dzrava
quit - rom gatishot programa.
stop - rom gaacherot dzrava
w - rom iaros win
s - rom ukan iaros
a - rom sheuxviot marcxniv
d - rom sheuxviot marjvniv
        """)
    elif command == "w":
        if started:
            print("Avtomobilma daiwyo win modzraoba")
        else:
            started = True
            print("Avtomobilis dzrava gatishulia, jer chartet rata gairos")
    elif command == "s":
        if started:
            print("Avtomobilma daiwyo ukan modzraoba")
        else:
            started = True
            print("Avtomobilis dzrava gatishulia, jer chartet rata gaiaros")
    elif command == "a":
        if started:
            print("Avtomobilma sheuxvia marcxniv")
        else:
            started = True
            print("Avtomobilis dzrava gatishulia, jer chartet rata gairos")
    elif command == "d":
        if started:
            print("Avtomobilma sheuxvia marjvniv")
        else:
            started = True
            print("Avtomobilis dzrava gatishulia, jer chartet rata gairos")
    elif command == "stop":
        if started:
            print("Avtomobili gacherda")
        else:
            started = True
            print("Avtomobili gacherebulia")
    elif command == "quit":
        break
    else:
        print("Bodishit, es brdzaneba armushaobs daxmarebistvis daweret 'help'")
