from behave import given, when, then, step
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", False) 
chrome_options.headless = True
driver = webdriver.Chrome(options = chrome_options)


@given('go to UH Form')
def go_to_login_form(context):
    driver.get('https://form.care4all.in/students/80312666')

@then('the title should be {text}')
def verify_title(context, text):
    title = driver.title
    try:
        assert "Urban Health with Perfect Smiles Clinic" == title
    except AssertionError as e:
        assert context, 'fail'

@when('fill the form')
def enter_credentials(context):
    
    #Name
    driver.find_element(By.NAME,'name').send_keys('Nirnay')
    
    #Gender
    radio1 = driver.find_element(By.XPATH,'/html/body/main/form/section[1]/div/div[2]/div[1]/label')
    ActionChains(driver).move_to_element(radio1).click()
    selected1 = radio1.is_selected()
    if selected1 == False:
        radio1.click()
    
    #Age
    radio2 = driver.find_element(By.XPATH,'//*[@id="survey-form"]/section[1]/div/div[3]/div[3]/label')
    ActionChains(driver).move_to_element(radio2).click()
    selected2 = radio2.is_selected()
    if selected2 == False:
        radio2.click()

    #Class
    Select(driver.find_element(By.CSS_SELECTOR, '.survey__panel__personaldetails > div:nth-child(4) > select:nth-child(2)')).select_by_value('Senior')
    
    #Section
    Select(driver.find_element(By.CSS_SELECTOR, '.survey__panel__personaldetails > div:nth-child(5) > select:nth-child(2)')).select_by_value('A')
    

@then('I click next')
def click_login(context):
    driver.find_element(By.XPATH,'/html/body/main/form/div[2]/button[2]').click()
    sh = driver.find_element(By.XPATH,'/html/body/main/form/section[2]/h2')
    try:
        assert "Parents Detail" == sh
    except AssertionError as e:
        assert context, 'fail'

@then('fill the form2 & click next')
def click_login(context):
    driver.find_element(By.XPATH,'//*[@id="father_name"]').send_keys('FATHER')
    driver.find_element(By.XPATH,'//*[@id="mother_name"]').send_keys('MOTHER')
    driver.find_element(By.XPATH,'//*[@id="mobile"]').send_keys('8828480007')
    driver.find_element(By.XPATH,'//*[@id="email"]').send_keys('nirnay.sheshware@urbanotechnologies.com')
    driver.find_element(By.XPATH,'//*[@id="address"]').send_keys('ADDRESS')
    driver.find_element(By.XPATH,'/html/body/main/form/div[2]/button[2]').click()
    
@then('fill the form3 & click next')
def click_login(context):
    #ToothDecay
    driver.find_element(By.XPATH,'//*[@id="upper_front_teeth_past"]').click()
    driver.find_element(By.XPATH,'//*[@id="lower_front_teeth_past"]').click()

    driver.find_element(By.XPATH,'//*[@id="upper_back_teeth_past"]').click()
    driver.find_element(By.XPATH,'//*[@id="lower_back_teeth_past"]').click()

    driver.find_element(By.XPATH,'//*[@id="upper_side_teeth_past"]').click()
    driver.find_element(By.XPATH,'//*[@id="lower_side_teeth_past"]').click()

    #GumProblem
    driver.find_element(By.XPATH,'//*[@id="upper_front_teeth_gum"]').click()
    driver.find_element(By.XPATH,'//*[@id="lower_front_teeth_gum"]').click()

    driver.find_element(By.XPATH,'//*[@id="upper_back_teeth_gum"]').click()
    driver.find_element(By.XPATH,'//*[@id="lower_back_teeth_gum"]').click()

    driver.find_element(By.XPATH,'//*[@id="upper_side_teeth_gum"]').click()
    driver.find_element(By.XPATH,'//*[@id="lower_side_teeth_gum"]').click()

    #Habits
    driver.find_element(By.XPATH,'//*[@id="mouth_breathing"]').click()
    driver.find_element(By.XPATH,'//*[@id="thumb_sucking"]').click()
    driver.find_element(By.XPATH,'//*[@id="nail_biting"]').click()
    driver.find_element(By.XPATH,'//*[@id="pencil_biting"]').click()

    #Maligned / Misaligned Teeth
    driver.find_element(By.XPATH,'//*[@id="upper_front_teeth_misaligned"]').click()
    driver.find_element(By.XPATH,'//*[@id="lower_front_teeth_misaligned"]').click()
    driver.find_element(By.XPATH,'//*[@id="upper_back_teeth_misaligned"]').click()
    driver.find_element(By.XPATH,'//*[@id="lower_back_teeth_misaligned"]').click()
    driver.find_element(By.XPATH,'//*[@id="upper_spacing_teeth_misaligned"]').click()
    driver.find_element(By.XPATH,'//*[@id="lower_spacing_teeth_misaligned"]').click()
    driver.find_element(By.XPATH,'//*[@id="upper_crowding_teeth_misaligned"]').click()
    driver.find_element(By.XPATH,'//*[@id="lower_crowding_teeth_misaligned"]').click()
    driver.find_element(By.XPATH,'//*[@id="upper_jaw_teeth_misaligned"]').click()
    driver.find_element(By.XPATH,'//*[@id="lower_jaw_teeth_misaligned"]').click()

    driver.find_element(By.XPATH,'//*[@id="survey-form"]/div[2]/button[2]').click()

@then('fill the form4 & click next')
def click_login(context):
    #ToothDecay
    driver.find_element(By.XPATH,'//*[@id="father_interested"]').click()
    driver.find_element(By.XPATH,'//*[@id="mother_interested"]').click()
    driver.find_element(By.XPATH,'//*[@id="brother1_interested"]').click()
    driver.find_element(By.XPATH,'//*[@id="brother2_interested"]').click()
    driver.find_element(By.XPATH,'//*[@id="sister1_interested"]').click()
    driver.find_element(By.XPATH,'//*[@id="sister2_interested"]').click()

    #Family Dentist Name
    driver.find_element(By.XPATH,'//*[@id="family_dentist"]').send_keys('DentistName')

    #AnyOtherScreening
    driver.find_element(By.XPATH,'//*[@id="other_treatment_eye"]').click()
    driver.find_element(By.XPATH,'//*[@id="other_treatment_ent"]').click()
    driver.find_element(By.XPATH,'//*[@id="other_treatment_other"]').click()

    #Submit
    driver.find_element(By.XPATH,'//*[@id="submit"]').click()


@then('validate if form is submitted')
def click_login(context):
    #ValidateSubmittion
    className = driver.find_element(By.XPATH,'/html/body/main/div/h2')
    try:
        assert "submission" == className
    except AssertionError as e:
        assert context, 'fail'
   

    #CheckDiscountRedirect
    driver.find_element(By.XPATH,'/html/body/main/div/h2/a').click()

@then('verify title {text}')
def verify_title(context, text):
    title = driver.title
    try:
        assert "Million Dollar Smi:)e" == title
    except AssertionError as e:
        assert context, 'fail'