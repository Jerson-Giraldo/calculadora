from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    resultado = None

    # Ingresar números
    if request.method == "POST":
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        if num1 == "" or num2 == "":
            resultado = "Por favor ingresa ambos números."
        else:
            num1 = int(num1)
            num2 = int(num2)
            operacion = request.POST.get("operacion")

            # Operaciones
            if operacion == "suma":
                resultado = num1 + num2
            elif operacion == "resta":
                resultado = num1 - num2
            elif operacion == "multiplicacion":
                resultado = num1 * num2
            elif operacion == "division":
                resultado = num1 / num2 if num2 != 0 else "No se puede dividir entre cero."

                # Guardar el resultado en la sesión y redirigir
        request.session["resultado"] = resultado
        return redirect("home")  # <-- el nombre de tu url

    # Si existe en sesión, mostrarlo y borrarlo
    resultado = request.session.pop("resultado", None)
    return render(request, "home.html", {"resultado": resultado})
