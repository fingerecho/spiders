import requests


def img_download(imgurl,id):
	strs = "jingdong_mobile_"+id
	file_name ="../Images/"+strs+".jpg"
	img = requests.get(imgurl)
	with open(file_name,"wb") as f:
		for chunk in img.iter_content(chunk_size=1024):
			if chunk:
				f.write(chunk)
				f.flush()
		f.close()