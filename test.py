

users = [
    {'spongebob':'squarepants'},
    {'sandy':'cheeks'},
    {'patrick': 'star'},
    {'larry':'lobster'},
]  
usernm = 'elana'
passwrd = 'lin'
  
for dic in users:
    for key in dic:
        if usernm is key and dic[usernm] == passwrd:
            print("Successfully logged in.", 'successful')
            
if usernm != users:
    users.append({usernm:passwrd})
    
print(users)