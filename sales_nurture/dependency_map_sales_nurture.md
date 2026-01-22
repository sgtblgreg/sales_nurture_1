# Sales Nurture — Dependency Map (T00 + T01)
*Техническое ТЗ‑описание того, как собрать «первый отчёт» (T01, Day 2) на базе SegFlow Dependency Map.*

> Этот документ **дополняет** базовый Dependency Map (`docs/ai-wiki-lite/dependency_map.md`) и описывает только то, что нужно для **Sales Nurture** (контекст после 1‑й встречи → корпус источников → T01‑отчёт).

## 0) Легенда
- **[BASE]** — элемент базового Dependency Map (канонический; менять/расширять лучше там).
- **[SN]** — элемент Sales Nurture (надстройка для отчётов/интерфейса/пейлоада касаний).

Формы (как в базовой карте):
- `([catalog])` — каталог/таблица данных
- `[analysis]` — анализ/flow
- `[[artifact]]` — артефакт/отчёт (что видит заказчик)

---

## 1) Как Sales Nurture «подключается» к базовой карте

### 1.1. Минимальный вход после первой встречи (T00)
- **[SN]** `sn_t00_brief_min` (форма/пейлоад)
  - **пишет в** **[BASE]** `client_scope`, `client_product_offer`, `client_competitor_shortlist` (subset)
  - источник правды для UI: `lead_brief_template.md`

### 1.2. Корпус источников и QA (для T01)
- **[BASE]** `source_*` → **[BASE]** `analysis_sources_corpus_profile` → **[BASE]** `sources_corpus_profile`
  - в рамках Sales Nurture используем как «двигатель» для блоков KPI + Block 1 + shortlist PDF.

### 1.3. Каталоги (укороченная версия для T01)
- **[BASE]** каталоги: `segments`, `needs`, `features`, `channels`, `sales_best_practices`
  - *Важно:* в этой версии **не требуем** `competitors/triggers/barriers` для T01 (можно добавить позже).

### 1.4. Надстройки Sales Nurture для T01‑отчёта
- **[SN]** `sn_t01_pdf_showcase` — выбор 5 PDF для блока 2
- **[SN]** `sn_doc_analyzer_result[]` — результаты документ‑анализатора для выбранных PDF
- **[SN]** `sn_segment_groups` — кластеризация «лингвистических вариантов» сегментов в группы + агрегированные метрики
- **[SN]** `sn_segment_groups_viz` — подготовка данных для визуализации «созвездие»
- **[SN]** `sn_t01_report_model` — итоговый пейлоад, из которого рендерится отчёт

---

## 2) Диаграмма зависимостей (T00 → T01)

```mermaid
graph LR
  %% ===== T00 =====
  subgraph SN0["T00 (Sales Nurture) — ввод после 1-й встречи"]
    sn_t00_brief_min([sn_t00_brief_min])
  end

  subgraph BASE0["BASE — Client inputs (канонические сущности)"]
    client_scope([client_scope])
    client_product_offer([client_product_offer])
    client_competitor_shortlist([client_competitor_shortlist])
  end

  sn_t00_brief_min --> client_scope
  sn_t00_brief_min --> client_product_offer
  sn_t00_brief_min --> client_competitor_shortlist

  %% ===== Sources & QA =====
  subgraph BASES["BASE — Sources"]
    source_web_search([source_web_search])
    source_competitor_sales_materials([source_competitor_sales_materials])
    source_reviews_platforms([source_reviews_platforms])
    source_video_platforms([source_video_platforms])
    source_statistical_data([source_statistical_data])
    source_regulatory_docs([source_regulatory_docs])
    source_ad_libraries([source_ad_libraries])
    source_platform_audience_insights([source_platform_audience_insights])
  end

  subgraph BASEQA["BASE — QA корпуса"]
    analysis_sources_corpus_profile[analysis_sources_corpus_profile]
    sources_corpus_profile([sources_corpus_profile])
  end

  client_scope --> source_web_search
  client_scope --> source_competitor_sales_materials
  client_scope --> source_reviews_platforms
  client_scope --> source_video_platforms
  client_scope --> source_statistical_data
  client_scope --> source_regulatory_docs
  client_scope --> source_ad_libraries
  client_scope --> source_platform_audience_insights

  source_web_search --> analysis_sources_corpus_profile
  source_competitor_sales_materials --> analysis_sources_corpus_profile
  source_reviews_platforms --> analysis_sources_corpus_profile
  source_video_platforms --> analysis_sources_corpus_profile
  source_statistical_data --> analysis_sources_corpus_profile
  source_regulatory_docs --> analysis_sources_corpus_profile
  source_ad_libraries --> analysis_sources_corpus_profile
  source_platform_audience_insights --> analysis_sources_corpus_profile

  analysis_sources_corpus_profile --> sources_corpus_profile

  %% ===== Catalogs =====
  subgraph BASE1["BASE — каталоги (укороченная версия для T01)"]
    segments([segments])
    needs([needs])
    features([features])
    channels([channels])
    sales_best_practices([sales_best_practices])
  end

  client_scope --> segments
  client_scope --> needs
  client_product_offer --> needs
  client_product_offer --> features
  client_scope --> channels
  client_scope --> sales_best_practices

  %% ===== T01 report build =====
  subgraph SN1["T01 (Sales Nurture) — сборка отчёта Day 2"]
    sn_t01_pdf_showcase([sn_t01_pdf_showcase])
    sn_doc_analyzer_result([sn_doc_analyzer_result[]])
    sn_segment_groups([sn_segment_groups])
    sn_segment_groups_viz([sn_segment_groups_viz])
    sn_t01_report_model[[sn_t01_report_model]]
  end

  sources_corpus_profile --> sn_t01_pdf_showcase
  sn_t01_pdf_showcase --> sn_doc_analyzer_result

  segments --> sn_segment_groups
  sn_doc_analyzer_result --> sn_segment_groups
  sources_corpus_profile --> sn_segment_groups

  sn_segment_groups --> sn_segment_groups_viz

  sources_corpus_profile --> sn_t01_report_model
  segments --> sn_t01_report_model
  needs --> sn_t01_report_model
  features --> sn_t01_report_model
  channels --> sn_t01_report_model
  sales_best_practices --> sn_t01_report_model
  sn_t01_pdf_showcase --> sn_t01_report_model
  sn_doc_analyzer_result --> sn_t01_report_model
  sn_segment_groups --> sn_t01_report_model
  sn_segment_groups_viz --> sn_t01_report_model
```

---

## 3) T00 — `sn_t00_brief_min` (минимальный контекст)

**Цель:** собрать только то, что нужно для T01 и дальнейших касаний, без «полного интервью».

### 3.1. Поля (минимум)
Источник: `docs/sales_nurture/lead_brief_template.md`.

**Обязательные:**
- компания
- продукт (1–3 предложения, *что именно считаем продуктом*)
- сайт/лендинг (если есть)
- география/рынок (scope = продукт × география)
- индустрия/категория
- язык результата (`ru`/`en`)
- окно актуальности (например, 12–18 месяцев)

**Опциональные (но очень желательные):**
- shortlist конкурентов (3–10)
- ограничения (legal/compliance, запреты на каналы/месседжи)
- «почему не купили после 1‑й встречи» (для тональности nurture)

### 3.2. Выход
- Заполняем/обновляем **[BASE]**:
  - `client_scope` (subset: industry + geo + product scope)
  - `client_product_offer` (subset: product description/value props)
  - `client_competitor_shortlist` (если есть)

---

## 4) Корпус источников + QA (Block KPI + Block 1)

### 4.1. Источники (реестр)
**[BASE]** `source_*` должны наполнять единый `sources_registry` (реестр корпуса).

**Минимальный контракт строки реестра (рекомендовано):**
```json
{
  "source_id": "src_...",
  "url": "https://...",
  "type": "web|competitors|ugc|video|reports|ads|regulatory|audience|internal",
  "title": "...",
  "publisher": "...",
  "published_at": "YYYY-MM-DD",
  "fetched_at": "YYYY-MM-DD",
  "geo": "US|EU|...",
  "language": "en|ru|...",
  "is_pdf": true,
  "trust_tier": "A|B|C",
  "status": "found|processed|skipped",
  "skip_reason": "authors_list|appendix|out_of_scope|..." 
}
```

### 4.2. QA / профиль корпуса (качество B72/100)
Используем **[BASE]** `analysis_sources_corpus_profile`, но для Sales Nurture фиксируем **явную формулу**, чтобы результат был воспроизводим.

**Score (0–100):**
`0.30×GeoMatch + 0.25×Freshness + 0.25×Trust + 0.20×Diversity`

**GeoMatch (0–100):**
- доля источников, совпадающих с `client_scope.geo` (или допустимым списком geo) с учётом типа источника.
- пример: `geo_match = processed_sources_in_geo / processed_sources_total`

**Freshness (0–100):**
- доля источников в окне актуальности `time_window_months` + штраф за «ядро старых» источников.
- пример базового правила: `fresh = sources_with(published_at >= now - window) / processed_total`
- штраф: если top‑N (например 20) самых часто цитируемых источников старше окна → минус X.

**Trust (0–100):**
- доля источников tier A/B (независимые, проверяемые, прозрачный автор/организация) + штраф за C.
- `trust = (A*1.0 + B*0.7 + C*0.2) / total` → затем масштабирование в 0–100.

**Diversity (0–100):**
- разнообразие типов и доменов, + penalty за «инфо‑пузырь».
- базовые компоненты:
  - `type_coverage`: есть ли покрытие ключевых типов (web/ugc/reports/competitors/…)
  - `domain_concentration`: доля top‑5 доменов (чем выше — тем хуже)
  - `duplicate_rate`: доля дублей/перепечаток

**Grade:**
- `A` ≥ 85, `B` 70–84, `C` < 70 (порог можно вынести в конфиг).

### 4.3. Block 1: микс источников (pie + breakdown + summary)
Источник данных: **[BASE]** `sources_corpus_profile` (и/или агрегаты из `sources_registry`).

**Что нужно отдать в UI:**
- `found_total` — найдено (может быть заглушкой на ранней версии; диапазон 8–12k)
- `processed_total` — обработано (реальный счётчик по статусу `processed`)
- `by_type[]` — counts + share по каждому `type`
- `quality` — 4 метрики + итоговый score/grade

**Summary по миксу источников (генератор):**
- вход: `by_type`, `quality`, топ‑домены/типы, доля A/B/C, доля свежих;
- выход: 3–6 буллетов (коротко), выбираем по правилам:
  - если `ugc+video` высоко → буллет про proof‑слой и барьеры;
  - если `regulatory` есть → буллет про фильтрацию claims/каналов;
  - если `reports/stat` достаточно → буллет про бенчмарки/приоритизацию;
  - если `diversity` низкая → буллет про риск «инфо‑пузыря» и план доборки.

---

## 5) Block 2: shortlist PDF (5 штук) + Document Analyzer

### 5.1. `sn_t01_pdf_showcase` — как выбираем PDF
Цель блока — **показать качество evidence** и «как работает метод» на 5 понятных PDF.

**Фильтр кандидатов:**
- `is_pdf = true`
- `published_at` в окне актуальности (или рядом; допускаем 1–2 «якоря», если очень trust/high‑value)
- `trust_tier` преимущественно A/B
- `out_of_scope` исключаем

**Скоринг (пример, можно тюнить):**
- `pdf_score = 0.35*trust + 0.25*fresh + 0.25*relevance + 0.15*visual_quality`
  - `trust`: A=1, B=0.7, C=0.2
  - `fresh`: нормализованная свежесть (0..1)
  - `relevance`: тематическая близость к `client_scope` (embedding/keywords)
  - `visual_quality`: эвристика (есть графики/таблицы, читаемый дизайн, не «скан из факса»)

**Выход:** 5 PDF с `title/tags/pdf_url/thumb_url` + ссылка «Посмотреть результат».

### 5.2. `sn_doc_analyzer_result[]` — как делаем анализ PDF
**Ключевой принцип:** doc analyzer **не извлекает “что угодно”**, а матчится к каталогу (synonyms/aliases + нормализация) и сохраняет ссылки на evidence.

**Входы:**
- PDF (из `sn_t01_pdf_showcase`)
- каталоги (**[BASE]**): `segments`, `needs`, `features`, `channels`, `sales_best_practices`

**Выход (рекомендованный контракт):**
```json
{
  "key": "doc_...",
  "title": "...",
  "pdf_url": "...",
  "page_count": 12,
  "items": [
    { "key": "seg_gen_z", "type": "segment", "code": "S01", "label": "Gen Z", "totals": { "count": 12, "pages": 6 } }
  ],
  "pages": [
    {
      "page": 3,
      "plain": "…/page_03.png",
      "marked": "…/page_03_marked.png",
      "hits": { "seg_gen_z": { "count": 2, "anchor": [0.42, 0.55] } }
    }
  ]
}
```

**Что обязательно:**
- `hits.anchor` в нормализованных координатах (0..1), чтобы UI мог рисовать подсветку/стрелки.
- фильтр «не анализировать мусор»:
  - страницы/доки типа `authors_list`, `references`, `appendix`, `legal boilerplate` → `status=skipped` и не влияют на метрики.
- relevance‑фильтр: элементы каталога должны относиться к изучаемому продукту/рынку (используем `client_scope` + `client_product_offer`).

---

## 6) Block 3: группы сегментов (кластеризация + метрики доверия/частоты)

### 6.1. `sn_segment_groups` — что это
На входе много лингвистического разнообразия (Gen Z / Z customers / Younger consumers / …). Нужно собрать **группы** (12–18) и раскрывать варианты.

**Входы:**
- **[BASE]** `segments` (и aliases/synonyms, если есть)
- **[SN]** `sn_doc_analyzer_result[]` (как слой evidence по PDF)
- **[BASE]** `sources_corpus_profile` + `sources_registry` (trust/freshness автора/домена)

**Выход (минимум):**
- `groups[]`:
  - `group_id`, `group_name`, `description`
  - `variants[]` (уникальные формулировки + какие источники это сказали)
  - `stats`: `total_mentions`, `docs_count`, `trust_score`, `freshness_score`

### 6.2. Как считаем trust/freshness для элемента/группы
- `trust_score` элемента = агрегат по evidence‑источникам (вес по количеству упоминаний или по strength evidence).
- `freshness_score` = агрегат по `published_at` источников.
- для группы — суммируем по вариантам, затем нормализуем.

### 6.3. Как кластеризуем варианты в группы
Рекомендуемая реализация (устойчивая к шуму):
1) нормализация строк (lowercase, punctuation, stopwords)
2) candidate‑merge по rules (например, `gen z` + `z consumer` + `younger consumers`)
3) embeddings‑merge (cosine similarity) для оставшихся
4) ручные overrides/aliases (конфиг), чтобы фиксировать «важные» объединения

---

## 7) Block 4: карта групп сегментов (визуализация «созвездие»)

### 7.1. `sn_segment_groups_viz`
**Вход:** `sn_segment_groups.groups[]`

**Выход (для UI):**
- `points[]`: `{ id, label, x, y, size, quad, meta… }`
  - `x` = нормализованная частота (обычно `log1p(total_mentions)` → 0..1)
  - `y` = доверие (0..1, где 1 = high trust)
  - `size` = нормализованное число документов (docs_count)
  - `quad` = один из 4 квадрантов (для подсветки/легенды)

**Важно:** анти‑наложение подписей — задача фронта (раздвижка label + leader line), но backend должен отдавать **истинные** координаты точки.

---

## 8) `sn_t01_report_model` — сборка пейлоада отчёта

**Собираем всё в один «снимок» для T01:**
- KPI: `found_total`, `processed_total`, `queue_total`
- качество: `score/grade` + breakdown (Geo/Fresh/Trust/Diversity)
- Block 1: pie + summary
- Block 2: 5 PDF + ссылки на doc analyzer
- Block 3: группы сегментов (раскрытие)
- Block 4: точки для «созвездия»

Рендер‑слой (UI) должен быть «тонким»: минимум логики, максимум данных из `sn_t01_report_model`.

---

## 9) Что относится к BASE, а что к Sales Nurture (ownership)

**Меняем в BASE (если нужна общесистемная польза):**
- типы источников `source_*` и контракт `sources_registry`
- методика QA корпуса (`analysis_sources_corpus_profile`) и контракт `sources_corpus_profile`
- каталоги `segments/needs/features/channels/sales_best_practices` (структура, aliases/synonyms)

**Делаем в Sales Nurture (надстройки):**
- выбор 5 PDF для блока 2 (`sn_t01_pdf_showcase`)
- doc analyzer UI и результаты для выбранных PDF (`sn_doc_analyzer_result[]`)
- кластеризация вариантов сегментов в группы для «первого value‑drop» (`sn_segment_groups`)
- визуализация «созвездие» (`sn_segment_groups_viz`)
- сборка snapshot‑пейлоада отчёта (`sn_t01_report_model`)

