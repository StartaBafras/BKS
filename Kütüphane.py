def kitap_ekle(): #teşvik programı eklenecek
    kitap_ismi=input("Kitap ismini giriniz:")
    kitap_yazar=input("Kitap yazarini BÜYÜK HARF kullanara giriniz:")
    kitap_yayinevi=input("Kitap yaynın evini giriniz:")
    print("01-Roman 02-Ani 03-Felsefe 04-Bilim 05-Deneme 06-Iktisat 07-Edebiyat 08-Şiir 09-Masal 10-Öykü 11-Oyun 12-Siyaset 13-Tarih")
    tur=input("Kitap tür numarasını giriniz. Örnek:05 ")
    #yaş=input("Yaş aralığını seniçiz.")
    kitap_değeri=input("Kitap değerini belirten sayıyı belirleyiniz, varsayılan olarak 25: ")
    #bas_harf=kitap_yazar[0]
    #İlk bağlantı kısmı
    import sqlite3 #içeri aktardık
    huseyro= sqlite3.connect('depo.db') #bağlantıyı oluşturduk
    im=huseyro.cursor() #imleç oluşturduk
    tablo_yap=("CREATE TABLE IF NOT EXISTS kitaplık ('isim','yazar','yayınevi','özel_numara','verildiği_tarih','alınacağı_tarih','alan_kişi_numarası',gerekli_puan)")
    im.execute(tablo_yap)#Tablolar düzenlenmeli
    huseyro.commit()
    import random
    uretilen_sayi=random.randint(1000,9999) #Sayi kontrol mekanizmasi icin veritabani baglantisi
    tur=int(tur)
    raf=random.randint(100*tur-99,tur*100)
    alfabe={"A":'01',"B":'02',"C":'03',"Ç":'04',"D":'05',"E":'06',"F":'07',"G":'08',"H":'09',"I":'10',"İ":'11',"J":'12',"K":'13',"L":'14',"M":'15',"N":'16',"O":'17',"Ö":'18',"P":'19',"R":'20',"S":'21',"Ş":'22',"T":'23',"U":'24',"Ü":'25',"V":'26',"Y":'27',"Z":'28',"Q":'29',"W":'30',"X":'31'}#Kısa yol olmalı
    #yzr=alfabe[bas_harf]
    ayırt_edici_kod=str(tur+raf+uretilen_sayi)
    im.execute("INSERT INTO kitaplık VALUES(?,?,?,?,'-','-',?,?)",(kitap_ismi,kitap_yazar,kitap_yayinevi,ayırt_edici_kod,ayırt_edici_kod,kitap_değeri))
    huseyro.commit()
    huseyro.close()
def üye_kayıt():
    ad=input("İsim giriniz: ")
    soyad=input("Soyad giriniz: ")
    yaş=str(input("Yaş giriniz: "))
    numara=str(input("Telefon numarasını giriniz: "))
    tc_numarası=str(input("T.C. Kimlik numarası giriniz: "))
    import random,sqlite3,os#dosya kontrolü eklenecek
    uretilen_kişi_numarası=str(random.randint(100000,999999))
    güvenilirlik_puanı=25
    huseyro=sqlite3.connect("mahluklar.db")
    im=huseyro.cursor()
    im.execute("CREATE TABLE IF NOT EXISTS kisiler ('Ad','Soyad','TC_numarası','Yaş','Güvenilirlik_Puanı','Kişi_Numarası')")
    huseyro.commit()
    im.execute("INSERT INTO kisiler VALUES(?,?,?,?,?,?)",(ad,soyad,tc_numarası,yaş,güvenilirlik_puanı,uretilen_kişi_numarası))
    huseyro.commit()
    huseyro.close()

def kitap_alım():
    import sqlite3, datetime
    kişi_numarası=input("6 Haneli kişi numarasını giriniz: ")
    kitap_numarası=input("Kitap numarasını giriniz: ")
    huseyro1=sqlite3.connect("mahluklar.db")
    im=huseyro1.cursor()
    im.execute("SELECT * FROM kisiler WHERE Kişi_Numarası=?",(kişi_numarası,))
    alınan_kişi=im.fetchall()
    kontrol_kişi=alınan_kişi[0]
    huseyro1.close()
    huseyro2=sqlite3.connect("depo.db")
    im1=huseyro2.cursor()
    im1.execute("SELECT * FROM kitaplık WHERE özel_numara=?",(kitap_numarası,))
    alınan_kitap=im1.fetchall()
    kontrol_kitap=alınan_kitap[0]
    if str(kontrol_kitap[7]) <= str(kontrol_kişi[4]):
        print("Alabilir")
        an = datetime.datetime.now()
        tarih = datetime.datetime.strftime(an,'%d.%m.%Y ')
        im1.execute("UPDATE kitaplık SET alan_kişi_numarası=? where alan_kişi_numarası=?",(kişi_numarası,kitap_numarası))#Bu ne saçmalık
        im1.execute("UPDATE kitaplık SET verildiği_tarih='-' where özel_numara=?",(kitap_numarası,))
        im1.execute("UPDATE kitaplık SET verildiği_tarih=? where özel_numara=?",(tarih,kitap_numarası,))
        huseyro2.commit()
        huseyro2.close()
        
    else:
        print("Gerekli puan sağlanmadı")
        print("Gereken puan:",kontrol_kitap[7],"Kişinin puanı:",kontrol_kişi[4])
def kitap_teslim():
    kişi_no=input("6 haneli kişi numarasını giriniz: ")
    kitap_no=str(input("Kitap numarasını giriniz: "))
    import sqlite3,datetime
    an = datetime.datetime.now()
    tarih = datetime.datetime.strftime(an,'%d.%m.%Y ')
    huseyro=sqlite3.connect("depo.db")
    im=huseyro.cursor()
    im.execute("SELECT * FROM kitaplık WHERE ")
    im.execute("UPDATE kitaplık SET alan_kişi_numarası='-' where özel_numara=?",(kitap_no,))
    huseyro.commit()
    huseyro.close()
while True:
    giriş=input("""Yapılacak İşlem için Numara Giriniz \n01:Kitap EKleme\n02:Yeni Üye Kaydı\n03:Kitap Verme\n04:Kitap Teslim\nİşlem Numarası:
    """)
    if giriş == '01':
        kitap_ekle()
    elif giriş == '02':
        üye_kayıt()
    elif giriş == '03':
        kitap_alım()
    elif giriş == '04':
        kitap_teslim()
    else:
        print("Bu numaraya sahip işlem bulunmamaktadır.")
#istek listesi
#ingilizce kitapları teşvik
#sunucu yedekleme
#E-kitap için pdf desteği