# UI-автотесты для сейчас  vpoxod_ru
Учебный проект: UI-тесты для сайта vpoxod.ru

<!-- Технологии -->
## Использованы технологии:
<p  align="left">
  <code><img width="5%" title="Python" src="media/logo/python.png"></code>
  <code><img width="5%" title="Pycharm" src="media/logo/pycharm.png"></code>
  <code><img width="5%" title="Pytest" src="media/logo/pytest.png"></code>
  <code><img width="5%" title="Selenium" src="media/logo/selenium.png"></code>
  <code><img width="5%" title="Selene" src="media/logo/selene.png"></code>
  <code><img width="5%" title="GitHub" src="media/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="media/logo/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="media/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="media/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="media/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="media/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="media/logo/tg.png"></code>
</p>

<!-- Тест кейсы -->

## Автоматизировано тестирование функционала:
* Поле поиска в хедере (позитивный и негативный сценарий)
* Форма поиска на главной - быстрый подбор путешествия по параметрам
* Подбор путешествия по параметрам (по цене)
* Проверка главного меню сайта
* Проверка файла логотипа

## Запуск тестов в Jenkins
<p  align="left">
  <code><img width="5%" title="Jenkins" src="media/logo/jenkins.png"></code>
</p>

### [Jenkins](https://jenkins.autotests.cloud/job/005_tsgibneva_vpoxodru_ui_tests/)

#### Запуск тестов:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```
  
