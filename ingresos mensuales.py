#ingresos desde 0
#ingresar dinero semanalmente
#mostrar cuantos gastos tuvo en la semana
print("Resumen de ingresos y gastos semanales y mensuales")

def resumen_ingresos_gastos():
    ingresos = []
    gastos = []
    num_semanas = 4

    for semana in range(1, num_semanas + 1):
        
        while True:
            try:
                ingreso = float(input(f"Ingrese el INGRESO de la semana {semana}: "))
                if ingreso >= 0:
                    ingresos.append(ingreso)
                    break
                else:
                    print("El ingreso no puede ser negativo.")
            except ValueError:
                print("Debe ingresar un número válido.")

    
        while True:
            try:
                gasto = float(input(f"Ingrese el GASTO de la semana {semana}: "))
                if gasto >= 0:
                    gastos.append(gasto)
                    break
                else:
                    print("El gasto no puede ser negativo.")
            except ValueError:
                print("Debe ingresar un número válido.")

    total_ingresos = sum(ingresos)
    total_gastos = sum(gastos)

    print("\n--- Resumen semanal ---")
    for semana, (ingreso, gasto) in enumerate(zip(ingresos, gastos), start=1):
        balance = ingreso - gasto
        print(f"Semana {semana}: Ingreso = {ingreso:,.2f} | Gasto = {gasto:,.2f} | Balance = {balance:,.2f}")

    print("\n--- Totales del mes ---")
    print(f"Total ingresos del mes: {total_ingresos:,.2f}")
    print(f"Total gastos del mes: {total_gastos:,.2f}")
    print(f"Balance mensual: {total_ingresos - total_gastos:,.2f}")

resumen_ingresos_gastos()
