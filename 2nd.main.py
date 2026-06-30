import random

while True:
     secret = random.randint(1,100)
     attempts = 0

     print("Санды тап оюну")
     print("1ден 100гө чейин  1 сан жашырдым.")

     while True:
           guess = int(input("Санды киргизиниз: "))
           attempts += 1

           if guess < secret:
               print("Чоңураак сан киргизиңиз.")
           elif guess > secret:
               print("Кичирээк сан киргизиңиз")
           else:
               print(f"Куттуктайм! Сиз жашыруун санды {attempts} аракетинде таптыныз!")
               break

     answer = input("Дагы ойнойсузбу? (ооба\жок)" ).lower()

     if answer != "ооба":
         print("Ойногонуңуз үчүн рахмат! :) ")
         break