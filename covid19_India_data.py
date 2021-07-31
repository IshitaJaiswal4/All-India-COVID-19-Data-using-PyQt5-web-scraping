import requests
import bs4
import pandas as pd


class covid19:

    def __init__(self):

        self.headers = {
            'authority': 'www.amazon.in',
            'cache-control': 'max-age=0',
            'rtt': '300',
            'downlink': '1.5',
            'ect': '4g',
            'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
            'sec-ch-ua-mobile': '?0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'session-id=258-4901071-8099064; i18n-prefs=INR; ubid-acbin=259-0690325-9018428; session-token=Y23RRJoA1bMEukwK8tug/8koVhfuMa/TyxvB0zSMPY+6js5ckAGF7cUqNPZnQwINbCD90/aNZYAxDCPZWPsDXCcAFa+eVEhVi09yTZKkhQd0ooKhmexSLtFaCikAdyYjnKL8YAUD+jm+qLzyAbfg3K9Lhqvs9IPGwiycNTPnzNchhEcGdLcd7mSIajRGv35H; session-id-time=2082758401l; csm-hit=tb:P8T49ANRMPQ93DY0NVVD+s-WX9MC1A4N74QA64PCF8P^|1627393368469&t:1627393368469&adb:adblk_no',
        }

        self.url = 'https://www.mygov.in/covid-19'

    def covid_data(self):

        covid_data = {
            'State': [],
            'Confirmed': [],
            'Active': [],
            'Discharged': [],
            'Deaths': [],
            'Vaccination': []
        }

        response = requests.get(self.url, headers=self.headers)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')

        if response.status_code == 200:
            divs = soup.find_all('div', attrs={'class': 'views-row'})

            for div in divs:
                try:
                    state = div.find('span', attrs={'class': 'st_name'}).text.strip()
                    confirmed = div.find('div', attrs={'class': 'tick-confirmed'}).small.text.strip()
                    active = div.find('div', attrs={'class': 'tick-active'}).small.text.strip()
                    discharged = div.find('div', attrs={'class': 'tick-discharged'}).small.text.strip()
                    deaths = div.find('div', attrs={'class': 'tick-death'}).small.text.strip()
                    vaccination = div.find('div', attrs={'class': 'tick-total-vaccine'}).small.text.strip()

                    covid_data['State'].append(state)
                    covid_data['Confirmed'].append(confirmed)
                    covid_data['Active'].append(active)
                    covid_data['Discharged'].append(discharged)
                    covid_data['Deaths'].append(deaths)
                    covid_data['Vaccination'].append(vaccination)

                except Exception as error:
                    break

            covid_data = pd.DataFrame(covid_data)

            return covid_data

        else:
            print("ERROR!! Status Code : ", response.status_code, 'Reason: ', response.reason)

if __name__ == '__main__':

    covid19 = covid19()
    data = covid19.covid_data()
    print(data)