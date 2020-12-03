import argparse
import os

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


xmlPath="./"

classes ={
"Dur Tabelası":0,
"Durak Tabelası":0,
"Hız Limiti 30 Tabelası":0,
"Sağa Dönülebilir Veya İleri Gidilebilir Tabelası":0,
"Sağa Dönüş Tabelası":0,
"Sağa Dönüş Yasak Tabelası":0,
"Sola Dönülebilir Veya İleri Gidilebilir Tabelası":0,
"Sola Dönüş Tabelası":0,
"Sola Dönüş Yasak Tabelası":0,
"Kırmızı Işık Tabelası":0,
"Sarı Işık Tabelası":0,
"Yeşil Işık Tabelası":0,
"Park Tabelası":0,
"Park Yasak Tabelası":0,
"Hız Limiti 20 Tabelası":0,
"Geçiş Yok Tabelası":0,
"Taşıt Giremez Tabelası":0,
"Hız Limiti 50 Tabelası":0,
"Yol Ver Tabelası":0,
"Işıklı İşaret Cihazı":0,
"Dönüş Adası Tabelası":0,
"Yön Tabelası":0,
"Sağdan Anayol Girişi":0,
"Soldan Anayol Girişi":0,
"Sağa Mecburi Yön":0,
"Sola Mecburi Yön":0,
"Sağdan Gidiniz":0,
"Soldan Gidiniz":0,
"Ada Etrafında Dönene Kadar Yol Ver":0,
"Hız Limiti 40 Tabelası":0,
"Tehlikeli Viraj Tabelası":0,
"Tümsek Uyarı Tabelası":0,
"Hız Limiti 10 Tabelası":0,
"Yaya Geçidi":0,
"Hız Limiti 70 Tabelası":0,
"U Dönüşü Yasak Tabelası":0,
"Kamyon Giremez":0,
"Her İki Yandan Gidiniz":0,
"Hız Limiti 60 Tabelası":0,
"Okul Geçidi":0,
"Hız Limiti 82 Tabelası":0,
"Duraklama ve Park Etme Yasak":0
}


filenames = os.listdir(xmlPath)

for filename in filenames:
    if filename.endswith(".xml"):
        mytree = ET.parse(filename)
        myroot = mytree.getroot()
        
        for pathLabel in myroot.iter('object'):
            for objectLabel in pathLabel.iter("name"):
                if (objectLabel.text in classes):
                    classes[objectLabel.text]=classes[objectLabel.text]+1
                else:
                    print("Not Found Classes")
   
print(classes)


 
