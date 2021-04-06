with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
for line in f:
    result = f.readline()
    print(result)