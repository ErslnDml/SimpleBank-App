import  random

class Banka:
    
    def __init__(self):
        kullanici="DAMLA ERASLAN"
        print(f"---------Hoşgeldiniz {kullanici}-----------")
        
    def hesap(self):   
        self.hesap=10000 
        print(f"Hesabınızdaki  Bakiye: {self.hesap} TL")
        self.ekhesap=5000
        print(f"Ek Hesabınızdaki  Bakiye: {self.ekhesap} TL ")
    
    def  para_yatir(self):
         self.miktar = int(input("Yatırmak istediğiniz tutarı giriniz:"))
         self.hesap+=self.miktar
         print(f"Hesabınızdaki Toplam Bakiye: {self.hesap}TL ")
    
    def  para_cek(self):
        self.miktar = int(input("Çekmek istediğiniz tutarı giriniz:"))
        if self.miktar > self.hesap:
            secim=input("Hesabınızda yeterli bakiye bulunmamaktadır ek hesap kullanmak ister misiniz?(e/h)")
            if  secim=="e":
                kalan=self.miktar-self.hesap
                print("Hesabınızda 0 TL bulunmaktadır.")
                if kalan>self.ekhesap:
                    print("Ek Hesabınızda yeterli bakiye bulunmamaktadır.")
                else:
                    ek_kalan=self.ekhesap-kalan
                    print(f"Ek Hesabınızda {ek_kalan} TL bulunmaktadır.")
            else :
                print("Üst menüye dönünüz!!!!")   
        elif self.hesap > self.miktar:
            kalan=self.hesap-self.miktar
            print(f"Hesabınızda {kalan} TL bulunmaktadır.")
        else:
            pass   
    def kredi_bilgi(self):
        self.anapara=int(input("Çekmek istediğiniz tutarı  giriniz:"))
        self.faiz_oranı= 0.015
        self.vade_sayisi=int(input("Vade sayısını  giriniz:"))
        self.taksit_tutarı= self.anapara*((((1 + self.faiz_oranı)**(self.vade_sayisi))*self.faiz_oranı) / (((1 + self.faiz_oranı)**(self.vade_sayisi))-1))
        self.toplam_geri_ödeme=self.taksit_tutarı*self.vade_sayisi
        self.toplam_faiz_borc=self.toplam_geri_ödeme-self.anapara
        print(f"Taksit : {self.taksit_tutarı}")
        print(f"Toplam Ödeme :{self.toplam_geri_ödeme}")
        print(f"Toplam Faiz Ödeme Tutarı:{self.toplam_faiz_borc}")
        print("*"* 50)
        
    def  kredi(self):
            self.faiz_tutar=self.anapara*self.faiz_oranı
            self.anapara_borc=self.taksit_tutarı-self.faiz_tutar
            self.anapara-=self.anapara_borc
            print(f"Faiz Tutarı:{self.faiz_tutar}")
            print(f"Ana Para Borç:{self.anapara_borc}")
            print(f"Anapara/Bakiye:{self.anapara}")
           
    def öde(self):
        
        for i in range(self.vade_sayisi-1):
            print("Ay:",i+1)
            x.kredi()
            self.ödeme=int(input("Ödemek istediğiniz tutarı giriniz:"))
            if self.ödeme > self.taksit_tutarı :
                kalan=self.taksit_tutarı-self.faiz_tutar
                self.toplam_faiz_borc-=self.faiz_tutar
                self.toplam_geri_ödeme-=self.ödeme
                print(f"Toplam Kalan Faiz Borcu:{self.toplam_faiz_borc}")
                print(f"KALAN BORÇ:{self.toplam_geri_ödeme}")
                print("*"* 50)
            elif self.ödeme < self.taksit_tutarı :
                if self.ödeme>self.faiz_tutar:
                    fark=self.taksit_tutarı-self.ödeme
                    self.toplam_faiz_borc-=self.faiz_tutar
                    self.toplam_geri_ödeme-=self.ödeme
                    print(f"Toplam Kalan Faiz Borcu:{self.toplam_faiz_borc}")
                    print(f"KALAN BORÇ:{self.toplam_geri_ödeme}")
                    print(f"Ödenmemiş Borç:{fark}")
                else:
                    fark=self.taksit_tutarı-self.ödeme
                    self.toplam_faiz_borc-=self.ödeme
                    self.toplam_geri_ödeme-=self.ödeme
                    print(f"Toplam Kalan Faiz Borcu:{self.toplam_faiz_borc}")
                    print(f"KALAN BORÇ:{self.toplam_geri_ödeme}")
                    print(f"Ödenmemiş Borç:{fark}")
            else:
                print("Bir üst menüye dönünüz!!!!!")


    def kredi_karti_bilgi(self):
        self.kart_borc=2000 
        self.faiz_oranı= 0.04
        self.toplam_borc=self.kart_borc+self.kart_borc*self.faiz_oranı
        self.asgari_ödeme=self.toplam_borc*0.3
        self.toplam_faiz_borc=self.kart_borc*self.faiz_oranı
        print(f"Kart Borcunuz: {self.kart_borc}")
        print(f"Toplam Borç :{self.toplam_borc}")
        print(f"Toplam Faiz Borç Tutarı:{self.toplam_faiz_borc}")
        print(f"ASgari Borç Tutarı:{self.asgari_ödeme}")
        print("*"* 50)
    
    def kredi_karti_öde(self):
            x.kredi_karti_bilgi()
            self.ödeme=int(input("Ödemek istediğiniz tutarı giriniz:"))
            if self.ödeme > self.asgari_ödeme :
                self.toplam_faiz_borc=0
                self.asgari_ödeme=0
                self.toplam_borc-=self.ödeme
                print(f"Toplam Kalan Faiz Borcu:{self.toplam_faiz_borc} TL")
                print(f"Asgari Borç Tutarı:{self.toplam_faiz_borc} TL")
                print(f"KALAN BORÇ:{self.toplam_borc} TL ")
                print("*"* 50)
            elif self.ödeme < self.asgari_ödeme :
                if self.ödeme>self.toplam_faiz_borc:
                    self.toplam_faiz_borc=0
                    self.toplam_borc-=self.ödeme
                    print(f"Toplam Kalan Faiz Borcu:{self.toplam_faiz_borc} ")
                    print(f"KALAN BORÇ:{self.toplam_borc}")
                    
                else:
                    self.toplam_faiz_borc-=self.ödeme
                    self.toplam_borc-=self.ödeme
                    print(f"Toplam Kalan Faiz Borcu:{self.toplam_faiz_borc}")
                    print(f"KALAN BORÇ:{self.toplam_borc}")
                
            else:
                print("Bir üst menüye dönünüz!!!!!")
                      
x=Banka()
x.hesap()
# x.para_yatir()
# x.para_cek()
# x.kredi_bilgi()
# x.öde()
# x.kredi_kartı_bilgi()
# x.kredi_karti_öde()
