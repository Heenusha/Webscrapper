import os
from selenium import webdriver
import bs4
import requests
import pandas as pd
from selenium.webdriver.common.keys import Keys


def subfinder(temp_str):
  if str(temp_str).find("/digital-factorial/Digital/")>=0:
    return 1
  else:
    return 0


temp_str=""

# get the path of ChromeDriverServer
#dir = os.path.dirname(__file__)
chrome_driver_path ="chromedriver.exe"

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("https://dcxstore.capgemini.com/")

headers = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
          }

login_data = {
    'LARES' : 'PGxpYjpBdXRoblJlc3BvbnNlIHhtbG5zOmxpYj0iaHR0cDovL3Byb2plY3RsaWJlcnR5Lm9yZy9zY2hlbWFzL2NvcmUvMjAwMi8xMiIgeG1sbnM6c2FtbD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6MS4wOmFzc2VydGlvbiIgeG1sbnM6c2FtbHA9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjEuMDpwcm90b2NvbCIgeG1sbnM6ZHM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG1sZHNpZyMiIHhtbG5zOnhzaT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2UiIFJlc3BvbnNlSUQ9InMwMjYyZTcwM2E5YjM5ZTI1MmRhYmQ0NDM3NWM3NGQwZDk1N2E0ZWZlIiAgSW5SZXNwb25zZVRvPSIxNTU3Mjk1NjE1MjY0IiBNYWpvclZlcnNpb249IjEiIE1pbm9yVmVyc2lvbj0iMCIgSXNzdWVJbnN0YW50PSIyMDE5LTA1LTA4VDA2OjA3OjA5WiI+PHNhbWxwOlN0YXR1cz4KPHNhbWxwOlN0YXR1c0NvZGUgVmFsdWU9InNhbWxwOlN1Y2Nlc3MiPgo8L3NhbWxwOlN0YXR1c0NvZGU+Cjwvc2FtbHA6U3RhdHVzPgo8c2FtbDpBc3NlcnRpb24gIHhtbG5zOnNhbWw9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjEuMDphc3NlcnRpb24iIHhtbG5zOnhzaT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2UiICB4bWxuczpsaWI9Imh0dHA6Ly9wcm9qZWN0bGliZXJ0eS5vcmcvc2NoZW1hcy9jb3JlLzIwMDIvMTIiICBpZD0ic2ZlYzI3MTEzMzIxY2FkNDJjOWU5NTc1YWU5ZjA1Y2U4MDgxM2YwODQwNCIgTWFqb3JWZXJzaW9uPSIxIiBNaW5vclZlcnNpb249IjAiIEFzc2VydGlvbklEPSJzZmVjMjcxMTMzMjFjYWQ0MmM5ZTk1NzVhZTlmMDVjZTgwODEzZjA4NDA0IiBJc3N1ZXI9Imh0dHBzOi8vc2lnbmluY29ycDA0LmNhcGdlbWluaS5jb206NDQzL29wZW5zc28vY2Rjc2VydmxldCIgSXNzdWVJbnN0YW50PSIyMDE5LTA1LTA4VDA2OjA3OjA5WiIgSW5SZXNwb25zZVRvPSIxNTU3Mjk1NjE1MjY0IiB4c2k6dHlwZT0ibGliOkFzc2VydGlvblR5cGUiPgo8c2FtbDpDb25kaXRpb25zICBOb3RCZWZvcmU9IjIwMTktMDUtMDhUMDY6MDc6MDlaIiBOb3RPbk9yQWZ0ZXI9IjIwMTktMDUtMDhUMDY6MDg6MDlaIiA+CjxzYW1sOkF1ZGllbmNlUmVzdHJpY3Rpb25Db25kaXRpb24+CjxzYW1sOkF1ZGllbmNlPmh0dHBzOi8vZGN4c3RvcmUuY2FwZ2VtaW5pLmNvbTo0NDMvYW1hZ2VudDwvc2FtbDpBdWRpZW5jZT4KPC9zYW1sOkF1ZGllbmNlUmVzdHJpY3Rpb25Db25kaXRpb24+Cjwvc2FtbDpDb25kaXRpb25zPgo8c2FtbDpBdXRoZW50aWNhdGlvblN0YXRlbWVudCAgQXV0aGVudGljYXRpb25NZXRob2Q9IktlcmJlcm9zIiBBdXRoZW50aWNhdGlvbkluc3RhbnQ9IjIwMTktMDUtMDhUMDY6MDc6MDlaIiBSZWF1dGhlbnRpY2F0ZU9uT3JBZnRlcj0iMjAxOS0wNS0wOFQwNjowODowOVoiIHhzaTp0eXBlPSJsaWI6QXV0aGVudGljYXRpb25TdGF0ZW1lbnRUeXBlIj48c2FtbDpTdWJqZWN0ICAgeHNpOnR5cGU9ImxpYjpTdWJqZWN0VHlwZSI+PHNhbWw6TmFtZUlkZW50aWZpZXIgTmFtZVF1YWxpZmllcj0iaHR0cHM6Ly9zaWduaW5jb3JwMDQuY2FwZ2VtaW5pLmNvbTo0NDMvb3BlbnNzby9jZGNzZXJ2bGV0Ij5BUUlDNXdNMkxZNFNmY3h6Vi03Mnl3Z2NvYmhkSXJNbVFpVFplcUc4Y2tDRFVzNC4qQUFKVFNRQUNNRE1BQWxOTEFCUXRORFF5T0RreE9EWTNNemt5TWpnMU9UVTFNUUFDVXpFQUFqQTAqPC9zYW1sOk5hbWVJZGVudGlmaWVyPgo8c2FtbDpTdWJqZWN0Q29uZmlybWF0aW9uPgo8c2FtbDpDb25maXJtYXRpb25NZXRob2Q+dXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6MS4wOmNtOmJlYXJlcjwvc2FtbDpDb25maXJtYXRpb25NZXRob2Q+Cjwvc2FtbDpTdWJqZWN0Q29uZmlybWF0aW9uPgo8bGliOklEUFByb3ZpZGVkTmFtZUlkZW50aWZpZXIgIE5hbWVRdWFsaWZpZXI9Imh0dHBzOi8vc2lnbmluY29ycDA0LmNhcGdlbWluaS5jb206NDQzL29wZW5zc28vY2Rjc2VydmxldCIgPkFRSUM1d00yTFk0U2ZjeHpWLTcyeXdnY29iaGRJck1tUWlUWmVxRzhja0NEVXM0LipBQUpUU1FBQ01ETUFBbE5MQUJRdE5EUXlPRGt4T0RZM016a3lNamcxT1RVMU1RQUNVekVBQWpBMCo8L2xpYjpJRFBQcm92aWRlZE5hbWVJZGVudGlmaWVyPgo8L3NhbWw6U3ViamVjdD48c2FtbDpTdWJqZWN0TG9jYWxpdHkgIElQQWRkcmVzcz0iMTAuMjQ3LjE1Ny4xNiIgRE5TQWRkcmVzcz0ic2lnbmluY29ycDA0LmNhcGdlbWluaS5jb20iIC8+PGxpYjpBdXRobkNvbnRleHQ+PGxpYjpBdXRobkNvbnRleHRDbGFzc1JlZj5odHRwOi8vd3d3LnByb2plY3RsaWJlcnR5Lm9yZy9zY2hlbWFzL2F1dGhjdHgvY2xhc3Nlcy9QYXNzd29yZDwvbGliOkF1dGhuQ29udGV4dENsYXNzUmVmPjxsaWI6QXV0aG5Db250ZXh0U3RhdGVtZW50UmVmPmh0dHA6Ly93d3cucHJvamVjdGxpYmVydHkub3JnL3NjaGVtYXMvYXV0aGN0eC9jbGFzc2VzL1Bhc3N3b3JkPC9saWI6QXV0aG5Db250ZXh0U3RhdGVtZW50UmVmPjwvbGliOkF1dGhuQ29udGV4dD48L3NhbWw6QXV0aGVudGljYXRpb25TdGF0ZW1lbnQ+PC9zYW1sOkFzc2VydGlvbj4KPGxpYjpQcm92aWRlcklEPmh0dHBzOi8vc2lnbmluY29ycDA0LmNhcGdlbWluaS5jb206NDQzL29wZW5zc28vY2Rjc2VydmxldDwvbGliOlByb3ZpZGVySUQ+PC9saWI6QXV0aG5SZXNwb25zZT4K'
    }

cookies = {
    'Cookie': '__utmv=38494129.|1=UserId=238348d0d92c1434af7e89b1b90556c5=1; SSESS86d6d75daff39bad56ee2b105bb87166=kL5nhe5PwW0j12qsrVpQ696H9i8ssVVic3BpVd7Cask; __utmc=38494129; sso_1530614434646=VND_RSSO_V2.eyJpYXQiOjE1NTgxNzY5Nzg3ODksInNydiI6Imh0dHBzOi8vZ2RpdG11dGFwd3Y1NXAuY29ycC5jYXBnZW1pbmkuY29tL3Jzc28vIiwicmxtIjoiY2FwZ2VtaW5pLmNvbSIsInRva2VuSWQiOiJfOThkOWM5NDUtZGYzMS00NWI0LWI2NzEtOWMwYjM4N2FhYzcxIn0=; has_js=1; __utma=38494129.422593764.1557915836.1558176961.1558353352.5; __utmz=38494129.1558353352.5.3.utmcsr=signincorp.capgemini.com|utmccn=(referral)|utmcmd=referral|utmcct=/opensso/UI/Login; amlbcookie=04; brandNewDayProd=AQIC5wM2LY4SfcwHI5nKKxC7Alk8xZs941-9LoD7mqtRQFs.*AAJTSQACMDMAAlNLABMzNjA5NTcwNjIxNzA1NzIwNjkyAAJTMQACMDQ.*'
    }


#select all the links from the home page
homepage_links=[]
lists = driver.find_elements_by_css_selector('div a')
for a in lists:
  homepage_links.append(a.get_attribute('href'))
print(set(homepage_links))

#With the help of sublink (/digital-factorial/Digital) find the links of items listed from home page
list2=[]
for i in range(len(homepage_links)):
   if subfinder(homepage_links[i]):
     list2.append(homepage_links[i])
list2 = list(set(list2))
print(list2)


#Taking User input to select the link from homepage

link_count = int(input("Please select the link whose data you want from homepage 0 to 5 where 0:Content Management, 1:User Experience and Frontends, 2:Customer Management, 3:Smart process & Integration, 4:Digital Commerce, 5:Wincenter = "))
print(list2[link_count])
driver.get(list2[link_count])


#Extracting category names of each items
contentText = [i.text for i in driver.find_elements_by_tag_name('h2')]
print(contentText)

#Extracting all field contents(Name of app,category and by) of respective categories
all_links = [i.text for i in driver.find_elements_by_css_selector('span.field-content ')]
print(all_links)

#For extracting partial names from all links
list3=[]
for i,j in enumerate(all_links):
  if i % 3 == 0:
    list3.append(j)
print(list3)

'''
elem = driver.find_element_by_partial_link_text(list3[1])
elem.click()

to_extract_more = driver.find_elements_by_css_selector('li.pager__item a')
more_link = to_extract_more[0].get_attribute('href')
'''

#taking user input for the number of records whose information is to be extracted in jsons
record_count = int(input("Please enter no records needed in multiples of 4 for each category: "))
link_click =(record_count - 4) / 4

if link_click == 0:
  # Extracting all field contents of respective categories
  all_links = [i.text for i in driver.find_elements_by_css_selector('span.field-content')]
  print(all_links)

  # For extracting partial names from all links
  list3 = []
  list4 = []
  for i,j in enumerate(all_links):
    if i % 3 == 0:
      list4.append(j)
  list3 = list4[:8]
  print(list3)
  countlist = list(range(1,10))


  df = pd.DataFrame(columns=['Name', 'Category', 'Tags', 'Asset Type', 'Efforts(PD)', 'Version Name',
                                 'Asset Owner Name', 'Asset Owner Contact', 'Asset Owner Email', 'Asset Sector',
                                 'Asset Package', 'Asset Technology', 'Featured Content', 'Description',
                                     'Key Features', 'Country','Project Details','Collateral details'])
  for ele,count in zip(list3,countlist):
    with requests.Session() as s:
      elem = driver.find_element_by_partial_link_text(ele)
      elem.click()
      url = driver.page_source
    #driver.get(list2[0])

      #res = s.post(url, data=login_data, headers=headers, cookies=cookies, verify=False)
      soup = bs4.BeautifulSoup(url, 'lxml')

      list5 = []
      for all_details in soup.find_all('div', attrs={
        "class": "field-items"}):
        details = all_details.text.strip()
        print(details)
        list5.append(details)
      print(list5)

      Country_details = ''
      for all_details in soup.find_all('div', attrs={
        "class": "field-name-field-country"}):
        Country_details = all_details.text.strip()
        print("Details: " + Country_details)

      Project_details = ''
      for all_details in soup.find_all('fieldset', attrs={
        "id": "edit-group_project_details"}):
        Project_details = all_details.text.strip()
        print("Details: " + Project_details)

      Collateral_details = ''
      for all_details in soup.find_all('div', attrs={
        "class": "field-name-field-upload-collaterals"}):
        Collateral_details = all_details.text.strip()
        print("Details: " + Collateral_details)


      versionNum = list5[6] + '.' + list5[7] + '.' + list5[8]
      df.loc[count] = [list5[0], list5[1], list5[2], list5[3], list5[4], versionNum, list5[9],
                   list5[10], list5[11], list5[12], list5[13], list5[14], list5[15], list5[16], list5[17],Country_details,
                 Project_details,Collateral_details]

      df.to_excel("C:\\Users\\hchandwa\\AppData\\Local\\Programs\\Python\\Python37-32\\data.xlsx")
      df.to_json("C:\\Users\\hchandwa\\AppData\\Local\\Programs\\Python\\Python37-32\\test.JSON")
      print(df)
    driver.get(list2[link_count])
else:
  for click in range(int(link_click)):
    print(click)
    if click == 0:
      # Extracting all field contents of respective categories
      all_links = [i.text for i in driver.find_elements_by_css_selector('span.field-content ')]
      print(all_links)

      # For extracting partial names from all links
      list3 = []
      list4=[]
      for i, j in enumerate(all_links):
        if i % 3 == 0:
          list4.append(j)
      list3 = list4[:8]
      print(list3)
      countlist = list(range(1, 10))

      df = pd.DataFrame(columns=['sName', 'Category', 'Tags', 'Asset Type', 'Efforts(PD)', 'Version Name',
                                 'Aset Owner Name', 'Asset Owner Contact', 'Asset Owner Email', 'Asset Sector',
                                 'Asset Package', 'Asset Technology', 'Featured Content', 'Description',
                                 'Key Features', 'Country', 'Project Details', 'Collateral details'])


      for ele,count in zip(list3,countlist):
        with requests.Session() as s:
          elem = driver.find_element_by_partial_link_text(ele)
          elem.click()
          url = driver.page_source
          soup = bs4.BeautifulSoup(url, 'lxml')
        #driver.get(list2[0])

          list5 = []
          for all_details in soup.find_all('div', attrs={
            "class": "field-items"}):
            details = all_details.text.strip()
            print(details)
            list5.append(details)
          print(list5)

          Country_details = ''
          for all_details in soup.find_all('div', attrs={
            "class": "field-name-field-country"}):
            Country_details = all_details.text.strip()
            print("Details: " + Country_details)

          Project_details = ''
          for all_details in soup.find_all('fieldset', attrs={
            "id": "edit-group_project_details"}):
            Project_details = all_details.text.strip()
            print("Details: " + Project_details)

          Collateral_details = ''
          for all_details in soup.find_all('div', attrs={
            "class": "field-name-field-upload-collaterals"}):
            Collateral_details = all_details.text.strip()
            print("Details: " + Collateral_details)

          versionNum = list5[6] + '.' + list5[7] + '.' + list5[8]
          df.loc[count] = [list5[0], list5[1], list5[2], list5[3], list5[4], versionNum, list5[9],
                           list5[10], list5[11], list5[12], list5[13], list5[14], list5[15], list5[16], list5[17],
                           Country_details,
                           Project_details, Collateral_details]

          # writer = pd.ExcelWriter('C:\\Users\\hchandwa\\AppData\\Local\\Programs\\Python\\Python37-32\\test.xlsx', engine=
          # 'xlsxwriter')
          # df.to_excel(writer)

          df.to_excel("C:\\Users\\hchandwa\\AppData\\Local\\Programs\\Python\\Python37-32\\data.xlsx")
          df.to_json("C:\\Users\\hchandwa\\AppData\\Local\\Programs\\Python\\Python37-32\\test.JSON")
          print(df)
        driver.get(list2[link_count])


    to_extract_more = driver.find_elements_by_css_selector('li.pager__item a')
    more_link = to_extract_more[0].get_attribute('href')
    driver.get(more_link)

    # Extracting all field contents of respective categories
    all_links = [i.text for i in driver.find_elements_by_css_selector('span.field-content ')]
    print(all_links)

    # For extracting partial names from all links
    list3 = []
    list4= []
    for i, j in enumerate(all_links):
      if i % 3 == 0:
        list4.append(j)
    list3 = list4[:8]
    print(list3)

    if click >= 0:
      extended_count_list = (click+1) * 8 + 1
      count_list = list(range(extended_count_list, extended_count_list+8))


      df1 = pd.DataFrame(columns=['Name', 'Category', 'Tags', 'Asset Type', 'Efforts(PD)', 'Version Name',
                               'Asset Owner Name', 'Asset Owner Contact', 'Asset Owner Email', 'Asset Sector',
                               'Asset Package', 'Asset Technology', 'Featured Content', 'Description',
                               'Key Features', 'Country', 'Project Details', 'Collateral details'])

      for ele,count in zip(list3,count_list):
       with requests.Session() as s:
        elem = driver.find_element_by_partial_link_text(ele)
        elem.click()

        url = driver.page_source
        soup = bs4.BeautifulSoup(url, 'lxml')

        list5 = []
        for all_details in soup.find_all('div', attrs={
         "class": "field-items"}):
          details = all_details.text.strip()
          print(details)
          list5.append(details)
        print(list5)

        Country_details = ''
        for all_details in soup.find_all('div', attrs={
          "class": "field-name-field-country"}):
          Country_details = all_details.text.strip()
          print("Details: " + Country_details)

        Project_details = ''
        for all_details in soup.find_all('fieldset', attrs={
          "id": "edit-group_project_details"}):
          Project_details = all_details.text.strip()
          print("Details: " + Project_details)

        Collateral_details = ''
        for all_details in soup.find_all('div', attrs={
          "class": "field-name-field-upload-collaterals"}):
          Collateral_details = all_details.text.strip()
          print("Details: " + Collateral_details)

        versionNum = list5[6] + '.' + list5[7] + '.' + list5[8]
        df.loc[count] = [list5[0], list5[1], list5[2], list5[3], list5[4], versionNum, list5[9],
                       list5[10], list5[11], list5[12], list5[13], list5[14], list5[15], list5[16], list5[17],
                       Country_details,
                       Project_details, Collateral_details]

        # writer = pd.ExcelWriter('C:\\Users\\hchandwa\\AppData\\Local\\Programs\\Python\\Python37-32\\test.xlsx', engine=
        # 'xlsxwriter')
        # df.to_excel(writer)

        df.to_excel("C:\\Users\\hchandwa\\AppData\\Local\\Programs\\Python\\Python37-32\\data.xlsx",startrow=0)
        df.to_json("C:\\Users\\hchandwa\\AppData\\Local\\Programs\\Python\\Python37-32\\test.JSON")
        print(df)

        driver.get(more_link)
      driver.get(more_link)







