#print(ord("hej"))



"""
def hashfunc(key):        #Vår egenskriven hashfunktion som returnerna våra "key's" till Hashtabellen.
    key1 = key[::-1]
    print(key1)
    hash_sum = 0
    for index,char in enumerate(key1):
        hash_sum = hash_sum + 31**(index+1) * ord(char)
        print(hash_sum)
    print(hash_sum%16)
"""
def hashfunc(key):        #Vår egenskriven hashfunktion som returnerna våra "key's" till Hashtabellen.
    n = len(key)
    keySum = 0 
    for x in range(n):
        keySum = keySum + ord(key[x]) #tar ascii värdet av varje bokstav och plussar ihop dem
        print(keySum)
    print (keySum%11) # modulus 11 men vi kör mudulus self.size i huvudfilen

hashfunc("hejj")
