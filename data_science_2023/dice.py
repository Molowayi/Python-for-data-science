from random import randint
# import random => random.randint(1, 10)

def my_dice(faces = 6):
    # return randint(1,6)
    print("faces : " + str(faces))
    result = randint(1, faces)
    return result

# print(my_dice())
#for _ in range(10):
#    my_dice()

dice1 = my_dice()
dice2 = my_dice(20)
value = dice1 + dice2

msg = f"{dice1: .2f} + {dice2} = {dice2 + dice1}"

print(msg)


# Attention à l'échapement des cartactères