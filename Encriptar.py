
import random

entrada = input("Insira um entrada: ")
texto = " "
alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
chave = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
random.shuffle(chave)

for letra in entrada:
    if letra == " ":
        texto += " "
    else:
        texto += (chave[alfabeto.index(letra)])
        
print(f"mensagem criptografada: {texto}  chave: {chave}")


