from faker import Faker
import random
import xlrd
import string

location_quote = "C:/Automation_Performance_Sast/SNTD_PCR_PM_SP8.xls"
var_excel_quote = xlrd.open_workbook(location_quote)
template_quote = var_excel_quote.sheet_by_index(0)

fake = Faker()
# fake.address()
# print(fake.last_name())

# Librería para generar data Fake
# Condición para generar data y consumirse en script de PCR para PM
# https://faker.readthedocs.io/en/stable/
letters = string.ascii_lowercase
# print ( ''.join(random.choice(letters) for i in range(1)) )

for _ in range(180):
    # print(random.randint(0, 9))
    # print(  # ''.join(random.choice(letters.upper()) for i in range(1)),
    #     random.randint(1, 9),
    #     ''.join(random.choice(letters.upper()) for i in range(1)),
    #     random.randint(1, 9),
    #     sep='')
    print(''.join(random.choice(letters)),
          random.randint(1, 9),
          ''.join(random.choice(letters)),
          ',',
          'GAVM950802,',
          'MARTHA,',
          'ELIZABETH,',
          'GARCIA,',
          'VILLA,',
          'GAVM950802HJCRLR 32,',
          '331-698-2655,',
          '3316982655',
          sep='')
    # for f_comm_name in range(0, 1):
    #     for f_rfcPM in range(1, 2):
    #         for f_CELL_OS in range(2, 3):
    #             for f_CELL_OS_v2 in range(3, 4):
    #                 for f_rfcPF in range(4, 5):
    #                     rfc_text = template_quote.cell_value(_, f_rfcPM)
    #                     size = len(rfc_text)
    #                     replacement = str(random.randint(0, 9))
    #                     rfc_text = rfc_text.replace(rfc_text[size - 1:], replacement)
    #                     # print(rfc_text)
    #                     rfc_text2 = template_quote.cell_value(_, f_rfcPM)
    #                     size2 = len(rfc_text2)
    #                     replacement = str(random.randint(000, 999))
    #                     rfc_text2 = rfc_text2.replace(rfc_text2[size2 - 3:], replacement)
    #                     # print(rfc_text2)
    #                     rfc_text3 = template_quote.cell_value(_, f_rfcPF)
    #                     size3 = len(rfc_text3)
    #                     replacement = str(random.randint(0, 9))
    #                     rfc_text3 = rfc_text3.replace(rfc_text3[size3 - 1:], replacement)
    #                     # print(rfc_text3)
    #                     rfc_text4 = template_quote.cell_value(_, f_rfcPF)
    #                     size4 = len(rfc_text4)
    #                     replacement = str(random.randint(00, 99))
    #                     rfc_text4 = rfc_text4.replace(rfc_text4[size4 - 2:], replacement)
    #                     # print(rfc_text4)
    #                     print(template_quote.cell_value(_, f_comm_name), ',',  # ComercialName
    #                           template_quote.cell_value(_, f_comm_name), ',',
    #                           # LegalName - 'TEKPROVIDER SA DE CV', ',',
    #                           '3316986302', ',',  # Celular
    #                           fake.first_name(), ',',  # GivenName
    #                           fake.first_name(), ',',  # MiddleName
    #                           fake.last_name(), ',',  # LastName
    #                           fake.last_name(), ',',  # SecondLastName
    #                           template_quote.cell_value(_, f_rfcPM), ',',  # PersonaMoralRFC
    #                           '2222875638', ',',  # telephone_PM
    #                           '222-2875638', ',',  # telephone_PM_V2
    #                           rfc_text, ',',  # PersonaMoralRFC_v2
    #                           fake.first_name(), ',',  # firstName_p1
    #                           fake.first_name(), ',',  # middleName_p1
    #                           fake.last_name(), ',',  # lastName_p1
    #                           fake.last_name(), ',',  # secondLastName_p1
    #                           rfc_text2, ',',  # Inter_p1_RFC
    #                           fake.first_name(), ',',  # firstName_p2
    #                           fake.first_name(), ',',  # middleName_p2
    #                           fake.last_name(), ',',  # lastName_p2
    #                           fake.last_name(), ',',  # secondLastName_p2
    #                           rfc_text3, ',',  # Inter_p2_RFC
    #                           int(template_quote.cell_value(_, f_CELL_OS)),
    #                           int(template_quote.cell_value(_, f_CELL_OS_v2)), random.randint(0000, 9999), ',',
    #                           # telephone_OS_CELL
    #                           '3322647683', ',',  # telephone_OS_OFFICE
    #                           '332-2647683', ',',  # telephone_OS_OFFICE_v2
    #                           int(template_quote.cell_value(_, f_CELL_OS)), '-',
    #                           int(template_quote.cell_value(_, f_CELL_OS_v2)), random.randint(0000, 9999),
    #                           # telephone_OS_CELL_v2
    #                           sep='')
