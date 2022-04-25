
# Global and local variables
# msg = "How r you?"
# def greet():
#     msg = "how do you do?"
#     print("inside the fn ==>", msg)
# greet()
# print("outside the fn ==>", msg)

# making global changes
msg = "How r you?"
def greet():
    global msg
    msg = "how do you do?"
    print("inside the fn ==>", msg)
greet()
print("outside the fn ==>", msg)