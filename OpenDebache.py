#este script es para mis subscriptores
""" script por los mil subs
code writting by Vampy Security"""
import  os
import  webbrowser

print("hola subs")
print("solamente elige la opcion deseada")
print("menu")
print("")
print ("1.- pagina de la NSA")
print("2.- pagina de la CIA")
print("3.- instalar Tools  en termux")
print("4.- instalar lenguajes de programacion en termux")
print("5.- complementos de termux")
print("6.- Phishing")
print("7.- Nethunter")
print("8.- Salir")
opcion = int(input("introduce el num deseado:   "))
if opcion == 1:
        webbrowser.open('https://nsa.gov')
elif opcion == 2:
        webbrowser.open('https://cia.gov')
elif opcion == 3:
        os.system('apt install nmap crunch exiftool whois -y')
elif opcion == 4:
        os.system('apt install python python2 perl php ruby -y')
elif opcion == 5:
        os.system('apt install git curl wget vim openssh openssl apache2 -y')
elif opcion == 6:
    os.system('chmod +x Lucifer.py && python Lucifer.py')
elif opcion == 7:
    os.system('apt install wget && wget -O install-nethunter-termux https://offs.ec/2MceZWr && chmod +x install-nethunter-termux && ./install-nethunter-termux')
elif opcion == 8:
    os.system('exit')
    print("gracias por apoyar el canal bro")
else:
    print("esta opcion no es validad mi camarada")
