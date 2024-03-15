import os 
geçerli_dizin=os.getcwd()
print(geçerli_dizin)

for i in os.listdir(geçerli_dizin):
    print(1)

new_directory = os.path.join(geçerli_dizin,"yeni_dizin")
os.mkdir(new_directory)
print(f"{new_directory} oluştu")

os.chdir(new_directory)
print(f"{new_directory} dizinine gidildi")

dosya_yolu = os.path.join(new_directory,"example.txt")
with open(dosya_yolu,'w',encoding='utf-8') as file:
    file.write("hellÖ wÖrld")

os.remove('example.txt')
print("dosya silindi")
os.chdir(geçerli_dizin)
print("desktopa gidildi")
os.rmdir('yeni_dizin')
print("açtığım dizimi sildim")