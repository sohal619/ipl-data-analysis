import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException
import pandas as pd


class Ipl:
    def __init__(self):
        self.chrome_web = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.chrome_web)
        self.data_skeleton = {}

    def get_data(self, url, tag):
        self.data_skeleton = {'TEAMS': [],
                              'M': [],
                              'W': [],
                              'L': [],
                              'PT': [],
                              'NRR': []}

        self.driver.maximize_window()
        self.driver.get(url)
        bar = self.driver.find_element(By.XPATH, '/html')
        for k in range(10):
            bar.send_keys(Keys.ARROW_DOWN)

        data = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/section/div[5]/div[1]/div['
                                                  '3]/div/div/table/tbody')

        for x in range(1, 25, 2):
            time.sleep(5)
            match_info = {'data': [], 'scorecard': []}

            try:
                team_name = data.find_element(By.XPATH, f'/html/body/div[1]/section/section/div[5]/div[1]/div['
                                                        f'3]/div/div/table/tbody/tr[{x}]/td[1]/a/div/span')
                self.data_skeleton['TEAMS'].append(team_name.text)

                m = data.find_element(By.XPATH, f'/html/body/div[1]/section/section/div[5]/div[1]/div['
                                                f'3]/div/div/table/tbody/tr[{x}]/td[2]')
                self.data_skeleton['M'].append(m.text)

                w = data.find_element(By.XPATH, f'/html/body/div[1]/section/section/div[5]/div[1]/div['
                                                f'3]/div/div/table/tbody/tr[{x}]/td[3]')
                self.data_skeleton['W'].append(w.text)

                l = data.find_element(By.XPATH, f'/html/body/div[1]/section/section/div[5]/div[1]/div['
                                                f'3]/div/div/table/tbody/tr[{x}]/td[4]')
                self.data_skeleton['L'].append(l.text)

                pt = data.find_element(By.XPATH, f'/html/body/div[1]/section/section/div[5]/div[1]/div['
                                                 f'3]/div/div/table/tbody/tr[{x}]/td[7]')
                self.data_skeleton['PT'].append(pt.text)

                nrr = data.find_element(By.XPATH, f'/html/body/div[1]/section/section/div[5]/div[1]/div['
                                                  f'3]/div/div/table/tbody/tr[{x}]/td[8]')
                self.data_skeleton['NRR'].append(nrr.text)

                data.find_element(By.XPATH, f'/html/body/div/section/section/div[5]/div[1]/div['
                                            f'3]/div/div/table/tbody/tr[{x}]/td[9]/div').click()

                team_info = data.find_element(By.XPATH, f'/html/body/div/section/section/div[5]/div[1]/div['
                                                        f'3]/div/div/table/tbody/tr[{x+1}]/td/div/div/div/div')

                for j in range(1, 20):
                    try:
                        data = team_info.find_element(By.XPATH, f'/html/body/div[1]/section/section/div[5]/'
                                                                f'div[1]/div[3]/div/div/table/tbody/tr[{x+1}]/'
                                                                f'td/div/div/div/div/a[{j}]/div/div[2]')

                        scorecard_link = team_info.find_element(By.XPATH, f'/html/body/div[1]/section/section/div[5]'
                                                                          f'/div[1]/div[3]/div/div/table/tbody/'
                                                                          f'tr[{x+1}]/td/div/div/div/div/a[{j}]')
                        match_info['data'].append(data.text)
                        match_info['scorecard'].append(scorecard_link.get_attribute('href'))
                    except NoSuchElementException:
                        break
                df2 = pd.DataFrame(match_info)
                df2.to_csv(f'../Data cleaning/scraped data/match data {tag}/{team_name.text} {tag}.csv', index=False)

                data.find_element(By.XPATH, f'/html/body/div/section/section/div[5]/div[1]/div['
                                            f'3]/div/div/table/tbody/tr[{x}]/td[9]/div').click()

            except NoSuchElementException:
                break

    def save_data(self, tag):
        df = pd.DataFrame(self.data_skeleton)
        df.to_csv(f'../Data cleaning/scraped data/points table/data{tag}.csv', index=False)


link_flags = ['2007-08-313494', '2009-374163', '2009-10-418064', '2011-466304', '2012-520932', '2013-586733',
              '2014-695871', '2015-791129', '2016-968923', '2017-1078425', '2018-1131611', '2019-1165643',
              '2020-21-1210595', '2021-1249214', '2022-1298423']

ipl_match = Ipl()

for i, v in enumerate(link_flags, 2008):
    ipl_match.get_data(url=f'https://www.espncricinfo.com/series/indian-premier-league-{v}/points-table-standings',
                       tag=i)
    ipl_match.save_data(i)
