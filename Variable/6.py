import random

while True:
    print("\n마법의 소라고둥에게 물어보기 [예]/[아니요]")
    answer = input()

    if answer == '예':
        print("\n소라고둥에게 물어볼것을 입력하세요.")
        question = input()
        print("\n줄을 당기는중...\n")
        lotto = ['별로','좋아','나라면 안해','흠..다시 생각해봐','안돼','마법의 소라고둥님 께서 특별히 허락해주지','다른걸 선택해']
        random.shuffle(lotto)
        print(random.choice(lotto))
        
