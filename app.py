# Importa las librerías necesarias
from flask import Flask, render_template, request
from driver.driver import DriverGeko

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/scrapear', methods=['POST'])
def scrapear_imagenes():
    # Obtiene la URL ingresada por el usuario desde el formulario desde el html
    url_a_scrapear = request.form.get('url')
    try:
        # usamos nuestro scraper 
        scraper = DriverGeko(url_a_scrapear)
        imagenes_scrapeadas = scraper.scrapearImg()
        urls_imagenes = [imagen.get_attribute('src') for imagen in imagenes_scrapeadas]
    except Exception as e:
        # Devuelve el mensaje de error si ocurre algún problema
        return str(e)
    finally:
        # Cierra el navegador después de usarlo
        scraper.driver.quit()
    #mandamos la url ala  pagina para renderirarlo
    return render_template('imagenes.html', urls_imagenes=urls_imagenes)


if __name__ == "__main__":
    app.run(debug=True)
