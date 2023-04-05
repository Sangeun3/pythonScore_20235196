def convert_score(grade):
    score = 0
    if grade == 'A+':
        score = 4.5
    elif grade =='A':
        score = 4
    elif grade =='B+':
        score = 3.5
    elif grade =='B':
        score = 3
    elif grade =='C+':
        score = 2.5
    elif grade =='C':
        score = 2
    elif grade =='D+':
        score = 1.5
    elif grade =='D':
        score = 1
    elif grade =='F':
        score = 0
    return score

submit_credit, archive_credit = 0, 0
submit_gpa, archive_gpa = 0.0, 0.0

while True:
    print('작업을 선택하세요')
    print('     1. 입력')
    print('     2. 계산')

    user_value = input()

    if user_value.isdigit():
        value = int(user_value)

        if value == 1:
            print('학점을 입력하세요.')
            user_value = input()
            credit = int(user_value)

            print('펑점을 입력하세요.')
            user_value = input()
            gpa = convert_score(user_value)

            if gpa > 0:
                submit_credit += credit
                submit_gpa += gpa * credit
                archive_credit += credit
                archive_gpa += gpa * credit

        elif value == 2:
            submit_gpa /= submit_credit
            archive_gpa /= archive_credit

            print('제출용: ' + str(submit_credit) + ' (GPA: ' + str(submit_gpa) + ')')
            print('열람용: ' + str(archive_credit) + ' (GPA: ' + str(archive_gpa) + ')')

            break
    else:
        print("잘못된 입력입니다. 다시 입력하세요.")