from models import dataDariExcel as Excel
from config import pesan

def cariNama(nama):
    data = Excel()
    temp = []
    for i in data:
        if nama in i["nama"].lower():
            text = pesan["absensi"].format(
                i["id"],
                i["nama"],
                i["jk"],
                i["lembaga"],
                i["s"],
                i["i"],
                i["a"],
            )
            temp.append(text)
    return temp