# soz+itemsi qaytarmalidir

items = [1,2,3,4]
string = "emp"
vurma = list(map(lambda x: string + str(x), items))
print(vurma)

# bu da onun funksiya versiyasidir

def my_function(string, items):
    return(list(map(lambda x: string + str(x), items)))

print(my_function("sas", [2,3,4]))



