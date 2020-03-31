secret_number = 33
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Gamoicani ricxvi\n0-50   Tqven gaqvt 3 cdis ufleba!\nRicxvi: '))
    guess_count += 1
    if guess == secret_number:
        print('Tqven gaimarjvet!')
        break
    elif guess != secret_number:
        print('Kidev cadet')
        print("Tqven dagrchat: ", (3 - guess_count), "cdis ufleba")
else:
    print('Samwuxarod tqven waaget')
    
