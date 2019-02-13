import random
# Talen som ska sorteras delas upp, halva åt gången
# Data som har samma längd
# Urvals-sortering
# Automagiskt: någon har löst problemet tidigare, och man behöver inte veta hur
# Nästlade for-slingor, den ena ligger i den andra


# Kollar inte värdet, utan positionen av värdet, tex minsta värdet låg på position 2
# Denna metod gör exakt samma arbete oavsett hur datan ser ut
def urvalssortera(data):
    n = len(data)
    for i in range(n):
        minst = i
        for j in range(i+1, n):
            if data[j] < data[minst]:
                minst = j
        data[minst], data[i] = data[i], data[minst]

# Bubbelsortering är något smartare metod, marginellt, den går igenom
# listan gång på gång tills inga byten sker
# Om listan är nästan sorterad från början räcker det med några få
# genomgångar och då blir bubbel snabbare än urval
# Jämför endast parvis, switchar plats på den vänstra och den högra, om vänstra > högra


def bubblesort(data):
    n = len(data)
    for i in range(n-1):
        done = True
        for j in range(n-i-1): # koden är fel, den jämför ej parvis
            if data[j+1] > data[j]: # jmf
                data[j+1], data[j] = data[j], data[j+1] # sw
                done = False
        if done:
            return

n = 100
data = []
for i in range(n):
    data.append(random.randint(0,1000))
print(data)
bubblesort(data)
print(data)
