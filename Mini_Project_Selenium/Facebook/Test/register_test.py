from selenium import webdriver
from selenium.webdriver.common.by import By
from Mini_Project_Selenium.Facebook.Base_Test.Locators import *
from time import sleep
def test_Facebook_Validate_Registering_with_Valid_information_by_providing_all_the_fields():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount_Path).click()  # Click Create New Account button
    sleep(2)
    signUp_Page = driver.find_element(By.XPATH,SignUp_PagePath).text  # Display Signup page
    assert 'Sign Up' == signUp_Page
    firstName_box = driver.find_element(By.NAME,FirstName_ElementPath)
    firstName_box.send_keys("bizu")  # entering first name
    sleep(2)
    surname_box = driver.find_element(By.NAME,LastName_ElementPath)
    surname_box.send_keys("belete")  # entering Last name
    sleep(2)
    registerEmail_box = driver.find_element(By.NAME,EmailInput_ElementPath)
    registerEmail_box.send_keys("bizu@****.com")  # entering email address
    sleep(2)
    registerReEnterEmail_box = driver.find_element(By.NAME,EmailReEnter_ElementPath)
    registerReEnterEmail_box.send_keys("bizu@****.com")  # entering Re-enter email address
    sleep(2)
    registerPassword_box = driver.find_element(By.NAME,Password_ElementPath)
    registerPassword_box.send_keys("password")  # entering password
    sleep(2)
    birthDay_box = driver.find_element(By.XPATH,BirthDay_ElementPath)
    birthDay_box.send_keys("08")  # entering Birth Day
    birthDay_box.send_keys("8")  # entering Birth Day
    sleep(2)
    birthMonth_box = driver.find_element(By.XPATH,BirthMonth_ElementPath)
    birthMonth_box.send_keys("nov")  # entering Birth Month
    sleep(2)
    birthYear_box = driver.find_element(By.XPATH,BirthDay_ElementPath)
    birthYear_box.send_keys("1999")  # entering Birth Year
    sleep(2)
    driver.find_element(By.XPATH,GenderSelect_ElementPath).click()  # Select Gender
    sleep(2)
    driver.find_element(By.XPATH,SignUp_ButtonPath).click()  # Click Sign Up Button
    sleep(5)
    email_conformation_Page = driver.find_element(By.XPATH,Email_ConformationPath).text  # Display Email conformation page
    assert 'Enter the code from your email' == email_conformation_Page
    driver.close()
    enterConformationNumber = driver.find_element(By.NAME, "code")
    enterConformationNumber.send_keys("2345678")  # entering conformation number
    sleep(2)
    driver.find_element(By.XPATH,Continue_ButtonPath).click()  # Click Continue Button
    accountConform_page = driver.find_element(By.NAME,"Account Confirmed").text  # Display Account conformation page
    assert 'Account Confirmed' == accountConform_page
    driver.find_element(By.XPATH,Ok_ButtonPath).click()  # Click Ok button
    Facebook_Home = driver.current_url  # Display Facebook User Home page
    assert Facebook_Home == Facebook_Web_Address
    driver.close()



def test_Facebook_Registering_with_Invalid_information_Using_Null_on_all_fields():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH,SignUp_ButtonPath).click()  # Click Sign Up Button
    sleep(5)
    error_Message = driver.find_element(By.XPATH,"/html[1]/body[1]/div[7]/div[1]/div[1]/div[1]").text  # Display Error Message
    error_Message = driver.find_element(By.XPATH,Error_nullAll).text  # Display Error Message
    assert '' == error_Message
    driver.close()


def test_Facebook_Registering_with_Invalid_Email():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount_Path).click()  # Click Create New Account button
    sleep(2)
    signUp_Page = driver.find_element(By.XPATH,SignUp_PagePath).text  # Display Signup page
    assert 'Sign Up' == signUp_Page
    firstName_box = driver.find_element(By.NAME,FirstName_ElementPath)
    firstName_box.send_keys("bizu")  # entering first name
    sleep(2)
    surname_box = driver.find_element(By.NAME,LastName_ElementPath)
    surname_box.send_keys("belete")  # entering Last name
    sleep(2)
    registerEmail_box = driver.find_element(By.NAME,EmailInput_ElementPath)
    registerEmail_box.send_keys("bizu123@gmail.com")  # entering email address
    registerEmail_box.send_keys("bizubelete@gmail.com")  # entering email address
    sleep(2)
    registerReEnterEmail_box = driver.find_element(By.NAME,EmailReEnter_ElementPath)
    registerReEnterEmail_box.send_keys("bizu@gmail.com")  # entering Re-enter email address
    registerReEnterEmail_box.send_keys("bizu@gmail.com")  # entering Re-enter email address
    sleep(2)
    registerPassword_box = driver.find_element(By.NAME,Password_ElementPath)
    registerPassword_box.send_keys("password")  # entering password
    sleep(2)
    birthDay_box = driver.find_element(By.XPATH,BirthDay_ElementPath)
    birthDay_box.send_keys("08")  # entering Birth Day
    birthDay_box.send_keys("08")  # entering Birth Day
    sleep(2)
    birthMonth_box = driver.find_element(By.XPATH,BirthMonth_ElementPath)
    birthMonth_box.send_keys("nov")  # entering Birth Month
    sleep(2)
    birthYear_box = driver.find_element(By.XPATH,BirthDay_ElementPath)
    birthYear_box.send_keys("1999")  # entering Birth Year
    sleep(2)
    driver.find_element(By.XPATH,GenderSelect_ElementPath).click()  # Select Gender
    sleep(2)
    driver.find_element(By.XPATH,SignUp_ButtonPath).click()  # Click Sign Up Button
    sleep(5)
    error_Message = driver.find_element(By.XPATH,"/html[1]/body[1]/div[7]/div[1]/div[1]/div[1]").text  # Display Error Message
    error_Message = driver.find_element(By.XPATH,Error_InvalidEmail).text  # Display Error Message
    assert '' == error_Message
    driver.close()



def test_Facebook_Registering_With_Null_Gender():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount_Path).click()  # Click Create New Account button
    sleep(2)
    signUp_Page = driver.find_element(By.XPATH,SignUp_PagePath).text  # Display Signup page
    assert 'Sign Up' == signUp_Page
    firstName_box = driver.find_element(By.NAME,FirstName_ElementPath)
    firstName_box.send_keys("bizu")  # entering first name
    sleep(2)
    surname_box = driver.find_element(By.NAME,LastName_ElementPath)
    surname_box.send_keys("belete")  # entering Last name
    sleep(2)
    registerEmail_box = driver.find_element(By.NAME,EmailInput_ElementPath)
    registerEmail_box.send_keys("bizu2435@gmail.com")  # entering email address
    registerEmail_box.send_keys("bizubelete@gmail.com")  # entering email address
    sleep(2)
    registerReEnterEmail_box = driver.find_element(By.NAME,EmailReEnter_ElementPath)
    registerReEnterEmail_box.send_keys("bizubelete@gmail.com")  # entering Re-enter email address
    sleep(2)
    registerPassword_box = driver.find_element(By.NAME,Password_ElementPath)
    registerPassword_box.send_keys("password")  # entering password
    sleep(2)
    birthDay_box = driver.find_element(By.XPATH,BirthDay_ElementPath)
    birthDay_box.send_keys("08")  # entering Birth Day
    birthDay_box.send_keys("08")  # entering Birth Day
    sleep(2)
    birthMonth_box = driver.find_element(By.XPATH,BirthMonth_ElementPath)
    birthMonth_box.send_keys("nov")  # enter Birth Month
    sleep(2)
    birthYear_box = driver.find_element(By.XPATH,BirthDay_ElementPath)
    birthYear_box.send_keys("1999")  # entering Birth Year
    sleep(2)
    driver.find_element(By.XPATH,SignUp_ButtonPath).click()  # Click Sign Up Button
    sleep(5)
    error_Message = driver.find_element(By.XPATH,"/html[1]/body[1]/div[7]/div[1]/div[1]/div[1]").text  # Display Error Message
    error_Message = driver.find_element(By.XPATH,Error_nullGender).text  # Display Error Message
    assert '' == error_Message
    driver.close()




def test_Facebook_Registering_with_Null_FirstName():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount_Path).click()  # Click Create New Account button
    sleep(2)
    signUp_Page = driver.find_element(By.XPATH,SignUp_PagePath).text  # Display Signup page
    assert 'Sign Up' == signUp_Page
    surname_box = driver.find_element(By.NAME,LastName_ElementPath)
    surname_box = driver.find_element(By.NAME, LastName_ElementPath)
    surname_box.send_keys("belete")  # entering Last name
    sleep(2)
    registerEmail_box = driver.find_element(By.NAME,EmailInput_ElementPath)
    registerEmail_box.send_keys("bizubelete@gmail.com")  # entering email address
    registerEmail_box.send_keys("bizu@gmail.com")  # entering email address
    sleep(2)
    registerReEnterEmail_box = driver.find_element(By.NAME,EmailReEnter_ElementPath)
    registerReEnterEmail_box.send_keys("bizu@gmail.com")  # entering Re-enter email address
    sleep(2)
    registerPassword_box = driver.find_element(By.NAME,Password_ElementPath)
    registerPassword_box.send_keys("password1234")  # entering password
    sleep(2)
    birthDay_box = driver.find_element(By.XPATH,BirthDay_ElementPath)
    birthDay_box.send_keys("13")  # entering Birth Day
    birthDay_box.send_keys("1")  # entering Birth Day
    sleep(2)
    birthMonth_box = driver.find_element(By.XPATH,BirthMonth_ElementPath)
    birthMonth_box.send_keys("jul")  # entering Birth Month
    sleep(2)
    birthYear_box = driver.find_element(By.XPATH,BirthDay_ElementPath)
    birthYear_box.send_keys("2000")  # entering Birth Year
    sleep(2)
    driver.find_element(By.XPATH,GenderSelect_ElementPath).click()  # Select Gender
    sleep(2)
    driver.find_element(By.XPATH,SignUp_ButtonPath).click()  # Click Sign Up Button
    sleep(5)
    error_Message = driver.find_element(By.XPATH,"/html[1]/body[1]/div[7]/div[1]/div[1]/div[1]").text  # Display Error Message
    error_Message = driver.find_element(By.XPATH,Error_nullFirstName).text  # Display Error Message
    assert '' == error_Message
    driver.close()


def test_Facebook_Registering_with_Null_LastName():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount_Path).click()  # Click Create New Account button
    sleep(2)
    signUp_Page = driver.find_element(By.XPATH,SignUp_PagePath).text  # Display Signup page
    assert 'Sign Up' == signUp_Page
    firstName_box = driver.find_element(By.NAME,FirstName_ElementPath)
    firstName_box.send_keys("bizu")  # entering first name
    sleep(2)
    registerEmail_box = driver.find_element(By.NAME,EmailInput_ElementPath)
    registerEmail_box.send_keys("bizu@****.com")  # entering email address
    sleep(2)
    registerReEnterEmail_box = driver.find_element(By.NAME,EmailReEnter_ElementPath)
    registerReEnterEmail_box.send_keys("bizu@****.com")  # entering Re-enter email address
    sleep(2)
    registerPassword_box = driver.find_element(By.NAME,Password_ElementPath)
    registerPassword_box.send_keys("password")  # entering password
    sleep(2)
    birthDay_box = driver.find_element(By.XPATH,BirthDay_ElementPath)
    birthDay_box.send_keys("1")  # entering Birth Day
    sleep(2)
    birthMonth_box = driver.find_element(By.XPATH,BirthMonth_ElementPath)
    birthMonth_box.send_keys("nov")  # entering Birth Month
    sleep(2)
    birthYear_box = driver.find_element(By.XPATH,BirthDay_ElementPath)
    birthYear_box.send_keys("1999")  # entering Birth Year
    sleep(2)
    driver.find_element(By.XPATH,GenderSelect_ElementPath).click()  # Select Gender
    sleep(2)
    driver.find_element(By.XPATH,SignUp_ButtonPath).click()  # Click Sign Up Button
    sleep(5)
    error_Message = driver.find_element(By.XPATH,Error_nullLastName).text  # Display Email conformation page
    assert '' == error_Message
    driver.close()


def test_Facebook_Registering_with_Null_Birthday():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount_Path).click()  # Click Create New Account button
    sleep(2)
    signUp_Page = driver.find_element(By.XPATH,SignUp_PagePath).text  # Display Signup page
    assert 'Sign Up' == signUp_Page
    firstName_box = driver.find_element(By.NAME,FirstName_ElementPath)
    firstName_box.send_keys("bizu")  # entering first name
    sleep(2)
    surname_box = driver.find_element(By.NAME, LastName_ElementPath)
    surname_box.send_keys("belete")  # entering Last name
    sleep(2)
    registerEmail_box = driver.find_element(By.NAME,EmailInput_ElementPath)
    registerEmail_box.send_keys("youremail@****.com")  # entering email address
    sleep(2)
    registerReEnterEmail_box = driver.find_element(By.NAME,EmailReEnter_ElementPath)
    registerReEnterEmail_box.send_keys("youremail@****.com")  # entering Re-enter email address
    sleep(2)
    registerPassword_box = driver.find_element(By.NAME,Password_ElementPath)
    registerPassword_box.send_keys("password")  # entering password
    sleep(2)
    birthMonth_box = driver.find_element(By.XPATH,BirthMonth_ElementPath)
    birthMonth_box.send_keys("nov")  # entering Birth Month
    sleep(2)
    birthYear_box = driver.find_element(By.XPATH,BirthDay_ElementPath)
    birthYear_box.send_keys("1999")  # entering Birth Year
    sleep(2)
    driver.find_element(By.XPATH,GenderSelect_ElementPath).click()  # Select Gender
    sleep(2)
    driver.find_element(By.XPATH,SignUp_ButtonPath).click()  # Click Sign Up Button
    sleep(5)
    error_Message = driver.find_element(By.XPATH,Error_Birthday).text  # Display Email conformation page
    assert '' == error_Message
    driver.close()