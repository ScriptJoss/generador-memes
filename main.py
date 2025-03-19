# Importar
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)


# Resultados del formulario
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # obtener la imagen seleccionada
        selected_image = request.form.get("image-selector")

        # Asignación #2. Hecho
        textTop = request.form.get("textTop")
        textBottom = request.form.get("textBottom")
        # Assignment #3. Receiving the text's positioning

        textTopY = request.form.get("textTopY")
        textBottomY = request.form.get("textBottomY")

        selectedColor = request.form.get("color-selector")

        # Asignación #3. Hecho ✅


        return render_template(
            "index.html",
            # Visualización de la imagen seleccionada
            selected_image=selected_image,
            # Asignación #2. Hecho
            textTop=textTop,
            textBottom=textBottom,
            #  Asignación #3. Visualización del color
            selectedColor=selectedColor,
            # Asignación #3. Visualización de la posición del texto
            textTopY=textTopY,
            textBottomY=textBottomY,
        )
    else:
        # Mostrar la primera imagen por defecto
        return render_template("index.html", selected_image="logo.svg")


@app.route("/static/img/<path:path>")
def serve_images(path):
    return send_from_directory("static/img", path)


app.run(debug=True)
