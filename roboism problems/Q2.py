def cred(n_str):
    try:
        if (type(int(n_str)==int)):
          if (len(n_str) == 16):
            t = n_str[len(n_str)-4:len(n_str)]
            ret_str = '*'*(len(n_str)-4)+t
          if(len(n_str) != 16):
            ret_str = 'Credit Card Should have 16 numbers'
    except:
        ret_str = 'You have not entered a valid credit card number'      
    return(ret_str)
n = '7658534627664735'# a credit card number
n1 = '2345216'# less than 16 digits
a = '1A23fg'# not a valid credit card number
print(cred(n))
print(cred(n1))
print(cred(a))