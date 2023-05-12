import requests
import json

file1 = open("info.txt","a")

# taking url from user
method,url = input("Enter the req :").split()
head = input("Do you want to modify headers(y/n) : ")
parameter = input("Do you want to give parameter(y/n) : ")

head_dict = {}
param_dict = {}

# checks header
if head == "y":
    h_n = int(input("Enter no. of headers : "))
    for i in range(h_n):
        key,value = input("Enter key & value : ").split()
        head_dict[key] = value

# checks parameter
if parameter == "y":
    p_n = int(input("Enter no. of parameters : "))
    for i in range(p_n):
        key,value = input("Enter key & value : ").split()
        param_dict[key] = value

#posting requests
if method == "post" :
    body_dict = {}
    k_n = int(input("Enter no of keys you want to post: "))
    for i in range(k_n):
        key,value = input("Enter key & value : ").split()
        body_dict[key] = value
    response = requests.post(url,headers = head_dict,params = param_dict,json = body_dict)
    
#storing response, content and header of url
elif method == "get":
    response  = requests.get(url,headers = head_dict,params = param_dict)

#put method
elif method == "put":
    put_dict ={}
    k_n = int(input("Enter no of keys you want to post: "))
    for i in range(k_n):
        key,value = input("Enter key & value : ").split()
        put_dict[key] = value
    response = requests.put(url,headers = head_dict,params = param_dict,data = put_dict )

#delete method
elif method == "delete":
    del_dict = {}
    d_n = int(input("Enter no of keys you want to delete : "))
    for i in range(d_n):
        key,value = input("Enter key & value : ").split()
        del_dict[key] = value

    response = requests.delete(url,headers = head_dict,params = param_dict,json = del_dict)

file1.write("\nURL: "+url+"  RESPONSE :"+str(response))
file1.close()

try:
    Content = json.dumps(response.json(),indent=4)
except:
    Content = response.content

Headers = response.headers
print(response)
print(Headers)
print(Content)
