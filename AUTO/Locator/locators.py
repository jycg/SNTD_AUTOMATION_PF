class Locators:
    # Login page objects
    usuario_autogestion = "txtUserCode"  # ID
    pass_autogestion = "txtPassword"  # ID
    login_autogestion = "btnLogin"  # ID

    # Search page object
    usuario_busqueda = "aUserName"  # ID
    icono_salir = "Cerrar sesión"  # LINK_TEXT
    nva_cot = "btnNewQuote"  # ID

    # Sección "PRODUCTO"
    agencia_click = "//span[@id='select2-cboAgencies-container']"
    agencia_enter = "//body/span[1]/span[1]/span[1]/input[1]"
    producto_arrendamiento = "TpPrdFinAP"  # ID
    producto_tipo_n = "//body/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/input[1]"  # XPATH
    producto_tipo_n_BYD = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]"
    producto_tipo_n_OM = "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]"
    producto_tipo_s = "//body/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]/input[1]"  # XPATH
    producto_tipo_s_OM = "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/input[1]"
    producto_tipo_m = "//body/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/input[1]"  # XPATH
    producto_tipo_m_OM = "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/input[1]"  # XPATH
    producto_uso_p = "//body/div[1]/div[2]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/input[1]"  # XPATH
    producto_uso_p_BYD = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/input[1]"
    producto_uso_cp = "opUsePrivate"  # ID
    producto_uso_c = "opUseComercial"  # ID
    producto_p_f = "//body/div[1]/div[2]/div[1]/div[1]/div[3]/div[4]/div[1]/div[1]/input[1]"  # XPATH
    producto_p_f_BYD = "//body/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/input[1]"
    producto_p_f_OM = "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/input[1]"
    producto_p_fae = "//body/div[1]/div[2]/div[1]/div[1]/div[3]/div[4]/div[1]/div[2]/input[1]"  # XPATH
    producto_p_fae_BYD = "//body/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/input[1]"
    producto_p_fae_OM = "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/input[1]"
    producto_marca_click = "select2-cboBrandID-container"  # ID
    producto_marca_enter = "//body/span[1]/span[1]/span[1]/input[1]"  # XPATH
    producto_modelo_click = "select2-cboProduct-container"  # ID
    producto_modelo_enter = "//body/span[1]/span[1]/span[1]/input[1]"  # XPATH
    producto_version_click = "select2-cboVersion-container"  # ID
    producto_version_enter = "//body/span[1]/span[1]/span[1]/input[1]"  # XPATH
    producto_ano_click = "select2-cboYear-container"  # ID
    producto_anio_enter = "//body/span[1]/span[1]/span[1]/input[1]"  # XPATH
    producto_section_divListPrice = "divListPrice"  # ID
    producto_monto_vehiculo = "input-as-label-operator"  # ID

    # Sección "PLAN DE FINANCIAMIENTO
    plan_plan = "cboFinantialPlan"  # ID
    plan_enganche_porcentaje = "porcentaje-elemento"  # ID
    plan_accesorios = "cboAccesoriesOptions"  # ID
    plan_desc_accesorios = 'txtAccesoriesDescription'  # ID
    plan_monto_accesorios = 'txtAccesoriesAmount'  # ID
    plan_g_ext = "cboWarrantyOptions"
    plan_g_ext_monto = "txtExtendedwarranty"
    plan_g_ext_forma_pago = "cboPaymentTypeWarranty"
    plan_type_accesories = "//select[@id='cboPaymentTypeAccessories']"
    plan_cuotas_show = "btnCalcCuotas"  # ID
    plan_cuotas_select = "divTermContent_24"  # ID
    plan_garantia_extendida = "chkExtendedWarranty"
    plan_seguro_robo = "chkAutoPartsTheftInsurance"
    plan_seguro_gap = "chkInsuranceGap"
    plan_coberturas = "divMessageBody"
    alert_label = "//h3[contains(text(),'Atención')]"
    plan_aceptar_click = "//button[@id='btnAccept']"

    # Sección "SEGURO DE AUTO"
    insurance_no = "optionsRadiosLabel2No"  # ID
    insurance_si = "optionsRadios2Si"  # ID
    insurance_manual = "optionsRadios2Manual"
    insurance_prima_manual = "optionsRadiosLabel2Manual"  # ID
    insurance_msj_aceptar_click = "//body/div[@id='msjNoSeguroAuto']/div[1]/div[1]/div[3]/button[1]"  # XPATH
    insurance_formapago = "cboPayMethod"  # ID
    insurance_tipo = "cboInsuranceDuration"  # ID
    insurance_cp = "txtZipCode"  # ID
    insurance_cobertura = "cboCoberture"  # ID
    insurance_birthdate = "txdBirthDate"  # ID
    insurance_male = "//body/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[5]/div[1]/div[6]/div[2]/div[1]/label[1]/span[1]"  # XPATH
    insurance_female = "//body/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[5]/div[1]/div[6]/div[2]/div[1]/label[2]/span[1]"  # XPATH
    insurance_recibo1 = "txtManualFirstReceipt"  # ID
    insurance_recibo2 = "txtManualConsequentReceipt"  # ID
    insurance_subsecuente = "txtManualSecondConsequentReceipt"  # ID
    insurance_btn_click = "btnInsuranceQuote"  # ID
    insurance_div = "divInsOptns"  # ID
    insurance_insurance = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[6]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]"  # XPATH
    insurance_divautocompara = "divCompareAuto"  # ID
    insurance_autocompara_si = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[5]/div[1]/div[6]/div[3]/div[1]/label[1]/span[1]"  # XPATH
    insurance_autocompara_no = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[5]/div[1]/div[6]/div[3]/div[1]/label[2]/span[1]"  # XPATH
    insurance_aseguradoras = "drpInsurers"  # ID
    insurance_UDI = "cboUDI"

    # Sección "DETALLE DEL FINANCIAMIENTO"
    txtPay12 = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]/span[1]"
    txtPay24 = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[2]/div[2]/div[1]/span[1]"
    txtPay36 = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[2]/div[3]/div[1]/span[1]"
    txtPay48 = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[2]/div[4]/div[1]/span[1]"
    txtPay60 = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[2]/div[5]/div[1]/span[1]"
    txtPay72 = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[2]/div[6]/div[1]/span[1]"
    cat = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[8]/div[2]/div[2]/div[1]/label[1]/b[2]"
    amortizationdetail_lblCar = "lblCar"  # ID
    amortizationdetail_lblPriceList = "lblPriceList"
    amortizationdetail_tdaccessories = "tdaccessories"
    amortizationdetail_tdaccessoriesamount = "tdaccessoriesamount"
    amortizationdetail_VFG = "VFG"
    amortizationdetail_balloonTCMInfo = "balloonTCMInfo"
    amortizationdetail_tdInterestRateTCM = "tdInterestRateTCM"
    amortizationdetail_tdTermTCM = "tdTermTCM"
    tblAmortization_information = "tblAmortization"
    tblAmortizationCycle2_TCM = "tblAmortizationCycle2"

    # Sección "DATOS DEL SOLICITANTE"
    information_fname = "txtfName"  # ID
    information_sname = "txtsName"  # ID
    information_flastname = "txtflastName"  # ID
    information_slastname = "txtsLastName"  # ID
    information_lada = "txtTelephoneLada"  # ID
    information_phone = "txtTelephone"  # ID
    information_cellphone = "txtCelphone"  # ID
    information_cellcompany_click = "cboPhoneCompany"  # ID
    information_email = "txtMail"  # ID
    quote_check_aviso_click_1 = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[10]/div[11]/label[2]/span[1]/span[1]"  # XPATH
    quote_check_aviso_click_2 = "/html[1]/body[1]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/label[1]/span[1]/span[1]"
    quote_check_aviso_msj_click = "//button[@id='btnNoticeOfPrivacyOk']"  # XPAT
    quote_imprimir_click = "btnImpCot"  # ID
    quote_solicita_credito = "btnStartCreditform"  # ID
    quote_confirm_data_step = 'confirm-data-step'  # ID
    quote_btnConfirmData = 'btnConfirmData'  # ID
    quote_divCodigoVerTemp = '/html[1]/body[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/label[1]'  # XPATH
    quote_txtConfirmCode = 'txtConfirmCode'  # ID
    quote_btnGotoCreditform = 'btnGotoCreditform'  # ID
