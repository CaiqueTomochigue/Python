print("Esses são os produtos disponíveis:")
print("-----------------------------------\n1-DualShock\n2-XboxJoystick\n3-NintendoJoystick\n-----------------------------------")
produto = int(input("Selecione qual o produto:"))

DualShock = 15
XboxJoystick = 20
NintendoJoystick = 5

if produto == 1:
    if DualShock > 0:
        print("Produto Disponível, temos em estoque: ", DualShock)
    else:
        print("Produto indisponível no momento.")
elif produto == 2:
    if XboxJoystick > 0:
        print("Produto Disponível, temos em estoque: ", XboxJoystick)
    else:
        print("Produto indisponível no momento.")
elif produto == 3:
    if NintendoJoystick > 0:
        print("Produto Disponível, temos em estoque: ", NintendoJoystick)
    else:
        print("Produto indisponível no momento.")
else:
    print("Código do Produto Inválido.")