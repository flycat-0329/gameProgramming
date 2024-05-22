import random
import sys
import time

cookingList = ["제육볶음", "잔치국수", "마늘빵", "볶음밥", "떡볶이", "치킨"]    #요리 제목 리스트
resourceList = ["돼지고기", "어묵", "밀가루", "국물용멸치", "어묵", "계란", "소면", "닭고기", "떡", "바게트", "소고기", "밥", 
                "소세지", "빵가루", "양파", "대파", "밥", "김치", "당근", "식용유"]   #요리 재료 리스트
sauceList = ["고추장", "간장", "버터", "후추", "고춧가루", "다시다", "소금", "다진마늘"]      #조미료 리스트
bowlList = ["양은그릇", "유리볼", "넓은접시", "기름종이"]       #그릇 리스트

#요리 제목: [[재료], [조미료], []] string: string 이중 리스트 딕셔너리
recipeDict = {"제육볶음": [["돼지고기", "대파", "양파", "당근"], ["고추장", "고춧가루", "간장", "후추"], ["넓은접시"]], 
              "잔치국수": [["소면", "당근", "계란", "국물용멸치"], ["다시다", "간장", "소금", "후추"], ["양은그릇"]],
              "마늘빵": [["다진마늘", "빵"], ["버터", "꿀"], ["기름종이"]],
              "볶음밥": [["대파", "양파", "당근", "계란", "소세지", "밥", "식용유"], ["소금", "후추"], ["기름종이"]],
              "떡볶이": [["떡", "어묵", "양파", "대파"], ["고추장", "고춧가루", "간장", "소금", "후추", "다시다"], ["넓은접시"]],
              "치킨": [["닭고기", "밀가루", "빵가루", "식용유"], ["소금"], ["기름종이"]]}     

cooking = "" #현재 요리중인 요리 이름

def recipePrint(cookName):
    a = 0
    print("재료", end = ": ")
    for a in range(0, len(recipeDict[cookName][0])):
        if a != len(recipeDict[cookName][0]) - 1:
            print(recipeDict[cookName][0][a], end = ", ")
        else:
            print(recipeDict[cookName][0][a])
    
    a = 0
    print("조미료", end = ": ")
    for a in range(0, len(recipeDict[cookName][1])):
        if a != len(recipeDict[cookName][1]) - 1:
            print(recipeDict[cookName][1][a], end = ", ")
        else:
            print(recipeDict[cookName][1][a])

    print(recipeDict[cookName][2][0] + "에 담아내 마무리한다.")

def introFirst():
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

while True:
    print()
    print("1. 게임시작")
    print("2. 게임설명")
    print("3. 제작자")
    print("4. 종료")
    
    a = input("번호를 입력하세요: ")
    if a == "1":
        cook = input("요리")
        recipePrint(cook)
    elif a == "2":
       introFirst()
    elif a == "3":
        print()
        print("프로그래밍 및 팀장: 송선")
        print("기획 및 출연: 정재웅")
        print("발표 및 늘 밥을 해준 사람: 안수형")
    elif a == "4":
        sys.exit()
    else:
        print("다시 입력하세요.")