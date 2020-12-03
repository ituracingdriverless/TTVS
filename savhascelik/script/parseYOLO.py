# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import argparse
import os


classes=["Dur Tabelası","Durak Tabelası","Hız Limiti 30 Tabelası","Sağa Dönülebilir Veya İleri Gidilebilir Tabelası","Sağa Dönüş Yasak Tabelası","Sola Dönülebilir Veya İleri Gidilebilir Tabelası","Sola Dönüş Yasak Tabelası","Kırmızı Işık Tabelası","Yeşil Işık Tabelası","Park Tabelası","Park Yasak Tabelası","Hız Limiti 20 Tabelası","Geçiş Yok Tabelası","Hız Limiti 50 Tabelası","Yol Ver Tabelası","Işıklı İşaret Cihazı","Dönüş Adası Tabelası","Yön Tabelası","Sağdan Anayol Girişi","Sağa Mecburi Yön","Sola Mecburi Yön","Sağdan Gidiniz","Soldan Gidiniz","Ada Etrafında Dönene Kadar Yol Ver","Hız Limiti 40 Tabelası","Tehlikeli Viraj Tabelası","Tümsek Uyarı Tabelası","Hız Limiti 10 Tabelası","Yaya Geçidi","Hız Limiti 70 Tabelası","U Dönüşü Yasak Tabelası","Kamyon Giremez","Her İki Yandan Gidiniz","Hız Limiti 60 Tabelası","Okul Geçidi","Hız Limiti 82 Tabelası","Duraklama ve Park Etme Yasak"]

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)



def main(args):
	dataset_path = args.dataset_path

	annot_path = os.path.join(dataset_path, "./annots")

	filenames = os.listdir(annot_path)


	if not os.path.exists(os.path.join(dataset_path, "labels")):
		os.makedirs(os.path.join(dataset_path, "labels"))
	for filename in filenames:
		img_id = filename[:-4]
		file_path = os.path.join(annot_path, filename)
		in_file = open(file_path,encoding="utf-8")
		out_file = open(os.path.join(dataset_path, "labels", img_id + ".txt"), "w")
		tree=ET.parse(in_file)
		root = tree.getroot()
		size = root.find('size')
		w = int(size.find('width').text)
		h = int(size.find('height').text)

		for obj in root.iter('object'):
			difficult = obj.find('difficult').text
			cls = obj.find('name').text
			if cls not in classes or int(difficult) == 1:
				continue
			cls_id = classes.index(cls)
			xmlbox = obj.find('bndbox')
			b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
			bb = convert((w,h), b)
			out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
	

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
	
    
    argparser.add_argument(
		'-d', '--dataset_path',
		help = 'The path of dataset',
		required = True)


    args = argparser.parse_args()
    
    main(args)
