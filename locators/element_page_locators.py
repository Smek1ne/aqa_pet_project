from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # fields form
    FULL_NAME = (By.CSS_SELECTOR, "#userName")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#permanentAddress")

    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")

    OUTPUT_NAME = (By.CSS_SELECTOR, "#output #name")
    OUTPUT_EMAIL = (By.CSS_SELECTOR, "#output #email")
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    OUTPUT_PERM_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    CHECKBOX_LIST = (By.CSS_SELECTOR, 'span.rct-text')
    CHECKED_BOXES = (By.CSS_SELECTOR, '.rct-icon-check')
    RESULT_MESSAGE = (By.CSS_SELECTOR, '#result')
    BOX_NAMES_FROM_RESULT = (By.CSS_SELECTOR, 'span.text-success')
    CHECKBOX_TITLE = (By.XPATH, './/ancestor::span[@class="rct-text"]')


class RadioButtonLocators:
    YES = (By.CSS_SELECTOR, '[for="yesRadio"]')
    IMPRESSIVE = (By.CSS_SELECTOR, 'label[for="impressiveRadio"]')
    NO = (By.CSS_SELECTOR, 'label[for="noRadio"]')
    SUCCESS_TEXT = (By.CSS_SELECTOR, 'p span[class="text-success"]')


class WebTablesLocators:
    # add person
    ADD_BUTTON = (By.CSS_SELECTOR, "#addNewRecordButton")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, '#firstName')
    LASTNAME_INPUT = (By.CSS_SELECTOR, '#lastName')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#userEmail')
    AGE_INPUT = (By.CSS_SELECTOR, '#age')
    SALARY_INPUT = (By.CSS_SELECTOR, '#salary')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, '#department')
    SUBMIT_BTN = (By.CSS_SELECTOR, '#submit')
    # tables
    ALL_PEOPLE_LIST = (By.CSS_SELECTOR, '.rt-tr-group')
    SEARCH_FIELD = (By.CSS_SELECTOR, '#searchBox')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = (By.XPATH, './/ancestor::div[@class="rt-tr-group"]')


class TestButtonPageLocators:
    DOUBLE_CLICK = (By.CSS_SELECTOR, '#doubleClickBtn')
    RIGHT_CLICK = (By.CSS_SELECTOR, '#rightClickBtn')
    CLICK_ME = (By.XPATH, "//*[..='Click Me']")

    DOUBLE_CLK_MESSAGE = (By.CSS_SELECTOR, '#doubleClickMessage')
    RIGHT_CLK_MESSAGE = (By.CSS_SELECTOR, '[id="rightClickMessage"]')
    CLICK_ME_MESSAGE = (By.CSS_SELECTOR, '#dynamicClickMessage')


class LinkPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, '#simpleLink')
    DYNAMIC_LINK = (By.CSS_SELECTOR, '#dynamicLink')
    BAD_REQUEST = (By.CSS_SELECTOR, '#bad-request')
    CREATED = (By.CSS_SELECTOR, '#created')
    NO_CONTENT = (By.CSS_SELECTOR, '#no-content')
    MOVED = (By.CSS_SELECTOR, '#moved')
    UNAUTHORIZED = (By.CSS_SELECTOR, '#unauthorized')
    FORBIDDEN = (By.CSS_SELECTOR, '#unauthorized')
    NOT_FOUND = (By.CSS_SELECTOR, '#invalid-url')


class UploadAndDownloadLocators:
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, '#downloadButton')
    SELECT_FILE = (By.CSS_SELECTOR, '#uploadFile')
    UPLOADED_RESULT = (By.CSS_SELECTOR, '[id="uploadedFilePath"]')


class DynamicPropertiesPageLocators:
    WILL_ENABLE_BUTTON = (By.CSS_SELECTOR, '#enableAfter')
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, '#colorChange')
    VISIBLE_AFTER_BUTTON = (By.CSS_SELECTOR, '#visibleAfter')
