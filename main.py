import requests, re
from bs4 import BeautifulSoup as bs


headers = {'accept':'*/*', 
  'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}


def get_hh():
    
    url = input("URL: ")
    n = int(input("n: "))
    stop = int(input("stop: "))
    f = open('links.txt', 'w')

    while n != stop:
        url2 = url + str(n)
        print(url2)
        session = requests.Session()
        request = session.get(url2, headers=headers)
        soup = bs(request.content, 'html.parser')
        data = soup.find_all('div', attrs={'class':'vacancy-serp-item'})
        for i in data:
            link = i.find('div', class_='resume-search-item__name').a['href']
            f.write(link + '\n')
        n += 1
        
    f.close()


def get_emails():

    file = 'links.txt'
    emails = []

    f = open(file, 'r') 
    f1 = open('emails.txt', 'w')
    session = requests.Session()
    line = f.readline()
    cnt = 1

    while line:  
        url = line.replace('\n', '')
        request = session.get(url, headers=headers)
        soup = bs(request.content, 'html.parser')
        try:
            email = soup.find('div', class_='vacancy-contacts__body').a.text        
            if email:
                print(email, url)
                f1.write(str(email))
                f1.write('\n')
                line = f.readline()
                cnt += 1
            if not email:
                line = f.readline()
                cnt += 1
        except:
            line = f.readline()
            cnt += 1
            pass

    f.close()
    return emails


def main(): 

    emails = 'emails.txt'
    checked = 'emails_checked.txt'

    f = open(emails, 'r')
    f1 = open(checked, 'w')

    checked = []
    doubled = []

    for receiver in f.readlines():

        email = re.sub('\n', '', receiver)

        if email in checked:
            print('{} is already in "checked"'.format(email))
            doubled.append(email)
        
        if not email in checked:
            print('{} appended to "checked"'.format(email))
            checked.append(email)

    print('Number of doubled is: {}, number of checked emails: {}'.format(len(doubled), len(checked)))

    for i in checked:
        f1.write(i)
        f1.write('\n')
    
    f1.close()
    f.close()      

        
get_hh()
get_emails()
main()

