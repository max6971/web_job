from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Функция для листания параграфов статьи
def browse_paragraphs(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, 'p')
    for paragraph in paragraphs:
        print(paragraph.text)
        next_action = input("Нажмите Enter для продолжения или введите 'q' для выхода: ")
        if next_action.lower() == 'q':
            break

# Функция для выбора одной из связанных страниц и перехода на неё
def browse_related_pages(browser):
    links = browser.find_elements(By.XPATH, "//a[contains(@href, '/wiki/') and not(contains(@href, ':'))]")
    for idx, link in enumerate(links[:10]):  # Ограничиваемся первыми 10 ссылками для простоты
        print(f"{idx + 1}. {link.text}")
    choice = int(input("Введите номер ссылки для перехода или '0' для возврата: "))
    if choice > 0 and choice <= len(links):
        links[choice - 1].click()
        time.sleep(3)
        main_menu(browser)

# Основное меню для выбора действий
def main_menu(browser):
    while True:
        print("Выберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        choice = input("Введите номер действия: ")
        if choice == '1':
            browse_paragraphs(browser)
        elif choice == '2':
            browse_related_pages(browser)
        elif choice == '3':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

# Основная программа
browser = webdriver.Firefox()
search_ass = input("Введите запрос: ")

browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
assert 'Википедия' in browser.title


search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(search_ass)
search_box.send_keys(Keys.RETURN)


main_menu(browser)

browser.quit()