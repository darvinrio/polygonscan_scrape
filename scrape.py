from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd
import time

print('scraping started')
driver = webdriver.Safari()

# XPATH of PolygonScan
# Symbol
# /html/body/div[1]/main/div[5]/div[1]/div[1]/div/div[2]/div[2]/div[2]/span[1]/b
# 
# Decimals
# /html/body/div[1]/main/div[5]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]
#
# Contract
# /html/body/div[1]/main/div[5]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/a[1]


def scrapeLink(address):
    link = 'https://polygonscan.com/token/'+address # '0x750e4c4984a9e0f12978ea6742bc1c5d248f40ed'
    driver.get(link)

    symbol = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[5]/div[1]/div[1]/div/div[2]/div[2]/div[2]/span[1]/b").text
    decimals = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[5]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]").text
    contract = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[5]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/a[1]").text

    print(symbol)
    print(decimals)
    print(contract)

    return {
        "contract":contract,
        "symbol":symbol,
        "decimals":decimals.replace('\n', '')
    }

df = pd.read_csv('poly_tokens.csv')

info_dict = []
i = 1
for token in df['token0'] :
    # print(token)
    info_dict+= [scrapeLink(token)]
    # break
    # if token == '0xe5417af564e4bfda1c483642db72007871397896' :
        # break
    i+= 1
    if i%10 == 0 :
        time.sleep(5)
    
    

print(info_dict)
out_df = pd.DataFrame.from_dict(info_dict)
out_df.to_csv('info.csv')