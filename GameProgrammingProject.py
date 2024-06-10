import random
import sys
import time
import os
import tkinter
from tkinter import *

cookingList = ["제육볶음", "잔치국수", "마늘빵", "볶음밥", "떡볶이", "치킨"]    #요리 제목 리스트
resourceList = ["돼지고기", "어묵", "밀가루", "국물용멸치", "계란", "소면", "닭고기", "떡", "바게트", "소고기", "밥", 
                "소세지", "빵가루", "양파", "대파", "김치", "당근", "식용유"]   #요리 재료 리스트
sauceList = ["고추장", "간장", "버터", "후추", "고춧가루", "다시다", "소금", "다진마늘"]      #조미료 리스트
bowlList = ["양은그릇", "유리볼", "넓은접시", "기름종이"]       #그릇 리스트
curLife = 3
curCook = "제육볶음"

selectResourceList = []
selectSauceList = []
selectBowl = ""
win = None
isSuccess = 0

#요리 제목: [[재료], [조미료], []] string: string 이중 리스트 딕셔너리
recipeDict = {"제육볶음": [["돼지고기", "대파", "양파", "당근"], ["고추장", "고춧가루", "간장", "후추"], ["넓은접시"]], 
              "잔치국수": [["소면", "당근", "계란", "국물용멸치"], ["다시다", "간장", "소금", "후추"], ["양은그릇"]],
              "마늘빵": [["다진마늘", "바게트"], ["버터", "꿀"], ["기름종이"]],
              "볶음밥": [["대파", "양파", "당근", "계란", "소세지", "밥", "식용유"], ["소금", "후추"], ["기름종이"]],
              "떡볶이": [["떡", "어묵", "양파", "대파"], ["고추장", "고춧가루", "간장", "소금", "후추", "다시다"], ["넓은접시"]],
              "치킨": [["닭고기", "밀가루", "빵가루", "식용유"], ["소금"], ["기름종이"]]}     

cooking = "" #현재 요리중인 요리 이름

def clear_grid(frame):
    # 현재 그리드에 배치된 모든 위젯을 가져와서 삭제
    for widget in frame.grid_slaves():
        widget.grid_forget()

def resourceTkinter():
    global resourceList
    global selectSauceList
    global curCook
    global win

    clear_grid(win)

    te = tkinter.Label(win, text=curCook, width=75, height=2, anchor="center")
    te.grid(row=0, column=0, columnspan=5)

    t = Text()
    t.delete("1.0", "end")
    t.insert(END, ", ".join(selectResourceList))
    t.grid(row=5, column=0, columnspan=5, sticky="we")

    for b in range(0, 4):
        for c in range(0, 5):
            try:
                btn = tkinter.Button(win, text = (resourceList[b * 5 + c].center(10)) , background = 'white', 
                                     height=4, width=15, command = lambda text=resourceList[b * 5 + c] : resourceSelect(text, t))
                btn.grid(row = b + 1, column=c)
            except IndexError:
                if (b * 5 + c) == 18:
                    btn = tkinter.Button(win, text="다음", background="white", height=4, width=30, 
                                         command=sauceTkinter)
                    btn.grid(row=4, column=3, columnspan=2, sticky="we")

    win.mainloop()

def resourceSelect(text, t):
    global selectResourceList

    if text not in selectResourceList:
        selectResourceList.append(text)
    else:
        selectResourceList.remove(text)
    
    t.delete("1.0", "end")
    t.insert(END, ", ".join(selectResourceList))
    t.grid(row=5, column=0, columnspan=5, sticky="we")

def sauceTkinter():
    global sauceList
    global selectSauceList
    global curCook
    global win

    clear_grid(win)
    
    te = tkinter.Label(win, text=curCook, width=50, height=2, anchor="center")
    te.grid(row=0, column=0, columnspan=4, sticky="we")

    t = Text()
    t.delete("1.0", "end")
    t.insert(END, ", ".join(selectSauceList))
    t.grid(row=4, column=0, columnspan=4, sticky="we")

    for b in range(0, 2):
        for c in range(0, 4):
            try:
                btn = tkinter.Button(win, text = (sauceList[b * 4 + c].center(10)) , background = 'white', 
                                        height=4, width=15, command = lambda text=sauceList[b * 4 + c] : sauceSelect(text, t))
                btn.grid(row = b + 1, column=c, sticky="we")
            except IndexError:
                pass
            
    btn = tkinter.Button(win, text="이전", background="white", height=4, width=15, command=resourceTkinter)
    btn.grid(row=3, column=0, sticky="w")
    
    win.grid_columnconfigure(2)

    btn = tkinter.Button(win, text="다음", background="white", height=4, width=15, command=bowlTkinter)
    btn.grid(row=3, column=3, sticky="e")

    win.mainloop()

def sauceSelect(text, t):
    global selectSauceList

    if text not in selectSauceList:
        selectSauceList.append(text)
    else:
        selectSauceList.remove(text)
    
    t.delete("1.0", END)
    t.insert(END, ", ".join(selectSauceList))
    t.grid(row=4, column=0, columnspan=4, sticky="we")

def bowlTkinter():
    global bowlList
    global selectBowl
    global curCook
    global win

    clear_grid(win)
    
    te = tkinter.Label(win, text=curCook, width=50, height=2, anchor="center")
    te.grid(row=0, column=0, columnspan=4, sticky="we")

    t = Text()
    t.delete("1.0", END)
    t.insert(END, selectBowl)
    t.grid(row=3, column=0, columnspan=4, sticky="wens")

    for c in range(0, 4):
        try:
            btn = tkinter.Button(win, text = (bowlList[c].center(10)) , background = 'white', 
                                    height=4, width=15, command = lambda text=bowlList[c] : bowlSelect(text, t))
            btn.grid(row = 1, column=c, sticky="we")
        except IndexError:
            pass
            
    btn = tkinter.Button(win, text="이전", background="white", height=4, width=15, command=sauceTkinter)
    btn.grid(row=2, column=0, sticky="w")
    
    win.grid_columnconfigure(2)

    btn = tkinter.Button(win, text="제출", background="white", height=4, width=15, command=cookCheck)
    btn.grid(row=2, column=3, sticky="e")

    win.mainloop()

def bowlSelect(text, t):
    global selectBowl

    selectBowl = text
    
    t.delete("1.0", END)
    t.insert(END, selectBowl)
    t.grid(row=3, column=0, columnspan=4, sticky="wens")

def mainGame():
    global curCook

    curCook = random.choice(cookingList)
    print(curCook + " 내 놔!")
    print()
    print("요리를 만들 식재료를 고르세요!")
    input("엔터 키를 누르면 시작합니다")

def cookCheck():
    global selectResourceList
    global selectSauceList
    global selectBowl
    global curCook
    global recipeDict
    global win
    global isSuccess

    win.destroy()

    for a in selectResourceList:
        if a not in recipeDict[curCook][0] or len(selectResourceList) != len(recipeDict[curCook][0]):
            isSuccess = 1
            return
    
    for a in selectSauceList:
        if a not in recipeDict[curCook][1] or len(selectSauceList) != len(recipeDict[curCook][1]):
            isSuccess = 2
            return
    
    if selectBowl != recipeDict[curCook][2][0]:
        isSuccess = 3
        return

    isSuccess = 4

#인트로
def introFirst():
    os.system("cls")
    print("여기 8연강을 마친 뒤 지치고 힘들고 찝찝하고 불쾌하고 아무튼 부정적인 정재웅이 있습니다.")
    time.sleep(1.5)
    print("이 때, 눈 앞에 안수형의 집이 보이는군요")
    time.sleep(1.3)
    print("\'수형이형은 늘 내게 밥을 해줬어...\'", end=" ")
    time.sleep(1)
    print("당장 쳐들어가자!")
    time.sleep(1.5)
    print("안수형 밥 줘! 밥 내놔!")
    time.sleep(1.5)
    print()
    print("이제부터 여러분은 안수형씨가 되어 정재웅에게 밥을 차려줘야합니다.")
    print("과연 여러분은 배고픈 정재웅을 만족시킬 수 있을까요?")
    print("부디 행운을 빕니다.")
    print()
    print("엔터 키를 눌러서 진행하세요")
    input("")

while True:
    os.system("cls")
    print()
    print("1. 게임시작")
    print("2. 게임설명")
    print("3. 제작자")
    print("4. 종료")
    
    a = input("번호를 입력하세요: ")
    if a == "1":
        mainGame()
        selectResourceList = []
        selectSauceList = []
        selectBowl = ""

        win = tkinter.Tk()
        win.geometry("800x600+100+100")
        win.resizable(False, False)
        resourceTkinter()
        os.system("cls")

        if isSuccess == 1:
            print("아니 이게 뭐야!")
            print(f"누가 {curCook}에 이런걸 넣어!")
            print("당장 이 집에서 나가!!")
            break
        elif isSuccess == 2:
            print("아니 이게 뭐야!")
            print(f"왜 {curCook}에서 이딴 맛이 나!")
            print("당장 이 집에서 나가!!")
            break
        elif isSuccess == 3:
            print("아니 이게 뭐야!")
            print(f"누가 {curCook}을 이딴 접시에 담아!")
            print("당장 이 집에서 나가!!")
            break
        elif isSuccess == 4:
            print("음 맛있는 밥을 만들었구만")
            print("약속한대로 집은 남겨두지")
            break
        else:
            print("버그가 났으니 프로그램을 종료해주세요.")
        
    elif a == "2":
       introFirst()
    elif a == "3":
        os.system("cls")
        print()
        print("프로그래밍 및 팀장: 송선")
        print("기획 및 출연: 정재웅")
        print("발표 및 늘 밥을 해준 사람: 안수형")
        print()
        print("엔터 키를 눌러서 진행하세요")
        input("")
    elif a == "4":
        sys.exit()
    else:
        print("다시 입력하세요.")
