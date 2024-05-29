from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open the sign-in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()


@when('Log in to the page, email: {email} password: {password}')
def log_in(context, email, password):
    context.app.sign_in_page.login_user(email,password)


@then('Change the language of the page to {language}')
def change_language(context, language):
    context.app.side_bar.go_to_menu()
    context.app.main_menu_page.change_language(context, language)

@then('Verify the language has changed to {language}')
def verify_language(context, language):
    context.app.main_menu_page.verify_language(language)
