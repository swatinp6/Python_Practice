def palindrome(num):
    new=num[::-1]
    if(num==new):
        print("palindrome")
    elif(num!=new):
        print("not palindrome")
    else:
        print("enter word or num")
palindrome("madam")
palindrome("123")
palindrome(str(121))