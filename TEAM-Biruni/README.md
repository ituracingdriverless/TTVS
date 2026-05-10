# [Team Biruni] - Teknofest Robotaksi Veri Seti Katkısı

Bu dizin, Team Biruni takımı tarafından Teknofest Robotaksi yarışması şartnamesine uygun olarak etiketlenmiş 500 adet görüntünün YOLO formatındaki etiket dosyalarını içermektedir.

Görseller Google Haritalar üzerinden toplanmıştır. Tüm etiketler YoloBBoxChecker ile kontrol edilmiştir. Etiketlenmiş orijinal görüntüler, proje ekibi tarafından sağlanan Google Drive klasörüne yüklenmiştir.

## Sınıf (Class) İndeksleri

YOLO etiket dosyalarında kullanılan sınıf (class) numaraları ve karşılık geldikleri levhalar aşağıda listelenmiştir:

| İndeks | Etiket Adı |
| :---: | :--- |
| 0 | UDonusuYasak |
| 1 | dur |
| 2 | durak |
| 3 | girilmez |
| 4 | hizSiniri30 |
| 5 | hizSiniri50 |
| 6 | parkYasak |
| 7 | parkYeri |
| 8 | sagDonus |
| 9 | sagGit |
| 10 | sagIleriDon |
| 11 | sagadonulmez |
| 12 | solDonus |
| 13 | solGit |
| 14 | solIleriDon |
| 15 | solMecbur |
| 16 | solaDonulmez |
| 17 | trafikIsigi |
| 18 | yayaYolu |

---
**Veri Seti Bilgileri:**
* Toplam Görüntü: 520
* Format: YOLO Bounding Box `[class_id, x_center, y_center, width, height]`