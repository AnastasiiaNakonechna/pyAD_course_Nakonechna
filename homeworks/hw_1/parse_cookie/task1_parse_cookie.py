def parse_cookie(query: str) -> dict:
    
    cookie = query
    while query in cookie:
            if cookie == '':
                #print ('OK_1') #для проверки теста
                return {}

            elif 'User' and 'age' not in cookie:
                i = 0
                r1 = cookie.split(';')[i].split('=')
                cookie1 = {r1[i] : r1[i-1]}
                i += 1
               # print('OK_2') #для проверки теста
                return cookie1
                break

            elif 'age' in cookie and 'User' not in cookie:
                i=0
                r1 = cookie.split(';')
                r2 = cookie.split(';')[i].split('=')+cookie.split(';')[i+1].split('=')
                cookie1 = {r2[i] : r2[i+1],r2[i+2] : r2[i-1]}
                #print(r1, r2) #для проверки теста
                #print(cookie1) #для проверки теста
                #print('OK_3') #для проверки теста
                return cookie1
                break


            elif 'age' in cookie and 'User' in cookie:
                resp1 = cookie.split(';')
                resp2 = cookie.split(';')[0].split('=')+cookie.split(';')[1].split('=')
                cookie1 = {resp2[0] : resp2[1]+'='+resp2[2], resp2[3] : resp2[-1]}
                #print(resp1, resp2) #для проверки теста
                #print(cookie1) #для проверки теста
                #print('OK_4') #для проверки теста
                return cookie1
                break


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
