import random

def lowerChar(char):
  return char.lower()

name = input("oyuncu ismini giriniz ")


print("iyi sanslar ! ", name)

kelimeler = ['elma', 'armut', 'ankara', 'bilgisayar',
         'python', 'matematik', 'fizik', 'ingilizce']
ipucu=["meyve",",meyve","sehir","masada bulunan bir sey","yazilim dili","bir ders","bir ders","bir dil"]

a=random.randint(0, 7)
word = kelimeler[a]

print("bir karakteri tahmin et")
print(ipucu[a])
guesses = ''

turns = 12

while turns > 0:
    failed = 0


    for char in word:


        if char in guesses:
            print(char)


        else:
            print("_")


            failed += 1

    if failed == 0:
        print("kazandin ")
        print("dogru kelime: ", word)
        break
    print(ipucu[a])
    guess = input("bir karakteri tahmin et")
    guess=lowerChar(guess)

    guesses += guess


    if guess not in kelimeler:

        turns -= 1

        print("yanlis")

        print(turns, ' tahmin hakkin kaldi')

        if turns == 0:
            print("Kaybettin")
            print("dogru kelime: ", word)
