# write
f = open('test.txt', 'w')
f.write('test\n')
print('Test print.', file=f)
f.close()

with open('test.txt', 'w') as f:
    print('이렇게 하면 Auto Close')

s = """
AAA
BBB
CCC
DDD
"""
# w+ 라고 하면 읽기 쓰기 모두 가능. read를 먼저 하는 경우에는 r+로 해야 한다.
# with open('test1.txt', 'w') as f:
#     f.write(s)
with open('test1.txt', 'r') as f:
    while True:
        # line = f.readline()
        # print(line, end='')
        # 두 글자씩 읽을 때 chunk 사용 가능.. 네트워크 패킷 옮길 때도 쓴다.
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break
    
    # 사용법을 잘 모르겠다.
    # f.seek(0) 이렇게 하면 元に戻る라고 했다.
    # print(f.read(1))

