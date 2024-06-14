from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application
from selenium.webdriver.chrome.options import Options


def browser_init(context, scenario_name):
    """
    :param scenario_name:
    :param context: Behave context
    """
    ###
    ### HEADLESS MODE ####
    ###
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #options.add_argument("--window-size=1920,1080")
    #options.add_argument("--start-maximized")
    #service = Service(ChromeDriverManager().install())
    #context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    #)

    ###
    ### FIREFOX BROWSER ###
    ###

    #driver_path = GeckoDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Firefox(service=service)



    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service)
    #context.driver.is_mobile = False

    ### BROWSERSTACK ###
    #Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    #bs_user = 'kervynrivero_hKq7jr'
    #bs_key = 'Kx8QpEfdqfsCsNeeWRNQ'
    #url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    #options = Options()

    #bstack_options = {
    #    "os": "Windows",
    #    "osVersion": "11",
    #     "browserName": "Edge",
    #    "browserVersion": "latest",
    #    'sessionName': scenario_name
    #}
    #options.set_capability('bstack:options', bstack_options)
    #context.driver = webdriver.Remote(command_executor=url, options=options)


    mobile_emulation = {
        "deviceName": "iPhone SE"  # You can use other device names as well
    }
    # Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.is_mobile = True


    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #options.add_argument("--window-size=1920,1080")
    #options.add_argument("--start-maximized")
    #service = Service(ChromeDriverManager().install())
    #context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    #)

    context.driver.maximize_window()
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
