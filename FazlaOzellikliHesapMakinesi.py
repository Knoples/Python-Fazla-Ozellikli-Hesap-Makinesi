import math
def toplama(x, y):
    return x + y
def cikarma(x, y):
    return x - y
def carpma(x, y):
    return (x) * (y)
def bölme(x, y):
    return (x) / (y)
def kök_alma(x, y):
   return pow(x,1/y)
def logaritma(x,y):
   return math.log(x,y)
def hipotenüs(x,y):
   return pow((x**2+y**2),1/2)
def açıtoradyan(x):
   return (x) * ((math.pi)/(180))
print("Hesap Makinesine Hoş Geldiniz.")
while True:
  print("""Lütfen Yapmak İstediğiniz İşlemi Seçiniz
           1- Toplama
           2- Çıkarma
           3- Çarpma
           4- Bölme
           5- Kök Alma
           6- Sinüs Alma
           7- Kosinüs Alma
           8- Tanjant Alma
           9- Kotanjant Alma
           10- Exp Alma (e^x)
           11- Faktöriyel
           12- Logaritma
           13- Hipotenüs Bulma
           14- Açıyı Radyana Çevirme
           15- Çıkış""")
  secim = input("=> ")
  if secim == "1" or secim == "2" or secim== "3" or secim=="4":
    while True:
      try:
          print("\nKüsüratlı Sayıları Nokta (.) İle Belirtiniz Örn: 1.2")
          sayi1=float(input("İlk Sayıyı Giriniz => "))
          sayi2=float(input("İkinci Sayıyı Giriniz => "))
          break
      except  ValueError:
          print("Hatalı Sayı Girişi. Lütfen Tekrar Sayı Girişi Yapınız.")
          continue
    if secim == "1":
      print(sayi1,"+",sayi2,"=",toplama(sayi1,sayi2)) 
    elif secim == "2":
      print(sayi1,"-",sayi2,"=",cikarma(sayi1,sayi2))
    elif secim == "3":
      print(sayi1,"x",sayi2,"=",carpma(sayi1,sayi2))
    elif secim == "4":
      if sayi2 == 0:
        print("Bir Sayının 0 (Sıfır) İle Bölümü Tanımsızdır.")
        continue
      print(sayi1,"/",sayi2,"=",bölme(sayi1,sayi2))
  elif secim == "5":
      while True:
       try:
          print("\nKüsüratlı Sayıları Nokta (.) İle Belirtiniz Örn: 1.2")
          sayi1=float(input("Sayıyı Giriniz => "))
          kok=float(input("Kaçıncı Dereceden Kök Almak İstiyorsunuz => "))
          if kok == 0:
             print("Sıfır Değeri Tanımsız Yapar.")
             continue
          break
       except  ValueError:
          print("Hatalı Sayı Girişi. Lütfen Tekrar Sayı Girişi Yapınız.")
          continue
      print(sayi1,"sayısının",kok,". Kökü => ",kök_alma(sayi1,kok))
  elif secim == "6" or secim == "7" or secim== "8" or secim=="9":
      while True:
       try:
          print("\nKüsüratlı Sayıları Nokta (.) İle Belirtiniz Örn: 1.2")
          sayi1=float(input("Açı Değerini Giriniz => "))
          aci = açıtoradyan(sayi1)
          break
       except  ValueError:
          print("Hatalı Sayı Girişi. Lütfen Tekrar Sayı Girişi Yapınız.")
          continue
      if secim == "6":
         print(math.sin(aci))
      elif secim == "7":
         print(math.cos(aci))
      elif secim == "8":
         print(math.tan(aci))
      elif secim == "9":
         deger = math.tan(aci)
         float(deger)
         print(1/deger)
  elif secim == "10":
      while True:
       try:
          print("\nKüsüratlı Sayıları Nokta (.) İle Belirtiniz Örn: 1.2")
          sayi1=float(input("Sayıyı Giriniz => "))
          break
       except  ValueError:
          print("Hatalı Sayı Girişi. Lütfen Tekrar Sayı Girişi Yapınız.")
          continue
      print("Sonuc => ", math.exp(sayi1))
  elif secim == "11":
      while True:
       try:
          print("\nKüsüratlı Sayıları Nokta (.) İle Belirtiniz Örn: 1.2")
          sayi1=int(input("Sayıyı Giriniz => "))
          break
       except  ValueError:
          print("Hatalı Sayı Girişi. Lütfen Tekrar Sayı Girişi Yapınız.")
          continue
     
      deger1 = 1
      for i in range(sayi1):
       deger1 = deger1 * (i+1)
 
      print("Faktoriyel Sonucu => ", deger1)
  elif secim == "12":       
      while True:
       try:
          print("\nKüsüratlı Sayıları Nokta (.) İle Belirtiniz Örn: 1.2")
          taban=float(input("Logaritma Tabanını Giriniz => "))
          sayi1=float(input("Logaritması Alınacak Sayıyı Giriniz => "))
          if taban <= 0 or taban == 1:
             print("Tabanda Bu Değer Tanımsız Yapar.")
             continue
          elif sayi1<=0:
             print("Bu sayı Logaritmayı Tanımsız Yapar.")
             continue 
          break
       except  ValueError:
          print("Hatalı Sayı Girişi. Lütfen Tekrar Sayı Girişi Yapınız.")
          continue
      print(logaritma(sayi1,taban))
  elif secim == "13":
      while True:
       try:
          print("\nKüsüratlı Sayıları Nokta (.) İle Belirtiniz Örn: 1.2")
          kenar1=float(input("İlk Kenarın Değerini Giriniz => "))
          kenar2=float(input("İkinci Kenarın Değerini Giriniz => "))
          if kenar1 < 0:
             print("Kenar Negatif Değer Alamaz.")
             continue
          elif kenar1 == 0:
             print("Kenarın Uzunluğu Sıfır Olamaz Çünkü Sıfır Olursa Bir Kenar Olmaz.")
             continue 
          if kenar2 < 0:
             print("Kenar Negatif Değer Alamaz.")
             continue
          elif kenar2 == 0:
             print("Kenarın Uzunluğu Sıfır Olamaz Çünkü Sıfır Olursa Bir Kenar Olmaz.")
             continue          
          break
       except  ValueError:
          print("Hatalı Sayı Girişi. Lütfen Tekrar Sayı Girişi Yapınız.")
          continue
      print(hipotenüs(kenar1,kenar2))
  elif secim == "14":
      while True:
       try:
          print("\nKüsüratlı Sayıları Nokta (.) İle Belirtiniz Örn: 1.2")
          sayi1=float(input("Açı Değerini Giriniz => "))
          aci = açıtoradyan(sayi1)
          break
       except  ValueError:
          print("Hatalı Sayı Girişi. Lütfen Tekrar Sayı Girişi Yapınız.")
          continue
      print(aci)        
  elif secim == "15":
    break   
  
  else:
    print("Yanlış Tuşlama Yaptınız. Tekrar Deneyiniz.")