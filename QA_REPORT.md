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
