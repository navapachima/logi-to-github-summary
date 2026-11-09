from playwright.sync_api import Page, expect
from pages.login_github import LoginPage
from utilities.config import TEST_PASSWORD_GITHUB, TEST_USERNAME_GITHUB


def test_sign_in_to_gmail(page: Page):
    signInPage = LoginPage(page)
    signInPage.open()
    
    signInPage.clickOnSignInButton()
    signInPage.waitForLoginPage()

    assert TEST_USERNAME_GITHUB is not None
    assert TEST_PASSWORD_GITHUB is not None

    page.pause()

    signInPage.usernameField.fill(TEST_USERNAME_GITHUB)
    signInPage.passwordField.fill(TEST_PASSWORD_GITHUB)

    expect(signInPage.signInButtonWithCredentials).to_be_enabled()
    
    pass

