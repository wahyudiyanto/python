baris = 0
inp = input("nilai : ")
batas = int(inp)
s = ""
no = batas * batas


while baris < batas:
    kolom = 0

    while kolom < batas:
        s = s + str(no) + " "
        kolom = kolom + 1
        no = no - 1
        
    s = s + "\n"
    baris = baris + 1

print(s)