#Проверка
# «Создание заказа самовывоз
# неавторизированным пользователем оплата в Kaspi»

from playwright.sync_api import sync_playwright
import allure
import os
import json
import time

@allure.step("begin")
def test_main():
    with  sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
        **p.devices["Pixel 5"],
        permissions=["geolocation"],
        geolocation={"latitude": 37.7749, "longitude": -122.4194},
        locale='en-US',
    )

        page = context.new_page()
        page.goto("https://dev.daribar.kz/")
        # Загрузка данных в localStorage

        page.locator("input").click()
        page.locator("input").fill("Парацетамол")
        sel=page.get_by_text("Парацетамол таблетки 500 мг №10").first
        sel.click()
        page.wait_for_timeout(3000)
        local_storage = page.evaluate('''() => {
                                let data = {};
                                for (let i = 0; i < localStorage.length; i++) {
                                    let key = localStorage.key(i);
                                    data[key] = localStorage.getItem(key);
                                }
                                return data;
                            }''')
        with open("storage_load2.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        browser.close()
time.sleep(2)
@allure.step("paracetamol")
def test_paracetomol():
    with  sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
        **p.devices["Pixel 5"],
        permissions=["geolocation"],
        geolocation={"latitude": 37.7749, "longitude": -122.4194},
        locale='en-US',
    )

        page = context.new_page()
        page.goto("https://dev.daribar.kz/products/paracetamol-0-5-10--3c20eebe-3ee1-4d9e-bd34-0ba2afd85286")
        with open("storage_load2.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)

        page.evaluate('''(data) => {
                       for (const key in data) {
                           localStorage.setItem(key, data[key]);
                           }
                       }''', local_storage_data)
        page.reload()
        page.wait_for_timeout(2000)
        page.get_by_text("В корзину").click()
        page.locator(".mobile_myCart__IJxPF").click()
        local_storage = page.evaluate('''() => {
                                        let data = {};
                                        for (let i = 0; i < localStorage.length; i++) {
                                            let key = localStorage.key(i);
                                            data[key] = localStorage.getItem(key);
                                        }
                                        return data;
                                    }''')
        with open("storage_load3.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        browser.close()

@allure.step("naiti_apteka")
def test_naiti_apteka():
    with  sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
        **p.devices["Pixel 5"],
        permissions=["geolocation"],
        geolocation={"latitude": 37.7749, "longitude": -122.4194},
        locale='en-US',
    )

        page = context.new_page()
        page.goto("https://dev.daribar.kz/cart")
        with open("storage_load3.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)
        page.evaluate('''(data) => {
                               for (const key in data) {
                                   localStorage.setItem(key, data[key]);
                                   }
                               }''', local_storage_data)
        page.reload()
        page.wait_for_timeout(2000)
        page.get_by_text("Найти в аптеках").click()
        local_storage = page.evaluate('''() => {
                                                let data = {};
                                                for (let i = 0; i < localStorage.length; i++) {
                                                    let key = localStorage.key(i);
                                                    data[key] = localStorage.getItem(key);
                                                }
                                                return data;
                                            }''')
        with open("storage_load4.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        browser.close()

@allure.step("ofo_form")
def test_ofo_form():
    with  sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
        **p.devices["Pixel 5"],
        permissions=["geolocation"],
        geolocation={"latitude": 37.7749, "longitude": -122.4194},
        locale='en-US',
    )

        page = context.new_page()
        page.goto("https://dev.daribar.kz/pharmacies")
        with open("storage_load4.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)
        page.evaluate('''(data) => {
                               for (const key in data) {
                                   localStorage.setItem(key, data[key]);
                                   }
                               }''', local_storage_data)
        page.reload()
        sel=page.get_by_text("Перейти к оформлению 110₸").first
        sel.click()
        page.wait_for_timeout(2000)
        local_storage = page.evaluate('''() => {
                                                        let data = {};
                                                        for (let i = 0; i < localStorage.length; i++) {
                                                            let key = localStorage.key(i);
                                                            data[key] = localStorage.getItem(key);
                                                        }
                                                        return data;
                                                    }''')
        with open("storage_load5.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        browser.close()


@allure.step("dos")
def test_dos():
    with  sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
        **p.devices["Pixel 5"],
        permissions=["geolocation"],
        geolocation={"latitude": 37.7749, "longitude": -122.4194},
        locale='en-US',
    )
        page = context.new_page()
        page.wait_for_timeout(2000)
        page.goto("https://dev.daribar.kz/checkout")
        with open("storage_load6.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)
        page.evaluate('''(data) => {
                               for (const key in data) {
                                   localStorage.setItem(key, data[key]);
                                   }
                               }''', local_storage_data)
        page.reload()
        page.wait_for_timeout(2000)
        full_xpath = "/html/body/div[1]/div[2]/div/div[2]/form/div[2]/input"
        page.wait_for_selector(f'xpath={full_xpath}')
        input_element = page.locator(f'xpath={full_xpath}')
        input_element.clear()
        input_element.type("7075999527")
        page.wait_for_timeout(2000)
        page.get_by_text("Перейти к оплате").click()
        page.wait_for_timeout(2000)
        page.get_by_text("Подтвердить").click()
        page.wait_for_timeout(2000)
        local_storage = page.evaluate('''() => {
                                                                let data = {};
                                                                for (let i = 0; i < localStorage.length; i++) {
                                                                    let key = localStorage.key(i);
                                                                    data[key] = localStorage.getItem(key);
                                                                }
                                                                return data;
                                                            }''')
        with open("storage_load7.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        browser.close()


