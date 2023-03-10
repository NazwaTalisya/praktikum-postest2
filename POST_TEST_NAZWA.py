def FiboSearching(arr,x):
    n = 0
    while fib(n) < len(arr):
        n = n + 1
    offset = -1
    for f in range(len(arr)):
            if type(arr[f]) == list:
                hasil_fibo = FiboSearching(arr[f],x)
                if hasil_fibo == -1:
                    arr[f] = "z"
                else:
                    print(x," ditemukan di indeks ", int(f)," pada kolom ",hasil_fibo)
                    exit()
    while (fib(n) > 1):
        i = min(offset + fib(n-2), len(arr) - 1)
        if (x > arr[i]):
            n = n-1
            offset = i
        elif (x < arr[i]):
            n = n-2
        else:
            return i
    if (fib(n-1) and arr[offset + 1] == x):
        return offset + 1
    return -1
def JumpSearching(arr,x,n):
    step = n**(1/2)
    prev = 0
    for p in range(len(arr)):
        if type(arr[p]) == list:  
            hasil_jump = JumpSearching(arr[int(p)],x,len(arr[int(p)]))
            if hasil_jump == -1:
                arr[int(p)] = 'z'
                print()
            else:
                print(x," ditemukan di indeks ", int(p)," pada kolom ",hasil_jump)
                exit()
    while arr[int(min(step, n)-1)] < x:
                prev = step
                step += n**(1/2)
                if prev >= n:
                    return -1
    while arr[int(prev)] < x:        
                prev += 1
                if prev == min(step, n):
                    return -1
    if arr[int(prev)] == x:
            return int(prev)
    return -1
def fib(n):
    if n < 1:
        return 1
    elif n == 1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
list_array = ['Arsel','Avivah','Daiva',['Wahyu','Wibi']]
panjangdata = len(list_array)
while True:
    print(f'''
Daftar Data
=============
|No | Nama  |
=============
| 1 | Arsel |
| 2 | Avivah|
| 3 | Daiva |
| 4 | Wahyu |
| 5 | Wibi  |
|============
''')
    print('''
    ======================
    | 1. Jump Search     |
    | 2. Fibonacci Search|
    ======================
    ''')
    a1 = int(input("Masukan nomor searching yang ingin dipakai: "))
    input_data = input("Masukan data yang ingin dicari: ")
    if a1 == 1:
        search_1 = JumpSearching(list_array,input_data,panjangdata)
        if search_1 == -1:
            print(input_data," tidak ditemukan")
        else:
            print(input_data," ditemukan di indeks ",search_1)
        exit()
    elif a1 == 2:
        search_2 = FiboSearching(list_array,input_data)
        if search_2 == -1:
            print(input_data," tidak ditemukan")
        else:
            print(input_data," ditemukan di indeks ",search_2)
        exit()

    else:
        print("Masukan input dengan benar")