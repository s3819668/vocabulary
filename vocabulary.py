import random
class vocabulary:
    def __init__(self,eng,chi):
        self.eng=eng
        self.chi=chi
        self.options=[chi]
###txt.read
def list_to_str(l):
    str=""
    for i in l:
        str+=i
        str+=" "
    return str
with open("vocabulary.txt","r",encoding="utf-8") as f:
    #讀檔
    read_vocabularys=[i[:-1] for i in f.readlines()]
    saperate=[i.split(" ") for i in read_vocabularys]
    all_chi=[i[-1] for i in saperate]
    all_eng=[i[0:-1] for i in saperate]
    vocabularys=[vocabulary(list_to_str(i[0:-1]),i[-1]) for i in saperate]
    #建立題目
    for v in vocabularys:
        while len(v.options)<4:
            option=all_chi[random.randint(0,len(all_chi)-1)]
            if option not in v.options and option !=v.chi:
                v.options.append(option)
        #打散選項
        random.shuffle(v.options)
    #打散題目順序
    random.shuffle(vocabularys)
    count=0#分數
    total=100#總分
    incorrect=[]
    # 主程式預設重複開始
    again=1
    all_vocabularys=vocabularys
    while(again):
        exam_no=1
        random.shuffle(all_vocabularys)
        vocabularys=all_vocabularys[0:int(input("要寫幾題"))]
        for v in vocabularys:
            illegal=0
            not_answered = 1
            while(illegal or not_answered):
                print(exam_no,". ",v.eng ,sep="")
                for i, option in enumerate(v.options):
                    print("  ",i + 1, option)
                illegal=0
                not_answered = 1
                try:
                    user_answer=int(input()) - 1
                    if user_answer==-1:
                        raise BaseException()
                    if v.chi == v.options[user_answer]:
                        count += total / len(vocabularys)
                        not_answered = 0
                    else:
                        incorrect.append(v)
                        not_answered = 0
                except:
                    illegal=1
                    print("輸入錯誤")
            exam_no += 1
        if len(incorrect):
            print("錯了這些")
            for i in incorrect:
                print(i.eng,i.chi)
        else:
            print("恭喜全對")
        print("得分:",count)
        print("再試一次?Y/N")
        again=(input()=="Y")
        count = 0
        incorrect = []
    f.close()




