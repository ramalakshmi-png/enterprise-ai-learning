me = {
"name":"Rama",
"experience":17,
"city":"Chennai",
"technology":".NET"
}
#print(me)
#print(me["technology"])
#print(me.get("city"))
#me["hobby"] = "Reading"
#print(me)
#me["hobby"]="cooking"
#print(me)
for key in me:
    print(key)
for value in me.values():
    print(value)
for key, value in me.items():
    print(key.upper(),":", value)