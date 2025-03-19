texto = "lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk lmird jk xjubt trmui jx ibndt wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"

alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
frequencia = []
frequenciabr = ["a", "e", "o", "s", "r", "i", "n", "d", "m", "u", "t", "c", "l", "p", "v", "g", "h", "q", "b", "f", "z", "j", "x", "k", "y," "w"]
frequenciaeng = ["e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p", "b", "v", "k", "j", "x", "q", "z"]
quant = []
idioma = input("Escolha o idioma do texto original (ENG|BR)")

if idioma == "BR":
    frequencia = frequenciabr
else:
    frequencia = frequenciaeng
    
for letra in alfabeto:
    if(letra != ' '):
        quant.append(texto.count(letra))

i = 0
while(i < len(alfabeto)):
    j = i
    while(j < len(alfabeto)):
        if(quant[i] < quant[j]):
            temp = quant[i]
            quant[i] = quant[j]
            quant[j] = temp
            temp2 = alfabeto[i]
            alfabeto[i] = alfabeto[j]
            alfabeto[j] = temp2
        j += 1
    i += 1

novoTexto = ""
for letra in texto:
   if(letra != ' '):
    novoTexto += frequencia[alfabeto.index(letra)]
   else:
      novoTexto += ' '


while(True):
   print(f"\n{novoTexto}\n")
   resposta = input("Deseja Trocar Duas Letras? (S/N): ")
   if(resposta == "N" or resposta == "n"):
      break
   else:
        letras = input("Digite as Duas Letras: (Dê espaço entre as letras) ")
        index1 = frequencia.index(letras[0])
        index2 = frequencia.index(letras[2])
        temp3 = frequencia[index1]
        frequencia[index1] = frequencia[index2]
        frequencia[index2] = temp3
        novoTexto = ""
        for letra in texto:
            if(letra != ' '):
                novoTexto += frequencia[alfabeto.index(letra)]
            else:
                novoTexto += ' '
    
      
