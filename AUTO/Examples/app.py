from flask import Flask
from flask import request
from selenium import webdriver
from selenium.webdriver.common.by import By

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
    <body>
    <h2>Automatizar Acción</h2>
    <form action="/automatizar" method="post">
        <input type="submit" value="Automatizar">
    </form>
    </body>
    </html>
    """

@app.route('/automatizar', methods=['POST'])
def automatizar():
    # Coloca aquí tu código de automatización con Selenium
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    boton = driver.find_element(By.CSS_SELECTOR, "selector_del_boton")
    boton.click()
    driver.quit()
    return "Acción automatizada exitosamente."

if __name__ == '__main__':
    app.run(debug=True)