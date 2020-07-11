'''
에라토스테네스의 체 사용
찾고자 하는 수 까지 True로 채운 리스트 생성 후 2의 배수, 3의 배수 등을 제거하여 리스트를 생성
N의 최댓값인 123456으로 소수를 구해 반복되는 실행에 시간 소모를 줄임
'''
'''
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 
'''
N = 123456 * 2 + 1
sieve = [True] * N

m = int(N ** 0.5)
for x in range(2, m + 1):
    if sieve[x] == True:
        for y in range(x + x, N, x):
            sieve[y] = False

while True:
    startNum = int(input())
    if startNum == 0:
        break
    endNum = startNum * 2

    print(list(map(lambda x:sieve[x],range(startNum+1, endNum+1))).count(True))