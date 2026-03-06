import pyautogui
import time
pyautogui.PAUSE=1
pyautogui.press ("win")
pyautogui.write("chrome")
pyautogui.press("enter")
#coloque aqui o link do site da empresa
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press ("enter")
time.sleep(5)
pyautogui.click(x=651, y=462)
#coloque aqui o email
pyautogui.write("seu_email_aqui")
pyautogui.press("tab")
#coloque aqui sua senha
pyautogui.write("sua_senha_aqui")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(5)
import pandas 
tabela=pandas.read_csv("produtos.csv")
print(tabela)
for linha in tabela.index:
    pyautogui.click (x=704, y=320)  
    codigo=str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    marca= str(tabela.loc[linha,"marca"])
    pyautogui.write (marca)
    pyautogui.press ("tab")
    tipo= str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo)
    pyautogui.press ("tab")
    categoria=str(tabela.loc[linha, "categoria"])
    pyautogui.write("categoria")
    pyautogui.press("tab")
    preco_unitario=str(tabela.loc[linha,"preco_unitario"])   
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")  
    custo=str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    obs=str(tabela.loc[linha,"obs"])
    if obs!="nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)