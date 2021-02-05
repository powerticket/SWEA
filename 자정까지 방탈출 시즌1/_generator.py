from bs4 import BeautifulSoup
import requests
import datetime

problem_number = input('문제 번호를 입력하세요: ')

baekjoon_url = 'https://www.acmicpc.net/problem/'
request = requests.get(baekjoon_url + f'{problem_number}')
if request.status_code == 200:
    soup = BeautifulSoup(request.text, 'html.parser')
    problem_title = soup.select_one('#problem_title').text.strip()
    sample_input = soup.select_one('#sample-input-1').text.strip()

    year, month, day = str(datetime.date.today()).split('-')
    f = open(f'{month}{day}_{problem_number}.txt', 'w', encoding='utf-8')
    for line in sample_input.splitlines():
        f.write(line)
        f.write('\n')
    f.close()
    f = open(f'{month}{day}_{problem_number}.py', 'w', encoding='utf-8')
    f.write(f"""import sys
sys.stdin = open('test.txt', 'r')

# {month}/{day}
# {problem_number} {problem_title}

""")
    f.close()
    print('생성되었습니다.')
else:
    print('문제가 존재하지 않습니다.')
