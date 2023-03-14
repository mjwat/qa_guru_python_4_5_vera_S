import os
import platform
from selene import browser, have, command
from selenium.webdriver import ActionChains, Keys


def test_fill_and_send_form(open_demoqa):
    browser.element('#fixedban').perform(command.js.remove)

    browser.element('#firstName').type('Vera')
    browser.element('#lastName').type('Sakhno')
    browser.element('#userEmail').type('mjw@gmail.com')

    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('0987654321')

    browser.element('#dateOfBirthInput').click()
    os_name = platform.system()  # to press Command or Control according OS
    action = ActionChains(browser.driver)
    if os_name == "Darwin":
        action.key_down(Keys.COMMAND).send_keys('A').key_up(Keys.COMMAND).perform()
    else:
        action.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
    browser.element('#dateOfBirthInput').type('05 Mar 1994').send_keys(Keys.ESCAPE)

    browser.element('#subjectsInput').type('Computer Science').press_enter().type('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-3"]').click()

    image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resources', 'duck.png'))
    browser.element('#uploadPicture').type(image_path)

    browser.element('#currentAddress').type('1st avenue 234 - 56, zip 678967')

    browser.element('#react-select-3-input').send_keys('Haryana').send_keys(Keys.RETURN)
    browser.element('#react-select-4-input').send_keys('Karnal').send_keys(Keys.RETURN)

    browser.element('#submit').perform(command.js.click)

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('//*[contains(text(),"Student Name")]/following-sibling::td').should(have.text('Vera Sakhno'))
    browser.element('//*[contains(text(),"Student Email")]/following-sibling::td').should(have.text('mjw@gmail.com'))
    browser.element('//*[contains(text(),"Gender")]/following-sibling::td').should(have.text('Female'))
    browser.element('//*[contains(text(),"Mobile")]/following-sibling::td').should(have.text('0987654321'))
    browser.element('//*[contains(text(),"Date of Birth")]/following-sibling::td').should(have.text('05 March,1994'))
    browser.element('//*[contains(text(),"Subjects")]/following-sibling::td').should(
        have.text('Computer Science, Maths'))
    browser.element('//*[contains(text(),"Hobbies")]/following-sibling::td').should(have.text('Music'))
    browser.element('//*[contains(text(),"Picture")]/following-sibling::td').should(have.text('duck.png'))
    browser.element('//*[contains(text(),"Address")]/following-sibling::td').should(
        have.text('1st avenue 234 - 56, zip 678967'))
    browser.element('//*[contains(text(),"State and City")]/following-sibling::td').should(have.text('Haryana Karnal'))
