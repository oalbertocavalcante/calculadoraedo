import sympy as sp

ordem = int(input("Digite a ordem da EDO (1 ou 2): "))

if ordem == 1:
    print("\nA * dy/dx + B * y = C\n")
    A_input = input("Digite o coeficiente A (de dy/dx): ")
    if A_input == "euler":
        E = sp.sympify(input("Digite o exponencial de euler: "))
        G = input("Digite a operação que desej2a realizar depois do euler(+, -, *, /): ")
        F = sp.sympify(input("Digite o resto do coeficiente A (de d^2y/d^2x): "))
        if G == "+":
            A = sp.exp(E) + F
        if G == "-":
            A = sp.exp(E) - F
        if G == "*":
            A = sp.exp(E) * F
        if G == "/":
            A = sp.exp(E) / F
    else:
        A = sp.sympify(A_input)
    B_input = input("Digite o coeficiente B (de y): ")
    if B_input == "euler":
        E = sp.sympify(input("Digite o exponencial de euler: "))
        G = input("Digite a operação que deseja realizar depois do euler(+, -, *, /): ")
        F = sp.sympify(input("Digite o resto do coeficiente B (de dy/dx): "))
        if G == "+":
            B = sp.exp(E) + F
        if G == "-":
            B = sp.exp(E) - F
        if G == "*":
            B = sp.exp(E) * F
        if G == "/":
            B = sp.exp(E) / F
    else:
        B = sp.sympify(B_input)
    C_input = input("Digite o coeficiente C (de F(x)): ")
    if C_input == "euler":
        E = sp.sympify(input("Digite o exponencial de euler: "))
        G = input("Digite a operação que deseja realizar depois do euler(+, -, *, /): ")
        F = sp.sympify(input("Digite o resto do coeficiente C (de y): "))
        if G == "+":
            C = sp.exp(E) + F
        if G == "-":
            C = sp.exp(E) - F
        if G == "*":
            C = sp.exp(E) * F
        if G == "/":
            C = sp.exp(E) / F
    else:
        C = sp.sympify(C_input)


    x = sp.Symbol('x')
    y = sp.Function('y')(x)

    edo = sp.Eq(A * y.diff(x) + B * y, C)

    solucao_geral = sp.dsolve(edo)

    lhs = solucao_geral.lhs
    rhs = solucao_geral.rhs

    rhs_simplificado = sp.simplify(rhs)

elif ordem == 2:
    print("\nA * d^2y/d^2x + B * dy/dx + C * y = D\n")
    A_input = input("Digite o coeficiente A (de d^2y/d^2x): ")
    if A_input == "euler":
        E = sp.sympify(input("Digite o exponencial de euler: "))
        G = input("Digite a operação que deseja realizar depois do euler(+, -, *, /): ")
        F = sp.sympify(input("Digite o resto do coeficiente A (de d^2y/d^2x): "))
        if G == "+":
            A = sp.exp(E) + F
        if G == "-":
            A = sp.exp(E) - F
        if G == "*":
            A = sp.exp(E) * F
        if G == "/":
            A = sp.exp(E) / F
    else:
        A = sp.sympify(A_input)
    B_input = input("Digite o coeficiente B (de dy/dx): ")
    if B_input == "euler":
        E = sp.sympify(input("Digite o exponencial de euler: "))
        G = input("Digite a operação que deseja realizar depois do euler(+, -, *, /): ")
        F = sp.sympify(input("Digite o resto do coeficiente B (de dy/dx): "))
        if G == "+":
            B = sp.exp(E) + F
        if G == "-":
            B = sp.exp(E) - F
        if G == "*":
            B = sp.exp(E) * F
        if G == "/":
            B = sp.exp(E) / F
    else:
        B = sp.sympify(B_input)
    C_input = input("Digite o coeficiente C (de y): ")
    if C_input == "euler":
        E = sp.sympify(input("Digite o exponencial de euler: "))
        G = input("Digite a operação que deseja realizar depois do euler(+, -, *, /): ")
        F = sp.sympify(input("Digite o resto do coeficiente C (de y): "))
        if G == "+":
            C = sp.exp(E) + F
        if G == "-":
            C = sp.exp(E) - F
        if G == "*":
            C = sp.exp(E) * F
        if G == "/":
            C = sp.exp(E) / F
    else:
        C = sp.sympify(C_input)
    D_input = input("Digite o coeficiente D (de F(x)): ")
    if D_input == "euler":
        E = sp.sympify(input("Digite o exponencial de euler: "))
        G = input("Digite a operação que deseja realizar depois do euler(+, -, *, /): ")
        F = sp.sympify(input("Digite o resto do coeficiente D (de F(x)): "))
        if G == "+":
            D = sp.exp(E) + F
        if G == "-":
            D = sp.exp(E) - F
        if G == "*":
            D = sp.exp(E) * F
        if G == "/":
            D = sp.exp(E) / F
    else:
        D = sp.sympify(D_input)

    x = sp.Symbol('x')
    y = sp.Function('y')(x)

    edo = sp.Eq(A * y.diff(x, x) + B * y.diff(x) + C * y, D)

    solucao_geral = sp.dsolve(edo)

    lhs = solucao_geral.lhs
    rhs = solucao_geral.rhs

    rhs_simplificado = sp.simplify(rhs)

print('\nSolução geral:\n')
sp.pprint(solucao_geral)

print('\nSolução simplificada:\n')
sp.pprint(rhs_simplificado)