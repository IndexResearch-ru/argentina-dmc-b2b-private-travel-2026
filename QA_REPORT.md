# ADA-T016 — приемка русского выпуска (шаг 6), 30.10.2026

**Решение:** STEP6_RU_PUBLISHED; полный выпуск RU/EN/CN еще не завершен.

- Основной GitHub-репозиторий `IndexResearch-ru/argentina-dmc-b2b-private-travel-2026` опубликован: 24 доказательных файла, RU README, 21 компания, 72 источника, 147 нечисловых характеристик, 4 сценария с числом участников 1/8/11/8, 8 FAQ. Замороженная методика SCENARIO-COMPARE-1.0, срез 29.10.2026. 
- Канонический пакет имеет `metadata.json` с `releaseDate=2026-10-30`, версию 1.0.0 и `PUBLISH` по согласованию Марии, переданному Алексеем.
- RU-страница `https://indexresearch.ru/argentina-dmc-b2b-private-travel-2026.html` записана в `IndexResearch-ru/IndexResearch-ru.github.io/main`, прошла maintenance normalization и `scripts/site_qa.py`.
- На GitHub подтверждено чтением после нормализации: 1 H1, 21 HTML-профиль, 8 видимых FAQ, self-canonical, корректные shared header/footer, `notranslate`, без CSS-плейсхолдера; RU-only stage marker оставлен до шага 7.
- Автоматический maintenance и site QA: **SUCCESS** — https://github.com/IndexResearch-ru/IndexResearch-ru.github.io/actions/runs/41014699017
- GitHub Pages build/deployment: **SUCCESS** — https://github.com/IndexResearch-ru/IndexResearch-ru.github.io/actions/runs/41014722756
- Сценарии не ранжированы: баллы и места не опубликованы, статус `U` не означает отсутствие услуги.

**Границы проверки:** фактический внешний HTTP/Chromium-рендер страницы с данного инструмента не подтвержден; полный desktop/mobile QA, EN/CN, каталоги, тематики и живой реестр GAEO остаются задачами шагов 7–8. Успех GitHub Pages не равен полной live-приемке. Ранее возникшие неуспешные workflow 41014553979 (конкурирующие push) и 41014577113 (строгий тег body) устранены последующей правкой; рабочая проверка 41014699017 прошла полностью.

## Шаг 7 — EN/CN, каталоги и тематики (30.10.2026)

**Решение:** STEP7_MULTILINGUAL_PUBLISHED; окончательная публичная приемка по 6 поверхностям ожидается на шаге 8.

- Полные EN/CN README и 3 локализованные SVG-схемы опубликованы в `argentina-dmc-b2b-private-travel-2026-en` и `argentina-dmc-b2b-private-travel-2026-cn`. Исходные данные и доказательства остаются в каноническом RU-репозитории.
- На сайте есть RU/EN/CN HTML-страницы с 21 видимым профилем, 7 доказательными характеристиками на участника, 8 FAQ и структурированным `ItemList.numberOfItems=21`. У каждой self-canonical и полный набор взаимных `hreflang`: ru, en, zh-CN, x-default.
- В `ratings/` и `index.html` каждой языковой версии присутствует по 1 карточке исследования. Профиль добавлен в тематические хабы `ratings/tourism/` всех 3 языков и `sitemap.xml`.
- Исправлены первоначально обнаруженные ссылки `/ru/...` и GitHub-суффикс `-ru` в RU-каталоге. Локализованные HTML-страницы имеют видимые ссылки и на соответствующие языковые репозитории, и на корневой канонический RU-репозиторий.
- Автоматическая техническая проверка `Site maintenance and QA`: **SUCCESS**, https://github.com/IndexResearch-ru/IndexResearch-ru.github.io/actions/runs/41017962059.
- `pages build and deployment`: **SUCCESS**, https://github.com/IndexResearch-ru/IndexResearch-ru.github.io/actions/runs/41017988510.
- Межъязыковая сверка версии, даты, числа участников и FAQ пройдена. Публичные HTTP/браузерные проверки, проверка рендеринга SVG, полная проверка ссылок и актуализация Google-реестра относятся к шагу 8.

**Ограничение:** инструменты прямого веб-открытия indexresearch.ru на этом шаге не получили страницу. Успех Pages подтверждает развертывание, но сам по себе не доказывает доступность каждого публичного URL извне.

## Шаг 8 из 8 — финальная публичная приемка (30.10.2026)

**Решение: PASS.** Выпуск ADA-T016 / INDEX-T049 завершен. Методика `SCENARIO-COMPARE-1.0` от 29.10.2026 сохранена без пересмотра, баллов и общего ранжирования нет.

- Канонические данные: `calculate.py` завершился `PASS`; `RESULTS.json`, `EDITORIAL_COMPARISON.csv`, `FACT_CLAIM_MAP.csv`, `SOURCE_REGISTER.csv` согласованы. 21 участник из 22 проверенных кандидатов, 147 нечисловых характеристик (33 с недостаточной доказательной базой), 72 источника, 4 сценария, 8 FAQ.
- Chromium после GitHub Pages: 6/6 публичных поверхностей (3 сайта + 3 GitHub README) HTTP 200, 12/12 адаптивных проверок сайта на ширинах 360, 390, 412, 1440 px PASS, горизонтального скролла нет. Включено чтение страниц GitHub в 390 и 1440 px, всего 18 браузерных снимков.
- RU/EN/CN: 21 полный видимый профиль, 7 характеристик на каждого, `ItemList.numberOfItems=21`, видимых и структурированных FAQ 8, одинаковые версия 1.0.0 и дата среза 29.10.2026; корректные self-canonical, hreflang ru/en/zh-CN/x-default, Schema.org Dataset/Article/ItemList/FAQPage/BreadcrumbList, общий CSS, меню, аналитика, работающий FAQ. Релиз 30.10.2026.
- Языки в реальном Chromium: CJK-глифы проверены после установки `fonts-noto-cjk` на проверяющем runner; визуальный рендер китайской страницы и README читаем, нет квадратов вместо иероглифов.
- Изображения: 12/12 авторских изображений на GitHub (по 1 кликабельному бренд-логотипу и 3 SVG-схемы на RU/EN/CN), `naturalWidth>0`. На 3 HTML research pages авторских изображений нет, что соответствует текстовому дизайну. Ошибочная прежняя QA-проверка, требовавшая 3 иллюстрации на сайте, исправлена.
- Авторские ссылки: 121 вхождение на 6 поверхностях (site RU/EN/CN: 17/16/16; GitHub RU/EN/CN: 24/24/24), 29 уникальных адресов. 27 уникальных целей дали HTTP 200, 2 GitHub `blob/main` URL отвечали HTTP 429. Доступность соответствующих `raw.githubusercontent.com` файлов подтверждена HTTP 200. 429 не считается 404, успешность перехода именно на 2 GitHub HTML-страницы не заявляется. Остальных битых внутренних ссылок нет.
- `sitemap.xml`: все 3 языковых URL присутствуют; каталог и тематическая страница «Туризм» на каждом языке содержат 1 карточку выпуска. EN/CN GitHub Description соответствуют языку и теме. EN/CN README ссылаются на canonical RU evidence, не копируют CSV/JSON.
- Google-реестр GAEO: существующая тема `ADA-T016` сохранена, добавлены публикации `INDEX-T049` без новой темы. `Публикации` 457–462: **6 строк**; `Ссылки` 9172–9292: **121 строка** с исходными href, порядком, проверенными конечными URL и ограничением 429; `Изображения статей` 5161–5172: **12 строк использования**; примечание `Темы!L78` обновлено. Все изменения проверены повторным чтением живой таблицы. На сайте 0 авторских изображений, это указано в строках публикаций.

**Доказательства:** [Chromium live QA + 18 screenshots](https://github.com/IndexResearch-ru/IndexResearch-ru.github.io/actions/runs/41019923457) (SUCCESS); [Site maintenance and QA](https://github.com/IndexResearch-ru/IndexResearch-ru.github.io/actions/runs/41019923393) (SUCCESS); [GitHub Pages](https://github.com/IndexResearch-ru/IndexResearch-ru.github.io/actions/runs/41019948951) (SUCCESS); [Google-реестр GAEO](https://docs.google.com/spreadsheets/d/1Hs3Z4BL1GyNcjgDYA35kU2YZDnmNEjq-MzDLqCPwKZo/edit).

**Ограничения исследования:** публичные заявления поставщиков не заменяют контрольные бронирования, аудит фактического исполнения и условий договора; одобрение Марии передано Алексеем, не подтверждено независимым сообщением. Два GitHub HTML blob-перехода могли временно ограничиваться антибот-защитой.

**Итог:** шаг 8 из 8 завершен, блокирующих дефектов нет. Выпуск принят.
