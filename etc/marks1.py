# mark1.py
marks = [80, 25, 60, 70, 45]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번학생은 합격입니다." % number)
    else:
        print("%d번학생은 불합격입니다." % number)
