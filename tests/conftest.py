import pytest
import allure
from playwright.sync_api import Page
from pages.mf_function_page import function_url, FUNCTION_NODE, FUNCTION_INPUT, SAVE_BUTTON, PLAY_BUTTON, VIEW_INPUT_OUTPUT_DATA, OUTPUT_DATA, TABLE_OUTPUT

@pytest.fixture
def login_leskov(page: Page):
    @allure.step("Логин пользователя{username}")
    def _login(username = '_leskov', password = '_leskov'):
        page.goto(function_url)
        page.fill('#username', username)
        page.fill('#password', password)
        page.click('#kc-login')
        page.wait_for_url(function_url)
    return _login

@pytest.fixture
def run_function_test(page: Page):
    def _runner(function_code, expected_value):
        with allure.step("Открытие кубика 'Функции'"):
            page.locator(FUNCTION_NODE).wait_for()
            page.locator(FUNCTION_NODE).dblclick()
        
        with allure.step("Очистка инпута и ввод формулы"):
            page.locator(FUNCTION_INPUT).wait_for()
            page.locator(FUNCTION_INPUT).click()
            page.locator(FUNCTION_INPUT).select_text()
            page.keyboard.press('Backspace')
            page.locator(FUNCTION_INPUT).fill(function_code)
        
        with allure.step("Сохранение настроек кубика"):
            page.locator(SAVE_BUTTON).click()
        
        with allure.step("Запуск кубика"):
            page.locator(PLAY_BUTTON).wait_for()
            page.locator(PLAY_BUTTON).click()
        
        with allure.step("Проверка таблицы выходных данных"):
            page.locator(VIEW_INPUT_OUTPUT_DATA).click()
            page.locator(OUTPUT_DATA).click()
            page.locator(TABLE_OUTPUT).wait_for(state='visible')
            page.wait_for_timeout(1000)

        with allure.step("Проверка результата работы кубика"):
            table_locator = page.locator(TABLE_OUTPUT)
            rows = table_locator.locator('tbody tr')

            for i in range(rows.count()):
                row = rows.nth(i)
                cell_text = row.locator('td').nth(16).text_content()
                if expected_value in cell_text:
                    assert expected_value in cell_text
                    return
            assert False, f"Функция '{function_code}' не пашет"
    return _runner