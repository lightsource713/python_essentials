## solicitará a entrada do usuário após cada chamada da função message(), aguardará a entrada e armazenará o valor em a, b e c

def message():
    return int(input("Enter a value: "))

a = message()
b = message()
c = message()

print(a, b, c, sep=', ')