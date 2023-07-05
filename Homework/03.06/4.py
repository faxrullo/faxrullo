import os
os.system("cls")
st=input("Gapni kiriting: ")
gap,suz=[],[]
gap_y,suz_y="",""
for x in st: 
    if x=="." or x=="!" or x=="?":
        gap.append(gap_y)
        gap_y=""
    else:
       gap_y+=x
    if x=="." or x=="!" or x=="?" or x==" " or x==",":
        suz.append(suz_y)
        suz_y=""
    else:
        suz_y+=x
if gap_y!="" and gap_y!="\n":
    gap.append(gap_y)
if suz_y!="" and suz_y!="\n":
    suz.append(suz_y)
print(f"Gaplar:{gap}\nSo'zlar: {suz}")

