from faker import Faker
import random
import xlrd
import string
import json

from numpy.core.defchararray import upper

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

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(4))
json_data = {
{
    "CallIGRequest": {
        "CASO_RIESGOS": {
            "CENTRO": {
                "EMPRESA": "0014",
                "CENTRO": "0500"
            },
            "CODIGO_CASO": "24031420531206579860",
            "CODIGO_VERSION": "00",
            "CODIGO_SOLICITUD": "001"
        },
        "PROCESO_NEGOCIO": {
            "EMPRESA": "0014",
            "PROCESO_DE_NEGOCIO": "0500"
        },
        "CASE_INFO": {
            "caseInfo": {
                "MEX_IG_IN": {
                    "folioInteligente": "24031420531206579860TI001",
                    "solicitantes": {
                        "solicitante": [
                            {
                                "ordenIntervencion": "TI001",
                                "datosPersonales": {
                                    "tipoInterviniente": "TI",
                                    "bucPersonas": "00000000",
                                    "nombre": "MARIA MAYELA",
                                    "primerApellido": "HARO",
                                    "segundoApellido": "ALCALA",
                                    "sexo": "M",
                                    "fechaNacimiento": "1999-08-18",
                                    "nacionalidad": "052",
                                    "paisNacimiento": "052",
                                    "formaMigratoria": "",
                                    "rfc": "HAAM990818",
                                    "curp": "HAAM990818MGTRLY04",
                                    "estadoCivil": "S",
                                    "relacionConyugal": "",
                                    "dependientesEconomicos": "0",
                                    "nivelDeEstudios": "005",
                                    "tipoCliente": "",
                                    "actividadGenerica": "0000008V",
                                    "actividadEspecifica": "",
                                    "ocupacion": "08V",
                                    "tipoPersona": "02",
                                    "relacionConTitular": "",
                                    "correoElectronico": "MAYEHARO@GMAIL.COM"
                                },
                                "infoDomicilio": {
                                    "titularidadDomicilio": "04",
                                    "codigoPostalDomicilio": "00037138",
                                    "paisResidenciaDomicilio": "052",
                                    "antiguedadDomicilioActual": "1900",
                                    "antiguedadDomicilioAnterior": "",
                                    "tipoAsentamientoDomicilio": "09",
                                    "tipoDomicilio": "ALT",
                                    "tipoViaDomicilio": "",
                                    "nombreViaDomicilio": "JARDIN YUGOSLAVO",
                                    "asentamientoDomicilio": "GRAN JARDIN",
                                    "delegacionOMunicipioDomicilio": "00020",
                                    "estadoDomicilio": "GT",
                                    "localidadDomicilio": "",
                                    "ciudadDomicilio": "0000007",
                                    "numeroExteriorDomicilio": "112",
                                    "numeroInteriorDomicilio": "",
                                    "tipoTelefonoDomicilio1": "",
                                    "claseTelefonoDomicilio1": "",
                                    "claveLadaDomicilio1": "",
                                    "numeroTelefonicoDomicilio1": "",
                                    "tipoTelefonoDomicilio2": "",
                                    "claseTelefonoDomicilio2": "",
                                    "claveLadaDomicilio2": "",
                                    "numeroTelefonoDomicilio2": "4776702643",
                                    "fechaInicioDomicilioAnterior": ""
                                },
                                "datosEmpresa": {
                                    "nombreEmpresa": "BAUSA COLECTIVO",
                                    "puesto": "EM",
                                    "giroTipoEmpresa": "001",
                                    "antiguedadEmpleoActual": "0106",
                                    "tiempoInactivoEntreUltimos2Empleos": "",
                                    "fechaInicioActividades": "",
                                    "fechaFinEmpleoAnterior": "",
                                    "fechaInicioEmpleoAnterior": "",
                                    "fechaInicioEmpleoActual": "",
                                    "tipoContrato": "F",
                                    "nombreEmpresaAnterior": "",
                                    "antiguedadEmpleoAnterior": ""
                                },
                                "datosDomicilioLaboral": {
                                    "codigoPostalLaboral": "00037160",
                                    "tipoViaLaboral": "",
                                    "nombreViaLaboral": "AVENIDA PANORAMA",
                                    "tipoDomicilioLaboral": "",
                                    "tipoAsentamientoLaboral": "",
                                    "asentamientoLaboral": "PANORAMA",
                                    "delegacionMunicipioLaboral": "00020",
                                    "ciudadPoblacionLaboral": "0000007",
                                    "estadoLaboral": "GT",
                                    "paisLaboral": "052",
                                    "ladaLaboral": "",
                                    "telefonoLaboral": "",
                                    "numeroExteriorLaboral": "603",
                                    "numeroInteriorLaboral": "PISO 2 OFICINA 3",
                                    "extensionLaboral": ""
                                },
                                "datosIngresos": {
                                    "ingresoNetoFijoMensual": "00008000",
                                    "ingresoNetoVariableMensual": "00000000",
                                    "otrosIngresosFijosMensual": "00000000",
                                    "profesionistasIndependientesAnual": "",
                                    "ventasAnuales": ""
                                },
                                "datosGastosDeclarados": {
                                    "pagoMensualRenta": "00000000",
                                    "pagoMensualHipotecaConBanco": "",
                                    "pagoMensualHipotecaOtrosBancos": "",
                                    "pagoMensualEfectivoConBanco": "",
                                    "pagoMensualEfectivoOtrosBancos": ""
                                },
                                "datosSaldos": {
                                    "saldoTarjetasCreditoConBanco": "",
                                    "saldoTarjetasCreditoOtrosBancos": ""
                                },
                                "datosPatrimoniales": {
                                    "saldoInversionesConBanco": "00009589",
                                    "saldoInversionesOtroBanco": "",
                                    "saldoChequesConBanco": "",
                                    "saldoCuentaChequesOtroBanco": ""
                                },
                                "datosHogar": {
                                    "gastosMensualesHogar": "",
                                    "otrosGastosMensualesHogar": ""
                                },
                                "datosPatrimonio": {
                                    "totalPatrimonio": "00008513",
                                    "patrimonioLiquido": "00003982",
                                    "patrimonioMuebles": "",
                                    "patrimonioInmuebles": ""
                                },
                                "datosMotorFraudes": {
                                    "cajaNegra": "",
                                    "ipDeclarada": "",
                                    "tipoRequerido": ""
                                },
                                "depositosPromedio": "0",
                                "riesgosGrupo": "0",
                                "sumaLineasRevolventes": "",
                                "saldosPromedio": "",
                                "montoContrato": "",
                                "cuentacontdc": "",
                                "tdcbancaria": "",
                                "tdcdepartamental": "",
                                "digitostdc": "",
                                "ctohipovig": "",
                                "ctoauto": ""
                            },
                            {
                                "ordenIntervencion": "CO001",
                                "datosPersonales": {
                                    "tipoInterviniente": "CO",
                                    "bucPersonas": "00000000",
                                    "nombre": "MAURICIO",
                                    "primerApellido": "HARO",
                                    "segundoApellido": "NAVARRO",
                                    "sexo": "H",
                                    "fechaNacimiento": "1971-02-12",
                                    "nacionalidad": "052",
                                    "paisNacimiento": "052",
                                    "formaMigratoria": "",
                                    "rfc": "HANM71021216A",
                                    "curp": "HANM710212HGTRVR 05",
                                    "estadoCivil": "C",
                                    "relacionConyugal": "01",
                                    "dependientesEconomicos": "0",
                                    "nivelDeEstudios": "005",
                                    "tipoCliente": "",
                                    "actividadGenerica": "0000008V",
                                    "actividadEspecifica": "",
                                    "ocupacion": "08V",
                                    "tipoPersona": "02",
                                    "relacionConTitular": "002",
                                    "correoElectronico": "MHARO@FLEXI.COM.MX"
                                },
                                "infoDomicilio": {
                                    "titularidadDomicilio": "04",
                                    "codigoPostalDomicilio": "00037138",
                                    "paisResidenciaDomicilio": "052",
                                    "antiguedadDomicilioActual": "1900",
                                    "antiguedadDomicilioAnterior": "",
                                    "tipoAsentamientoDomicilio": "09",
                                    "tipoDomicilio": "ALT",
                                    "tipoViaDomicilio": "",
                                    "nombreViaDomicilio": "JARDIN YUGOSLAVO",
                                    "asentamientoDomicilio": "GRAN JARDIN",
                                    "delegacionOMunicipioDomicilio": "00020",
                                    "estadoDomicilio": "GT",
                                    "localidadDomicilio": "",
                                    "ciudadDomicilio": "0000007",
                                    "numeroExteriorDomicilio": "112",
                                    "numeroInteriorDomicilio": "",
                                    "tipoTelefonoDomicilio1": "",
                                    "claseTelefonoDomicilio1": "",
                                    "claveLadaDomicilio1": "",
                                    "numeroTelefonicoDomicilio1": "",
                                    "tipoTelefonoDomicilio2": "",
                                    "claseTelefonoDomicilio2": "",
                                    "claveLadaDomicilio2": "",
                                    "numeroTelefonoDomicilio2": "4776701077",
                                    "fechaInicioDomicilioAnterior": ""
                                },
                                "datosEmpresa": {
                                    "nombreEmpresa": "GRUPO FLEXI",
                                    "puesto": "EM",
                                    "giroTipoEmpresa": "001",
                                    "antiguedadEmpleoActual": "2900",
                                    "tiempoInactivoEntreUltimos2Empleos": "",
                                    "fechaInicioActividades": "",
                                    "fechaFinEmpleoAnterior": "",
                                    "fechaInicioEmpleoAnterior": "",
                                    "fechaInicioEmpleoActual": "",
                                    "tipoContrato": "F",
                                    "nombreEmpresaAnterior": "",
                                    "antiguedadEmpleoAnterior": ""
                                },
                                "datosDomicilioLaboral": {
                                    "codigoPostalLaboral": "00037510",
                                    "tipoViaLaboral": "",
                                    "nombreViaLaboral": "FCO VILLA",
                                    "tipoDomicilioLaboral": "",
                                    "tipoAsentamientoLaboral": "",
                                    "asentamientoLaboral": "ORIENTAL",
                                    "delegacionMunicipioLaboral": "00020",
                                    "ciudadPoblacionLaboral": "0000007",
                                    "estadoLaboral": "GT",
                                    "paisLaboral": "052",
                                    "ladaLaboral": "",
                                    "telefonoLaboral": "",
                                    "numeroExteriorLaboral": "201",
                                    "numeroInteriorLaboral": "1",
                                    "extensionLaboral": ""
                                },
                                "datosIngresos": {
                                    "ingresoNetoFijoMensual": "00000000",
                                    "ingresoNetoVariableMensual": "00258000",
                                    "otrosIngresosFijosMensual": "00000000",
                                    "profesionistasIndependientesAnual": "",
                                    "ventasAnuales": ""
                                },
                                "datosGastosDeclarados": {
                                    "pagoMensualRenta": "00000000",
                                    "pagoMensualHipotecaConBanco": "",
                                    "pagoMensualHipotecaOtrosBancos": "",
                                    "pagoMensualEfectivoConBanco": "",
                                    "pagoMensualEfectivoOtrosBancos": ""
                                },
                                "datosSaldos": {
                                    "saldoTarjetasCreditoConBanco": "",
                                    "saldoTarjetasCreditoOtrosBancos": ""
                                },
                                "datosPatrimoniales": {
                                    "saldoInversionesConBanco": "00006953",
                                    "saldoInversionesOtroBanco": "",
                                    "saldoChequesConBanco": "",
                                    "saldoCuentaChequesOtroBanco": ""
                                },
                                "datosHogar": {
                                    "gastosMensualesHogar": "",
                                    "otrosGastosMensualesHogar": ""
                                },
                                "datosPatrimonio": {
                                    "totalPatrimonio": "00285676",
                                    "patrimonioLiquido": "00079455",
                                    "patrimonioMuebles": "",
                                    "patrimonioInmuebles": ""
                                },
                                "datosMotorFraudes": {
                                    "cajaNegra": "",
                                    "ipDeclarada": "",
                                    "tipoRequerido": ""
                                },
                                "depositosPromedio": "0",
                                "riesgosGrupo": "0",
                                "sumaLineasRevolventes": "",
                                "saldosPromedio": "",
                                "montoContrato": "",
                                "cuentacontdc": "",
                                "tdcbancaria": "",
                                "tdcdepartamental": "",
                                "digitostdc": "",
                                "ctohipovig": "",
                                "ctoauto": ""
                            }
                        ]
                    },
                    "solicitud": {
                        "claseSolicitud": "300",
                        "condicionesProducto": "",
                        "tipodeProducto": "",
                        "canalAdquisicion": "014",
                        "promocionConvenioCampania": "0000008V",
                        "importeSolicitado": "321187",
                        "valorBienAdquirir": "380900",
                        "plazoSolicitado": "72",
                        "tipoTasa": "",
                        "enganche": "76180",
                        "tipoGarantia": "",
                        "segmento": "",
                        "tasaReferencia": "",
                        "tasa": "1549",
                        "plazo": "",
                        "antiguedadBien": "1",
                        "plazoRemanenteBienSustituir": "000",
                        "sdoTransferirSustitucion": "0000",
                        "cuotaMensualSustituir": "0",
                        "tipoUsoBienAdquirir": "001",
                        "parentescoVendedor": "",
                        "comprobanteIngresos": "",
                        "infoNavit": {
                            "tiempoAportacionInfonavit": "",
                            "fondoAcumuladoVivinfonavit": "",
                            "aportacionesMensualesInfonavit": ""
                        },
                        "llamadaRDT": "3",
                        "reevaluacion": "",
                        "listadoProducto": {
                            "producto": "12",
                            "subproducto": "0641"
                        },
                        "datosUniversidad": {
                            "codigoUniversidad": "",
                            "codigoCarrera": "",
                            "anioEnCurso": "0",
                            "tipoBeca": "",
                            "porcentajeBeca": "",
                            "importeColegiatura": "",
                            "postGrado": ""
                        },
                        "numeroEmpleados": "",
                        "atribuciones": "",
                        "decisionManual": ""
                    },
                    "camposRaiting": {
                        "interesesPagdos": "142053"
                    }
                }
            }
        }
    }
}
}

json_online =json.dumps(json_data)

print(json_online)
for _ in range(1):
    # print(random.randint(0, 9))
    # print(  # ''.join(random.choice(letters.upper()) for i in range(1)),
    #     random.randint(1, 9),
    #     ''.join(random.choice(letters.upper()) for i in range(1)),
    #     random.randint(1, 9),
    #     sep='')

    # Sección correcta para data dumi en loadrunner
    print(''.join(random.choice(letters.upper())),
          random.randint(1, 9),
          ''.join(random.choice(letters.upper())),
          ',',
          'GAHJ950802,',
          'JULIO,',
          'DE JESUS,',
          'GARCIA,',
          'HERNANDEZ,',
          'GAHJ950802HJCRRL 00,',
          '331-698-5551,',
          '3316985551',
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
