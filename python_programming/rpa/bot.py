from selenium import webdriver
import pyautogui as p


def AbrirSite(driver):
    try:
        driver.maximize_window()
        driver.get('https://web.whatsapp.com/')
        
        wapp = None
        entrou = None
        while wapp == None:
            print('buscando tela para QR code')
            p.sleep(3)
            wapp = p.locateCenterOnScreen('C:/Repositorios/python_projects/python_programming/rpa/ima/wapp.PNG', confidence = 0.9)
            if wapp != None:
                print('achou logo')
                while entrou == None:
                    print('buscando tela whatsapp')
                    p.sleep(3)
                    entrou = p.locateCenterOnScreen('C:/Repositorios/python_projects/python_programming/rpa/ima/entrou.PNG', confidence = 0.9)
                    if entrou != None:
                        print('entrou')
                        p.sleep(5)
        
        while True:
            print('buscando barra de pesquisa')
            try:
                driver.find_element("xpath", '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys('teste')
                break
            except Exception as e:
                print(e)
                try:
                    driver.find_element("xpath", '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]').send_keys('teste')
                    break
                except Exception as e:
                    print(e)
                    try:
                        driver.find_element("xpath", '//*[@id="side"]/div[1]/div/div/div[2]/div').send_keys('teste')
                        break
                    except Exception as e:
                        print(e)
                        p.sleep(1)
        
        p.sleep(13)

        for i in range(50):
            try:
                lst = driver.find_element("xpath", f'/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div[{i}]').text
                print(lst)
                print()
            except Exception as e:
                p.sleep(1)
                print(e)
        
    except Exception as e:
        print(e)
        
    
if __name__ == '__main__':
    driver = webdriver.Chrome('C:/Repositorios/python_projects/python_programming/rpa/driver/chromedriver.exe')
    AbrirSite(driver)