# The idea of this program is to say an amount of money and than say % of winning it. And then you're getting that much of money that you were playing for.
import random
def play():
    global amount_of_money
    global global_money
    Won = False
    global_money = 0
    dif_in_win = 0
    while True:
        if Won == False:
            amount_of_money = int(input("Input your amount of money with which you want to play: "))
        else:
            amount_of_money = amount_of_money
        m = amount_of_money
        Percentage = int(input("Input your chance to succeed with which you want to play. "))
        t = random.randint(1, 100)
        if Percentage > 99:
            print(f"You were not playing by rules, I've lost automatically. I hope that the next time, you'll change yourself.")
            break
        elif t > Percentage:
            amount_of_money = 0
            global_money -= (amount_of_money + m)
            Won = False
        else:
            m = amount_of_money
            amount_of_money = int((amount_of_money*100)/Percentage)
            global_money += (amount_of_money - m)
            Won = True
        b = input(f"Your current balance is {amount_of_money}, Do you want to continue playing. (Yes/No): ")
        if b.lower() == "no":
            break
play()
print(f"You ended up with {amount_of_money},Your profit is {global_money}")