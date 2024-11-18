from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = Options()
driver = webdriver.Chrome('C:/Users/Danix/Downloads/chromedriver-win64/chromedriver.exe', options=options)

books = 'https://books.toscrape.com/index.html'

lgen = []
lli = []
lp = []

driver.get(books)

for i in range(0,50):

    livros = driver.find_elements(By.TAG_NAME, 'a')[54:94:2]

    for i in livros:
        try:
            i.click()
            genero = driver.find_elements(By.TAG_NAME, 'a')[3]
            lgen.append(genero.text)

            livro = driver.find_elements(By.TAG_NAME, 'h1')
            lli.append(livro[0].text)

            preco = driver.find_elements_by_class_name('price_color')
            lp.append(preco[0].text)

            driver.back()
        except:
            pass

    try:
        driver.find_element_by_css_selector('#default > div > div > div > div > section > div:nth-child(2) > div > ul > li.next > a').click()
    except:
        print("Botão Next não encontrado")
        pass

dicionario = {'Livro':lli,
              'Genero': lgen,
              'Preco': lp}

df = pd.DataFrame(dicionario)

#Retirar simbolo de euro do valor
df['Preco'] = df['Preco'].str.replace('£', '').astype(float)

#passar para arquivo CSV
df.to_csv('livros.csv', encoding='utf-8', index=False)

driver.close()
