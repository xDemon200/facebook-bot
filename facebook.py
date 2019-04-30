""" Facebook Bot """
""" Desarrollado por Juan Carlos Muñoz Guzmán """
""" 
    Version 1
        Funciones
            *Login
            *Commentar
            *Cerrar sesión
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

class FacebookBot():
    # Init
    def __init__(self, user, password):
        #Chrome o Firefox
        # need webdriver
        self.chromeoptions = webdriver.ChromeOptions()
        self.prefs = {
            "profile.default_content_setting_values.notifications": 2
        }
        self.chromeoptions.add_experimental_option("prefs", self.prefs)
        self.chromeoptions.add_argument("headless")
        self.chromeoptions.add_argument("disable-gpu")
        self.chromeoptions.add_argument("no-sandbox")       
        self.driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe', chrome_options=self.chromeoptions)
        self.user = user
        self.password = password
    
    def login_facebook(self):
        dr = self.driver
        dr.get('https://www.facebook.com/')
        time.sleep(2)
        print("Se ha cargado la web")
        # declare elements of web(facebook)
        elem_user = dr.find_element_by_xpath("//input[@id='email']")
        elem_user.clear()
        elem_user.send_keys(self.user)
        elem_password = dr.find_element_by_xpath("//input[@id='pass']")
        elem_password.clear()
        elem_password.send_keys(self.password)
        elem_password.send_keys(Keys.ENTER)
        time.sleep(5)
        print("Has iniciado sesión")
    
    def comment_facebook(self, message):
        dr = self.driver
        elem_comment = dr.find_element_by_xpath("//textarea[@name='xhpc_message']")
        elem_comment.click()
        elem_comment.send_keys(message)
        time.sleep(2)
        elem_okay = dr.find_element_by_xpath("//button[@class='_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft']")
        elem_okay.click()
        print("Post creado con exito")
       


# Credenciales de facebook
usuario_facebook = "sky17@gmx.es"
contrasena_facebook = "1234567890."

#   Apartado de comentarios
comentario_facebook = "Este es mi primer comentario mediante un bot con python"

obj_bot_facebook = FacebookBot(usuario_facebook, contrasena_facebook)
obj_bot_facebook.login_facebook()
obj_bot_facebook.comment_facebook(comentario_facebook)


