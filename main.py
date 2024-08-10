from selenium import webdriver
from selenium.webdriver.common.by import By
import utils as utils


lista_cadastro = utils.read_excel("challenge.xlsx")
browser = webdriver.Chrome()

browser.get("https://rpachallenge.com/")
browser.find_element(By.XPATH, "//button[contains(.,'Start')]").click()

for dados_pessoa in lista_cadastro:
    browser.find_element(By.XPATH,"//label[contains(.,'First Name')]/..//input").send_keys(dados_pessoa['First Name'])
    browser.find_element(By.XPATH,"//label[contains(.,'Last Name')]/..//input").send_keys(dados_pessoa['Last Name '])
    browser.find_element(By.XPATH,"//label[contains(.,'Company Name')]/..//input").send_keys(dados_pessoa['Company Name'])
    browser.find_element(By.XPATH,"//label[contains(.,'Role in Company')]/..//input").send_keys(dados_pessoa['Role in Company'])
    browser.find_element(By.XPATH,"//label[contains(.,'Address')]/..//input").send_keys(dados_pessoa['Address'])
    browser.find_element(By.XPATH,"//label[contains(.,'Email')]/..//input").send_keys(dados_pessoa['Email'])
    browser.find_element(By.XPATH,"//label[contains(.,'Phone Number')]/..//input").send_keys(dados_pessoa['Phone Number'])
    browser.find_element(By.XPATH,"//input[@value='Submit']").click()
    
    print(
        f"Foram preenchidos os seguintes dados: \n"
        f"Nome: {dados_pessoa['First Name']};\n"
        f"Sobrenome: {dados_pessoa['Last Name ']};\n"
        f"Nome da Empresa: {dados_pessoa['Company Name']};\n"
        f"Função: {dados_pessoa['Role in Company']};\n"
        f"Endereço: {dados_pessoa['Address']};\n"
        f"Email:{dados_pessoa['Email']};\n"
        f"Telefone: {dados_pessoa['Phone Number']}\n"
        )
    

