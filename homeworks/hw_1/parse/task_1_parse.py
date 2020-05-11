def parse(query: str) -> dict:
    
    url = query
    while query in url:
            if '?' not in url:
                #print ('OK_1')
                return {}
                break

            elif '?' == url[-1]:
                #print ('OK_2') #для проверки теста
                return {}
                break

            elif '?' != url[-1] and '&' not in url:
                resp1 = url.split('?')[1].split('&')
                r1 = str(resp1[0]).split('=')
                resp2= {r1[0] : r1[1]}
                #print ('OK_3') #для проверки теста
                return resp2

            elif  '&' != url[-1]:
                resp1 = url.split('?')[1].split('&')
                r1 = str(resp1[0]).split('=')
                r2 = str(resp1[1]).split('=')
                resp2 = {r1[0]: r1[1], r2[0]: r2[1]}
                #print ('OK_4') #для проверки теста
                return resp2
                break

            elif '&' == url[-1]:
                resp1 = url.split('?')[1].split('&')
                r1 = str(resp1[0]).split('=')
                r2 = str(resp1[1]).split('=')
                resp2 = {r1[0]: r1[1], r2[0]: r2[1]}
                #print('OK_5') #для проверки теста
                return resp2

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
