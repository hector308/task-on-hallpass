#manuel aguado, hector martinez
students = ["manny", "hector", "alice", "armando", "john", "bob", "jane", "hector"]
time = ['6', '4', '3', '8', '5', '11', '7', '7'] 

oktime = 5
warningtime = 9
flaggedtime = 10
bob_count= students.count("bob")


for x, y in zip(students, time):
    y = int(y) 
    
    if y >= flaggedtime or bob_count>=1:
        status = "FLAGGED"
    elif y >= warningtime:
        status = "WARNING"
    elif y >= oktime:
        status = "OK"
    else:
        status = "WARNING"   

    print(x, y, status)
