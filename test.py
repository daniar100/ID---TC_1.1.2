from playwright.sync_api import sync_playwright
import time
import os
import json

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
        while True:
            page.goto("https://dev.daribar.kz/")
            time.sleep(70)
            break
        local_storage = page.evaluate('''() => {
                                        let data = {};
                                        for (let i = 0; i < localStorage.length; i++) {
                                            let key = localStorage.key(i);
                                            data[key] = localStorage.getItem(key);
                                        }
                                        return data;
                                    }''')
        with open("storage_load_deskctop.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        browser.close()