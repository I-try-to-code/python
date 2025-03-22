import random 
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

 
sym = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
print("welcome")
n_let= int(input("enter the number of letters you want in your password: "))
n_sym= int(input("enter the number of symbols you want in your password: "))
n_num= int(input("enter the number of numbers you want in your password: "))

pas = []
for i in range(n_let):
    pas.append(random.choice(alpha))

for i in range(n_sym):
    pas.append(random.choice(sym));

for i in range(n_num):
    pas.append(random.choice(num));


a=n_let+n_num + n_sym 
a= int(a)

for i in range(a//2):
    u= random.randint(0,a//2)
    v= random.randint((a+1)//2,a-1)
    pas[u],pas[v]=pas[v],pas[u];

print("\n")
b=""

for i in range(a):
    b+=pas[i]

print(b)