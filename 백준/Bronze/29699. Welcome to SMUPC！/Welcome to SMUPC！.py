s = "WelcomeToSMUPC"
n = int(input())
if n >= 14:
    print(s[n%14-1])
else:
    print(s[n-1])