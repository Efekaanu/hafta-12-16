#kelime =input("kelime gir:")
#ters_kelime = kelime[::-1]
#if kelime == ters_kelime:
 #   print("girilen kelime bir palindrome'dur")
#else:
 #   print("\033[96m"+"girilen kelime bir palindrome değildir Palindrome'a örnek olarak: 'neden' kelimesi)"+"\033[0m")

' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '

#kelime=input("lütfen bir kelime girin:")
#kelime.lower(kelime)
#kelime.upper(kelime)
#palindrome(kelime)

' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '

#def ortak_elemanlar(liste1,liste2):
    #ortaklar = set()
   # for i in liste1:
   #     if i in liste2:
  #          liste1.append(i)
 #   return ortaklar

#liste1=[1,2,5,7,8]
#liste2=[1,5,7,8,4]

#ortaklar= ortak_elemanlar(liste1,liste2)
#print(ortaklar)

' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '

#def sıklık(liste):
 #   frekanslar={}
  #  for eleman in liste:
  #      if eleman in frekanslar:
   #         frekanslar[eleman] += 1 
    #    else:
     #       frekanslar[eleman] = 1
   # return frekanslar

#liste_örneği = [2,3,5,7,9,29,42,13,7,2,96,5]

#sonuç=sıklık(liste_örneği)

#for eleman,frekans in sonuç.items():
 #   print(f"{eleman}: {frekans}")

#' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 

def fibonacci(n):
    fibo=[0,1]
    for _ in range(2,n):
        next=  fibo[-1] + fibo[-2]
        fibo.append(next)
    return fibo
n=10
fibo=fibonacci(n)
print(f"{fibo}")