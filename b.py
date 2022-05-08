"""
알아서 수정해서 제출하세요
"""
en=list(map(lambda ex: int(ex), input("list=").split()))
while 1:
    kei=int(input("k="))
    if kei==0 or kei==1 or kei>len(en): break
    print(max([sum([en[i+j] for j in range(kei) if i+j < len(en)]) for i in range(len(en))]))
