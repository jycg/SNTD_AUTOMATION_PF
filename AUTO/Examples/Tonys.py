import json

# Tu JSON de ejemplo
json_data = {
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

# Convertir el JSON a una sola línea
json_one_line = json.dumps(json_data)

# Mostrar el resultado
print(json_one_line)
