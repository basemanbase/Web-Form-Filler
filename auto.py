from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import math
import time

web = webdriver.Firefox()
df = pd.read_excel (r'auto.xlsx')
time.sleep(1)
web.get('https://itcentre.iita.org/add-new-extension/?ign_skip=itoms')


time.sleep(5)

for i in range(0,291):
    Location = web.find_element_by_name('wpcf-location')
    Location.click()
    time.sleep(1)


    select = Select(web.find_element_by_name('category[]'))
    select.select_by_visible_text("Group")
    time.sleep(1)

    fullName = (df.loc[i,'FullName'])
    Name = web.find_element_by_name('post_title')
    try:
        math.isnan(fullName)
    
    except:
        Name.send_keys(fullName)
    time.sleep(1)

    designation = (df.loc[i,'Designation'])
    desig = web.find_element_by_name('wpcf-designation')
    try:
        math.isnan(designation)
    except:
        desig.send_keys(designation)      
    time.sleep(1)
    
    office = (df.loc[i,'Office'])
    offExt = web.find_element_by_name('wpcf-office-extension')
    offExt.send_keys(int(office))
    time.sleep(1)
    #mobile = (df.loc[0,'Mobile'])
    #mobExt = web.find_element_by_name('wpcf-mobile-extension')
        
    #mobExt.send_keys(mobile)

    Secretary = (df.loc[i,'secretary'])
    secExt = web.find_element_by_name('wpcf-secretary-lab-extension')
    if math.isnan(Secretary) == False:
        secExt.send_keys(int(Secretary))
    time.sleep(1)
    home = (df.loc[i,'Home'])
    homExt = web.find_element_by_name('wpcf-home')
    if math.isnan(home) == False:
        homExt.send_keys(int(home))
    time.sleep(2)

    q = "wpt-form-submit form-submit submit"
    Location = web.find_element_by_css_selector(".btn.btn-primary.btn-lg.wpt-form-submit.form-submit.submit")
    Location.submit()
    time.sleep(5)

