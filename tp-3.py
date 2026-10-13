
def procesar_venta_medicamento(tipo_cliente, tiene_obra_social, tipo_medicamento, dia_semana):
    # ERROR 1: Alta Complejidad Ciclomatica (if/else anidados)
    if tipo_cliente == "jubilado":
        if tiene_obra_social:
            if tipo_medicamento == "cronico":
                if dia_semana == "miercoles":
                    # ERROR 2: Duplicación de código
                    print("Aplicando descuento PAMI")
                    precio = 1000 * 0.20
                    return precio
                else:
                    print("Aplicando descuento PAMI")
                    precio = 1000 * 0.40
                    return precio
    elif tipo_cliente == "particular":
        if tiene_obra_social:
            # ERROR 2: Duplicacion de codigo
            print("Aplicando descuento Obra Social")
            precio = 1000 * 0.60
            return precio
        else:
            return 1000
    return 1000