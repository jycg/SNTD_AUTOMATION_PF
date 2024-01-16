import xlrd
# import random
#
# rfchmn = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(random.choice(rfchmn))
# rfchml1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(random.choice(rfchml1))
# rfchml2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(random.choice(rfchml2))


class Database:
    # for a in range(3):
    #     #ANGELA,MARIA,GARCIA,VILLA,GAVA950802,005,GAVA950802HJCRLN 02
    #     print("ANGELA",random.choice(rfchml1),random.choice(rfchmn),random.choice(rfchml2))
    # El primer valor indica la fila (0) y el segundo valor indica la columna (1)
    # print(template.cell_value(0, 0))
    # print(template.cell_value(0, 1))
    # location_1 = ("C:/Automation_Performance_Sast/Database_quote.xls")
    # location_2 = ("C:/Automation_Performance_Sast/Database_ejemplo.xls")
    # var_excel_1 = xlrd.open_workbook(location_1)
    # var_excel_2 = xlrd.open_workbook(location_2)
    # template_1 = var_excel_1.sheet_by_index(0)
    # template_2 = var_excel_2.sheet_by_index(0)

    # print(template_cont.cell_value(0, 0))

    # NOTA: Las celdas de color azul no debe eliminarse debido a que es la base. Para los ciclos en PyCharm, se sugiere
    # iniciarlizar la variable con el valor 2 para iniciar con el registro de operaciones

    # data_input = int(input("Ingresa la cantidad de iteraciones: "))
    # for cont_input in range(1, data_input):
    #     print(cont_input)
    #     for for_plazo in range(18, 19):
    #         print("Plazo: ", template_1.cell_value(cont_input, for_plazo))
    #         example_plazo = template_1.cell_value(cont_input, for_plazo)
    #         print(example_plazo)

     # data_input = int(input("Ingresa la cantidad de iteraciones: "))
     # for cont_input in range(1, data_input):
     #    print(cont_input)
     #    for for_plazo in range(18, 19):
     #         print("Plazo: ", template_1.cell_value(cont_input, for_plazo))
     #     for for_ejemplo in range(0, 1):
     #         print("Segundo excel: ", template_2.cell_value(cont_input, for_ejemplo))

    # ------------------------------ Data para el CANAL ------------------------------
    def chanelsntd(self, chanel):
        default = "No existe el canal"
        return getattr(self, 'case_' + str(chanel), lambda: default)()

    def case_1(self):
        return "AGENCIA"

    def case_2(self):
        return "SUCURSAL"

    def case_3(self):
        return "OPEN MARKET"

    # ------------------------------ Data para el USUARIO ------------------------------
    def usersntd(self, users):
        defaultuser = "No existe el usuario"
        return getattr(self, 'caseuser_' + str(users), lambda: defaultuser)()

    def caseuser_1(self):
        return "TBBT01"

    def caseuser_2(self):
        return "TBBT02"

    def caseuser_3(self):
        return "n807433"

    def caseuser_4(self):
        return "n807322"

    # ------------------------------ Data para el PRODUCTO ------------------------------
    def productsntd(self, product):
        defaultproduct = "No existe el producto"
        return getattr(self, 'caseproduct_' + str(product), lambda: defaultproduct)()

    def caseproduct_1(self):
        return "CREDITO"

    def caseproduct_2(self):
        return "ARRENDAMIENTO"

    # ------------------------------ Data para el TIPO PRODUCTO ------------------------------
    def typeproductsntd(self, typeproduct):
        defaulttypeproduct = "No existe el tipo de producto"
        return getattr(self, 'casetypeproduct_' + str(typeproduct), lambda: defaulttypeproduct)()

    def casetypeproduct_1(self):
        return "NUEVO"

    def casetypeproduct_2(self):
        return "SEMINUEVO"

    def casetypeproduct_3(self):
        return "MOTO"

    # ------------------------------ Data para el USO ------------------------------
    def typeusentd(self, typeuse):
        defaulttypeuse = "No existe el tipo de uso"
        return getattr(self, 'casetypeuse_' + str(typeuse), lambda: defaulttypeuse)()

    def casetypeuse_1(self):
        return "PARTICULAR"

    def casetypeuse_2(self):
        return "CHOFER"

    def casetypeuse_3(self):
        return "COMERCIAL"

    # ------------------------------ Data para el TIPO PERSONA ------------------------------
    def typepeoplesntd(self, people):
        defaulttypepeople = "No existe el tipo de persona"
        return getattr(self, 'casetypepeople_' + str(people), lambda: defaulttypepeople)()

    def casetypepeople_1(self):
        return "FISICA"

    def casetypepeople_2(self):
        return "FISICA AE"

    # ------------------------------ Data para el SEGURO ------------------------------
    def insurancesntd(self, insurance):
        defaultinsurance = "No existe la opción de seguro"
        return getattr(self, 'caseinsurance_' + str(insurance), lambda: defaultinsurance)()

    def caseinsurance_1(self):
        return "NO"

    def caseinsurance_2(self):
        return "SI"

    def caseinsurance_3(self):
        return "PRIMA MANUAL"

    # ------------------------------ Data para el AMBIENTE ------------------------------

    def environmentnstd(self, environment):
        defaultenvironment = "No existe el ambiente"
        return getattr(self, 'caseenvironment_' + str(environment), lambda: defaultenvironment)()

    def caseenvironment_1(self):
        return "TEST"

    def caseenvironment_2(self):
        return "UAT1"

    def caseenvironment_3(self):
        return "UAT2"

    def caseenvironment_4(self):
        return "PRE"

    def caseenvironment_5(self):
        return "DEV"

    #Vehicle
    Vehicle_kia = "KIA"

switch_chanel = Database()
# input_chanel = int(input("Selecciona el CANAL: [1 - AGENCIA, 2 - SUCURSAL, 3 - OPEN MARKET]: "))
# input_user = int(input("Selecciona el USUARIO: [1 - TBBT01, 2 - TBBT02, 3 - n807433, 4 - n807322]: "))
# for uno in range(1, 2):
#     print(switch_chanel.chanelsntd(input_chanel))
# for dos in range(1,2):
#     print(switch_chanel.usersntd((input_user)))
