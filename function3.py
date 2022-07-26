# function3.py
# 기본값이 있는경우
def times(a=10,b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드인자
def connectURI(server, port):
    strURL = "httep://" + server + ":" + port
    return strURL

#호출
print(connectURI("credu.com", "80"))
print(connectURI(port="80", server="credu.com"))

#가변인자
def union(*ar):
    result = []
    for item in ar:     #그룹안의 단어 2개를 쪼갬
        for x in item:      #단어는 알파벳으로 쪼갬
            if x not in result:
                result.append(x)
    return result

#호출
print(union("PARK", "AK"))
print(union("union","knight","run","pray"))

#정의되지 않은 인자(필수와 옵션이 있는경우)
def userURIbuilder(server, port, **user):
    strURL = "httep://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

#호출
print(userURIbuilder("ruliweb.com", "80", id = "kim"))
print(userURIbuilder("ruliweb.com", "80", id = "kim", passwd = "1234"))

#람다함수(이름이 없는 간결한 함수 정의)
g = lambda x,y:x*y
print(g(2,8))
print(g(3,4))
print((lambda x:x*x)(3))
print(globals())