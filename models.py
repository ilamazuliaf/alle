import xlrd

def dataDariExcel():
    book = xlrd.open_workbook("data.xlsx")
    sheet = book.sheet_by_index(0)
    temp = []
    for r in range(1,sheet.nrows):
        id = sheet.cell(r, 0).value
        nama = sheet.cell(r, 1).value
        lembaga = sheet.cell(r, 2).value
        s = sheet.cell(r, 3).value
        i = sheet.cell(r, 4).value
        a = sheet.cell(r, 5).value
        jk = sheet.cell(r, 6).value

        data = {
            "id" : id,
            "nama" : nama,
            "lembaga" : lembaga,
            "s" : int(s),
            "i" : int(i),
            "a" : int(a),
            "jk" : jk,
        }
        temp.append(data)
    return temp