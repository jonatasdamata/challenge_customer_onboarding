from clicknium import clicknium as cc, locator, ui 
import csv

# Abrindo o site do desafio
var_tabChrome = cc.chrome.open("https://pathfinder.automationanywhere.com/challenges/automationanywherelabs-customeronboarding.html")

# Abrir o arquivo CSV
with open('customer-onboarding-challenge.csv', mode='r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# Exibe os dados da tabela (as linhas)
for row in rows[1:]:  # Ignorando a primeira linha, pois é um cabeçalho

    # Armazena as variáveis de cada cliente
    company_name = row[0]
    company_id = row[1]
    primary_contact = row[2]
    street_address = row[3]
    customer_city = row[4]
    customer_state = row[5]
    customer_zip = row[6]
    customer_email = row[7]
    active_discount = row[8]
    customer_on_file = row[9]

    # Localizando o campo de entrada de "company_name" usando o XPath e preenchendo 
    xpath = '//*[@id="customerName"]'
    element = var_tabChrome.find_element_by_xpath(xpath)
    element.set_text(company_name)

    # Localizando o campo de entrada de "customer ID" usando o XPath e preenchendo 
    xpath = '//*[@id="customerID"]'
    element = var_tabChrome.find_element_by_xpath(xpath)
    element.set_text(company_id)

    # Localizando o campo de entrada de "primary contact" usando o XPath e preenchendo 
    xpath = '//*[@id="primaryContact"]'
    element = var_tabChrome.find_element_by_xpath(xpath)
    element.set_text(primary_contact)

    # Localizando o campo de entrada de "street" usando o XPath e preenchendo 
    xpath = '//*[@id="street"]'
    element = var_tabChrome.find_element_by_xpath(xpath)
    element.set_text(street_address)

    # Localizando o campo de entrada de "city usando o XPath e preenchendo 
    xpath = '//*[@id="city"]'
    element = var_tabChrome.find_element_by_xpath(xpath)
    element.set_text(customer_city)

    # Localizando o campo de entrada de "state" usando o XPath e preenchendo 
    xpath = '//*[@id="state"]'
    element = var_tabChrome.find_element_by_xpath(xpath)
    element.send_hotkey(customer_state)

    # Localizando o campo de entrada de "zip" usando o XPath e preenchendo 
    xpath = '//*[@id="zip"]'
    element = var_tabChrome.find_element_by_xpath(xpath)
    element.set_text(customer_zip)

    # Localizando o campo de entrada de "email" usando o XPath e preenchendo 
    xpath = '//*[@id="email"]'
    element = var_tabChrome.find_element_by_xpath(xpath)
    element.set_text(customer_email)

    # Localizando o campo de entrada de "active discount" usando o XPath e preenchendo 
    if active_discount.strip().lower() == "yes":
        # Seleciona a opção "yes"
        xpath = '//*[@id="activeDiscountYes"]'
        element = var_tabChrome.find_element_by_xpath(xpath)
        element.click()
    elif active_discount.strip().lower() == "no":
        xpath = '//*[@id="activeDiscountNo"]'
        element = var_tabChrome.find_element_by_xpath(xpath)
        element.click()
    
    # Localizando o checkbox "Non-Disclosure Agreement (NDA)"
    xpath = '//*[@id="NDA"]'
    nda_checkbox = var_tabChrome.find_element_by_xpath(xpath)

    if customer_on_file.strip().lower() == "yes":
        # Marca o checkbox
        nda_checkbox.click()

    # Clica no botão de envio
    submit_button = var_tabChrome.find_element_by_xpath('//*[@id="submit_button"]')
    submit_button.click()
