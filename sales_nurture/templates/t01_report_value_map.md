<div class="reportHeader">
  <div>
    <div class="reportTitle">Touch 01 — Профиль источников + сегменты (первый срез)</div>
    <div class="reportSub">Профиль корпуса источников + первые “сигналы рынка”: сегменты/контексты и их уверенность</div>
  </div>
</div>

<div class="kpiGrid">
  <div class="kpiCard">
    <div class="kpiLabel">Корпус источников</div>
    <div class="kpiValue">420 обработано • 8 563 найдено</div>
    <div class="kpiNote">В очереди (найдено, но не обработано): <b>8 143</b>. Разнотипные источники: web, конкуренты, отзывы, видео, отчёты, ad libraries, регуляторика, audience insights.</div>
    <div class="sfKpiLinks">
      <a class="sfInlineLink" href="https://example.com/source_repository" target="_blank" rel="noopener noreferrer">Ссылка на хранилище</a>
      <button class="sfInlineBtn" data-sf-action="open_sources_registry">Открыть таблицу (420)</button>
    </div>
  </div>
  <div class="kpiCard">
    <div class="kpiLabel">Качество корпуса</div>
    <div class="kpiValue">B (72/100)</div>
    <div class="kpiNote">Geo‑match 82% • свежесть 74% • trust A/B 57% • diversity 73% (penalty: “инфо‑пузырь”).</div>
    <details class="sfDetails">
      <summary>Как считаем 72/100 (логика)</summary>
      <div class="sfDetailsBody">
        <div><b>Скоринг:</b> 0.30×GeoMatch + 0.25×Freshness + 0.25×Trust + 0.20×Diversity</div>
        <ul>
          <li><b>GeoMatch</b> — доля источников, релевантных географии/рынку.</li>
          <li><b>Freshness</b> — доля источников в окне актуальности + штраф за устаревшие “ядра” корпуса.</li>
          <li><b>Trust</b> — доля независимых/проверяемых источников (A/B) и штраф за C.</li>
          <li><b>Diversity</b> — разнообразие доменов/типов + штраф за “инфо‑пузырь”.</li>
        </ul>
        <div class="expertOnly">
          <div style="margin-top:10px;"><b>“Инфо‑пузырь”:</b> много повторов и мало независимых подтверждений (PR‑перепечатки/одни и те же тезисы без данных).</div>
        </div>
      </div>
    </details>
  </div>
  <div class="kpiCard">
    <div class="kpiLabel">Извлечено (кластеры)</div>
    <div class="kpiValue">21 сегмент • 52 потребности</div>
    <div class="kpiNote">126 функций • 21 канал • 18 конкурентов • 12 триггеров • 16 барьеров.</div>
  </div>
</div>

<div class="chartCard">
  <div class="chartTitle">Блок 1 — Микс источников (самое важное)</div>
  <div class="sfMixRow sfMixRow3">
    <svg class="sfPie" width="320" height="320" viewBox="0 0 200 200" role="img" aria-label="Source mix pie chart">
      <circle cx="100" cy="100" r="68" fill="none" stroke="rgba(255,255,255,0.10)" stroke-width="30"></circle>
      <!-- circumference ~ 427.257 (r=68) -->
      <circle class="sfPieSeg" data-sf-action="open_source_segment" data-sf-payload="web" cx="100" cy="100" r="68" fill="none" stroke="#60a5fa" stroke-width="30" stroke-dasharray="148.523 278.734" stroke-dashoffset="0" transform="rotate(-90 100 100)"></circle>
      <circle class="sfPieSeg" data-sf-action="open_source_segment" data-sf-payload="competitors" cx="100" cy="100" r="68" fill="none" stroke="#22c55e" stroke-width="30" stroke-dasharray="87.486 339.771" stroke-dashoffset="-148.523" transform="rotate(-90 100 100)"></circle>
      <circle class="sfPieSeg" data-sf-action="open_source_segment" data-sf-payload="ugc" cx="100" cy="100" r="68" fill="none" stroke="#f59e0b" stroke-width="30" stroke-dasharray="62.054 365.203" stroke-dashoffset="-236.008" transform="rotate(-90 100 100)"></circle>
      <circle class="sfPieSeg" data-sf-action="open_source_segment" data-sf-payload="video" cx="100" cy="100" r="68" fill="none" stroke="#a78bfa" stroke-width="30" stroke-dasharray="42.726 384.531" stroke-dashoffset="-298.062" transform="rotate(-90 100 100)"></circle>
      <circle class="sfPieSeg" data-sf-action="open_source_segment" data-sf-payload="reports" cx="100" cy="100" r="68" fill="none" stroke="#38bdf8" stroke-width="30" stroke-dasharray="34.587 392.669" stroke-dashoffset="-340.788" transform="rotate(-90 100 100)"></circle>
      <circle class="sfPieSeg" data-sf-action="open_source_segment" data-sf-payload="ads" cx="100" cy="100" r="68" fill="none" stroke="#fb7185" stroke-width="30" stroke-dasharray="25.432 401.825" stroke-dashoffset="-375.375" transform="rotate(-90 100 100)"></circle>
      <circle class="sfPieSeg" data-sf-action="open_source_segment" data-sf-payload="regulatory" cx="100" cy="100" r="68" fill="none" stroke="#f97316" stroke-width="30" stroke-dasharray="16.276 410.980" stroke-dashoffset="-400.807" transform="rotate(-90 100 100)"></circle>
      <circle class="sfPieSeg" data-sf-action="open_source_segment" data-sf-payload="audience" cx="100" cy="100" r="68" fill="none" stroke="#94a3b8" stroke-width="30" stroke-dasharray="10.173 417.084" stroke-dashoffset="-417.084" transform="rotate(-90 100 100)"></circle>
      <circle cx="100" cy="100" r="46" fill="rgba(7,10,18,0.75)"></circle>
      <text x="100" y="96" text-anchor="middle" font-size="20" font-weight="900" fill="rgba(255,255,255,0.92)">420</text>
      <text x="100" y="118" text-anchor="middle" font-size="10" font-weight="900" fill="rgba(255,255,255,0.70)">обработано</text>
      <text x="100" y="134" text-anchor="middle" font-size="10" font-weight="900" fill="rgba(255,255,255,0.55)">из 8 563</text>
    </svg>

    <div class="sfSummary sfSummaryCard sfMixLegendCard">
      <div class="sfSummaryTitle">Сектора диаграммы (что означает каждый)</div>
      <div class="sfSummaryBody">
        <p class="help">Наведи на сектор (или на строку) — подсветим на диаграмме и в списке. Клик → откроем примеры источников.</p>
      </div>
      <div class="sfLegend">
        <button class="sfLegendRow" data-sf-action="open_source_segment" data-sf-payload="web">
          <span class="sfLegendSwatch" style="background:#60a5fa;"></span>
          <div class="sfLegendText">
            <div class="sfLegendMain">Web search — <b>146</b> (35%)</div>
            <div class="sfLegendDesc">Независимые материалы: статьи, блоги, обзоры, исследования.</div>
          </div>
        </button>
        <button class="sfLegendRow" data-sf-action="open_source_segment" data-sf-payload="competitors">
          <span class="sfLegendSwatch" style="background:#22c55e;"></span>
          <div class="sfLegendText">
            <div class="sfLegendMain">Материалы конкурентов — <b>86</b> (20%)</div>
            <div class="sfLegendDesc">Лендинги/сторы/PR/кейсы: что они обещают и как упаковывают.</div>
          </div>
        </button>
        <button class="sfLegendRow" data-sf-action="open_source_segment" data-sf-payload="ugc">
          <span class="sfLegendSwatch" style="background:#f59e0b;"></span>
          <div class="sfLegendText">
            <div class="sfLegendMain">Отзывы/сообщества (UGC) — <b>61</b> (15%)</div>
            <div class="sfLegendDesc">“Живой голос”: ожидания, барьеры, причины недоверия/возвратов.</div>
          </div>
        </button>
        <button class="sfLegendRow" data-sf-action="open_source_segment" data-sf-payload="video">
          <span class="sfLegendSwatch" style="background:#a78bfa;"></span>
          <div class="sfLegendText">
            <div class="sfLegendMain">Видео — <b>42</b> (10%)</div>
            <div class="sfLegendDesc">YouTube/TikTok/обзоры: форматы, триггеры, реальный use‑case.</div>
          </div>
        </button>
        <button class="sfLegendRow" data-sf-action="open_source_segment" data-sf-payload="reports">
          <span class="sfLegendSwatch" style="background:#38bdf8;"></span>
          <div class="sfLegendText">
            <div class="sfLegendMain">Отчёты/статистика — <b>34</b> (8%)</div>
            <div class="sfLegendDesc">Бенчмарки рынка: тренды, размеры, динамика.</div>
          </div>
        </button>
        <button class="sfLegendRow" data-sf-action="open_source_segment" data-sf-payload="ads">
          <span class="sfLegendSwatch" style="background:#fb7185;"></span>
          <div class="sfLegendText">
            <div class="sfLegendMain">Ad libraries — <b>25</b> (6%)</div>
            <div class="sfLegendDesc">Креативы: что “пушат” в аукционе, какие офферы повторяются.</div>
          </div>
        </button>
        <button class="sfLegendRow" data-sf-action="open_source_segment" data-sf-payload="regulatory">
          <span class="sfLegendSwatch" style="background:#f97316;"></span>
          <div class="sfLegendText">
            <div class="sfLegendMain">Регуляторика — <b>16</b> (4%)</div>
            <div class="sfLegendDesc">Ограничения и риски по claims/каналам/коммуникации.</div>
          </div>
        </button>
        <button class="sfLegendRow" data-sf-action="open_source_segment" data-sf-payload="audience">
          <span class="sfLegendSwatch" style="background:#94a3b8;"></span>
          <div class="sfLegendText">
            <div class="sfLegendMain">Audience insights — <b>10</b> (2%)</div>
            <div class="sfLegendDesc">Аудитория и поведение: интересы, паттерны, темы.</div>
          </div>
        </button>
      </div>

      <div class="chartNote">Список кликабельный: можно открыть реестр источников по типу.</div>
    </div>

    <div class="sfSummary sfSummaryCard">
      <div class="sfSummaryTitle">Summary по миксу источников</div>
      <div class="sfSummaryBody">
        <div class="sfTagRow">
          <span class="sfTag">найдено: 8 563</span>
          <span class="sfTag">обработано: 420</span>
          <span class="sfTag">в очереди: 8 143</span>
        </div>
        <p>Корпус сбалансирован: есть и “жёсткие” источники (отчёты/статистика/регуляторика), и “голос рынка” (UGC/видео), и независимые материалы (web). Это помогает одновременно видеть <b>тренды/цифры</b> и <b>живые триггеры/барьеры</b>, а также отделять реальные паттерны от шумных повторов.</p>
        <ul>
          <li><b>Web</b> → карта тем и формулировок: быстро понимаем “как рынок говорит” и где искать первичные доказательства.</li>
          <li><b>Материалы конкурентов</b> → фиксируем офферы/упаковку, но трактуем как гипотезы (требуют независимого подтверждения).</li>
          <li><b>UGC+видео</b> → сценарии использования, мотивация, причины недоверия и реальные “провалы опыта”.</li>
          <li><b>Отчёты/статистика</b> → дают ориентиры по размеру/динамике рынка и помогают приоритизировать сегменты.</li>
          <li><b>Регуляторика</b> → снижает риск “непроходимых” claims и проблемных каналов коммуникации.</li>
        </ul>
        <p class="help">Дальше этот микс используем как “карту уверенности”: где есть независимые подтверждения и где нужна доборка корпуса.</p>
      </div>
    </div>
  </div>

  <div class="chartNote">Итого: mix помогает понять, на чём “держатся” сегменты/потребности (и где может быть шум).</div>
</div>

<div class="chartCard">
  <div class="chartTitle">Блок 2 — PDF‑отчёты (скачать)</div>
  <div class="sfCardGrid">
    <div class="sfSourceCard sfSourceCardPdf">
      <button type="button" class="sfSourceShot sfSourceShotImg sfSourceShotBtn" data-sf-action="open_doc_analyzer" data-sf-payload="bcg_activewear"><img class="sfSourceThumb" src="Example%20researches/_thumbs/bcg-activewear-trends-report.pdf.png" alt="BCG — Activewear trends report (page 1)" /></button>
      <div class="sfSourceCardBody">
        <div class="sfSourceTitle">BCG — Activewear trends report</div>
        <div class="sfTagRow"><span class="sfTag">report</span><span class="sfTag">activewear</span></div>
        <div class="sfSourceActions">
          <a class="sfInlineLink" href="Example%20researches/bcg-activewear-trends-report.pdf" target="_blank" rel="noopener noreferrer">Открыть</a>
          <a class="sfInlineLink" href="Example%20researches/bcg-activewear-trends-report.pdf" download>Скачать</a>
          <a class="sfInlineLink" href="#" data-sf-action="open_doc_analyzer" data-sf-payload="bcg_activewear">Посмотреть результат</a>
        </div>
      </div>
    </div>
    <div class="sfSourceCard sfSourceCardPdf">
      <button type="button" class="sfSourceShot sfSourceShotImg sfSourceShotBtn" data-sf-action="open_doc_analyzer" data-sf-payload="sporting_goods_2025"><img class="sfSourceThumb" src="Example%20researches/_thumbs/sporting-goods-2025-the-new-balancing-act-turning-uncertainty-into-opportunity-v3.pdf.png" alt="Sporting goods 2025 — report (page 1)" /></button>
      <div class="sfSourceCardBody">
        <div class="sfSourceTitle">Sporting goods 2025 — The new balancing act</div>
        <div class="sfTagRow"><span class="sfTag">report</span><span class="sfTag">market</span></div>
        <div class="sfSourceActions">
          <a class="sfInlineLink" href="Example%20researches/sporting-goods-2025-the-new-balancing-act-turning-uncertainty-into-opportunity-v3.pdf" target="_blank" rel="noopener noreferrer">Открыть</a>
          <a class="sfInlineLink" href="Example%20researches/sporting-goods-2025-the-new-balancing-act-turning-uncertainty-into-opportunity-v3.pdf" download>Скачать</a>
          <a class="sfInlineLink" href="#" data-sf-action="open_doc_analyzer" data-sf-payload="sporting_goods_2025">Посмотреть результат</a>
        </div>
      </div>
    </div>
    <div class="sfSourceCard sfSourceCardPdf">
      <button type="button" class="sfSourceShot sfSourceShotImg sfSourceShotBtn" data-sf-action="open_doc_analyzer" data-sf-payload="time_to_move"><img class="sfSourceThumb" src="Example%20researches/_thumbs/time-to-move-sporting-goods-full-report-2024.pdf.png" alt="Time to move — Sporting goods full report 2024 (page 1)" /></button>
      <div class="sfSourceCardBody">
        <div class="sfSourceTitle">Time to move — Sporting goods full report 2024</div>
        <div class="sfTagRow"><span class="sfTag">report</span><span class="sfTag">full</span></div>
        <div class="sfSourceActions">
          <a class="sfInlineLink" href="Example%20researches/time-to-move-sporting-goods-full-report-2024.pdf" target="_blank" rel="noopener noreferrer">Открыть</a>
          <a class="sfInlineLink" href="Example%20researches/time-to-move-sporting-goods-full-report-2024.pdf" download>Скачать</a>
          <a class="sfInlineLink" href="#" data-sf-action="open_doc_analyzer" data-sf-payload="time_to_move">Посмотреть результат</a>
        </div>
      </div>
    </div>
    <div class="sfSourceCard sfSourceCardPdf">
      <button type="button" class="sfSourceShot sfSourceShotImg sfSourceShotBtn" data-sf-action="open_doc_analyzer" data-sf-payload="mckinsey_wellness"><img class="sfSourceThumb" src="Example%20researches/_thumbs/the-2-trillion-dollar-global-wellness-market-gets-a-millennial-and-gen-z-glow-up_final.pdf.png" alt="Global wellness market report (page 1)" /></button>
      <div class="sfSourceCardBody">
        <div class="sfSourceTitle">Global wellness market — millennial & Gen‑Z glow‑up</div>
        <div class="sfTagRow"><span class="sfTag">report</span><span class="sfTag">wellness</span><span class="sfTag">segment mention: Gen Z</span></div>
        <div class="sfSourceActions">
          <a class="sfInlineLink" href="Example%20researches/the-2-trillion-dollar-global-wellness-market-gets-a-millennial-and-gen-z-glow-up_final.pdf" target="_blank" rel="noopener noreferrer">Открыть</a>
          <a class="sfInlineLink" href="Example%20researches/the-2-trillion-dollar-global-wellness-market-gets-a-millennial-and-gen-z-glow-up_final.pdf" download>Скачать</a>
          <a class="sfInlineLink" href="#" data-sf-action="open_doc_analyzer" data-sf-payload="mckinsey_wellness">Посмотреть результат</a>
        </div>
      </div>
    </div>
    <div class="sfSourceCard sfSourceCardPdf">
      <button type="button" class="sfSourceShot sfSourceShotImg sfSourceShotBtn" data-sf-action="open_doc_analyzer" data-sf-payload="bb_shrinking"><img class="sfSourceThumb" src="Example%20researches/_thumbs/bb_shrinking_to_grow.pdf.png" alt="BB — Shrinking to grow (page 1)" /></button>
      <div class="sfSourceCardBody">
        <div class="sfSourceTitle">BB — Shrinking to grow</div>
        <div class="sfTagRow"><span class="sfTag">report</span><span class="sfTag">strategy</span></div>
        <div class="sfSourceActions">
          <a class="sfInlineLink" href="Example%20researches/bb_shrinking_to_grow.pdf" target="_blank" rel="noopener noreferrer">Открыть</a>
          <a class="sfInlineLink" href="Example%20researches/bb_shrinking_to_grow.pdf" download>Скачать</a>
          <a class="sfInlineLink" href="#" data-sf-action="open_doc_analyzer" data-sf-payload="bb_shrinking">Посмотреть результат</a>
        </div>
      </div>
    </div>
    <div class="sfSourceCard sfSourceCardPdf">
      <div class="sfSourceShot"><div style="font-size:28px; font-weight:950; line-height:1;">+415</div></div>
      <div class="sfSourceCardBody">
        <div class="sfSourceTitle">Дополнительные обработанные источники</div>
        <div class="sfTagRow"><span class="sfTag">web</span><span class="sfTag">ugc</span><span class="sfTag">ads</span><span class="sfTag">stats</span></div>
        <div class="help" style="margin-top:8px;">В отчёте приложено 5 PDF‑примеров. В реальном проекте корпус шире: <b>+415</b> дополнительных источников уже обработано.</div>
        <div class="sfSourceActions">
          <a class="sfInlineLink" href="#" data-sf-action="open_sources_registry">Открыть реестр</a>
        </div>
      </div>
    </div>
  </div>
  <div class="chartNote">Это приложенные PDF‑документы: можно открыть или скачать.</div>
</div>

<div class="vizStack">
  <div class="chartCard">
    <div class="chartTitle">Блок 3 — Группы сегментов: доверие → частота (<span data-sf-seg-groups-count>—</span>)</div>
    <div class="chartNote">Группировка по trust (A/B/C proxy), внутри — по Σ упоминаний. Клик по строке → раскрыть варианты и источники; кнопка «Карточка» → поп‑ап с агрегированными метриками.</div>

    <div data-sf-seg-groups></div>

    <div class="sfScrollY">
      <table class="sfTable">
        <thead>
          <tr>
            <th>Сегмент</th>
            <th>Упоминания (PDF / корпус)</th>
            <th>Контекст (из PDF)</th>
            <th>Evidence</th>
          </tr>
        </thead>
        <tbody data-sf-segments-tbody>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_01" data-sf-name="Скидочные охотники" data-sf-mentions="162" data-sf-context="Покупают на скидках/распродажах, быстро реагируют на промо и ограниченность по времени." data-sf-evidence="A/B • fresh">
            <td><b>Скидочные охотники</b></td>
            <td>162</td>
            <td>“хочу выгодно”, ждут распродажи, важна прозрачность скидки</td>
            <td><span class="sfTag">A/B</span> <span class="sfTag">fresh</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_02" data-sf-name="Импульсные покупки" data-sf-mentions="141" data-sf-context="Покупка “здесь и сейчас”: вдохновение, витрина/лента, быстрый checkout." data-sf-evidence="B • fresh">
            <td><b>Импульсные покупки</b></td>
            <td>141</td>
            <td>вдохновение → быстрый выбор → минимальное трение</td>
            <td><span class="sfTag">B</span> <span class="sfTag">fresh</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_03" data-sf-name="Базовый гардероб / essentials" data-sf-mentions="128" data-sf-context="Покупают базовые вещи регулярно: качество/посадка/размер важнее трендов." data-sf-evidence="A/B • ok">
            <td><b>Базовый гардероб / essentials</b></td>
            <td>128</td>
            <td>“нужны базовые вещи”, важны размеры/посадка/качество ткани</td>
            <td><span class="sfTag">A/B</span> <span class="sfTag">ok</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_04" data-sf-name="Тренд‑ориентированные" data-sf-mentions="117" data-sf-context="Следят за трендами, важны новинки, вдохновение, быстрые поставки." data-sf-evidence="B • fresh">
            <td><b>Тренд‑ориентированные</b></td>
            <td>117</td>
            <td>новинки/коллекции, важен “wow” и частота обновлений</td>
            <td><span class="sfTag">B</span> <span class="sfTag">fresh</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_05" data-sf-name="Оффлайн‑first (примерка)" data-sf-mentions="109" data-sf-context="Предпочитают примерку и оффлайн‑опыт: комфорт, быстро понять размер/посадку." data-sf-evidence="A/B • ok">
            <td><b>Оффлайн‑first (примерка)</b></td>
            <td>109</td>
            <td>важна примерка, ощущение ткани и “понять размер” сразу</td>
            <td><span class="sfTag">A/B</span> <span class="sfTag">ok</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_06" data-sf-name="Онлайн‑first (доставка)" data-sf-mentions="101" data-sf-context="Покупают онлайн: доставка/возвраты/пункты выдачи решают; нужен быстрый и надёжный сервис." data-sf-evidence="A/B • fresh">
            <td><b>Онлайн‑first (доставка)</b></td>
            <td>101</td>
            <td>скорость доставки/возврата = часть продукта</td>
            <td><span class="sfTag">A/B</span> <span class="sfTag">fresh</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_07" data-sf-name="Покупка к событию (дедлайн)" data-sf-mentions="96" data-sf-context="Нужна вещь к событию: дедлайн → высокий intent, нужен предсказуемый результат." data-sf-evidence="B • fresh">
            <td><b>Покупка к событию (дедлайн)</b></td>
            <td>96</td>
            <td>“нужно к выходным/событию”, критичны сроки и предсказуемость</td>
            <td><span class="sfTag">B</span> <span class="sfTag">fresh</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_08" data-sf-name="Мужчины: быстро и без выбора" data-sf-mentions="88" data-sf-context="Минимизируют выбор: понятные наборы, быстрый checkout, повторяемость размеров." data-sf-evidence="B • ok">
            <td><b>Мужчины: быстро и без выбора</b></td>
            <td>88</td>
            <td>нужен “быстрый путь”: готовые наборы/повтор покупки</td>
            <td><span class="sfTag">B</span> <span class="sfTag">ok</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_09" data-sf-name="Подарки" data-sf-mentions="79" data-sf-context="Покупают не себе: высокий риск ошибки по размеру/вкусу → нужны подсказки и возврат." data-sf-evidence="B/C • ok">
            <td><b>Подарки</b></td>
            <td>79</td>
            <td>риск ошибиться → важны подсказки и “безболезненный возврат”</td>
            <td><span class="sfTag">B/C</span> <span class="sfTag">ok</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_10" data-sf-name="Нестандартные размеры (plus/рост)" data-sf-mentions="74" data-sf-context="Сложнее подобрать: нужна уверенность в размере/посадке, подробные замеры и отзывы." data-sf-evidence="A/B • ok">
            <td><b>Нестандартные размеры (plus/рост)</b></td>
            <td>74</td>
            <td>важны точные замеры, честные отзывы, стабильность размеров</td>
            <td><span class="sfTag">A/B</span> <span class="sfTag">ok</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_11" data-sf-name="Gen Z (подростки/студенты)" data-sf-mentions="69" data-sf-context="Ограниченный бюджет + желание выглядеть “в тренде”: важны промо и социальное доказательство." data-sf-evidence="B • fresh">
            <td><b>Gen Z (подростки/студенты)</b></td>
            <td>69</td>
            <td>бюджет + тренды, важны скидки и social proof</td>
            <td><span class="sfTag">B</span> <span class="sfTag">fresh</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_12" data-sf-name="Семейные покупки" data-sf-mentions="62" data-sf-context="Покупают сразу для нескольких людей: важны фильтры, корзина, доставка, возвраты." data-sf-evidence="B • ok">
            <td><b>Семейные покупки</b></td>
            <td>62</td>
            <td>много позиций → важна удобная корзина, объединение доставки</td>
            <td><span class="sfTag">B</span> <span class="sfTag">ok</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_13" data-sf-name="Экономящие время (click&collect)" data-sf-mentions="58" data-sf-context="Минимизируют время на покупку: самовывоз/быстрый возврат, понятный статус заказа." data-sf-evidence="A/B • fresh">
            <td><b>Экономящие время (click&collect)</b></td>
            <td>58</td>
            <td>быстро получить/примерить, важны статусы и самовывоз</td>
            <td><span class="sfTag">A/B</span> <span class="sfTag">fresh</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_14" data-sf-name="Эко/устойчивость" data-sf-mentions="51" data-sf-context="Важно происхождение материалов и “осознанность”: требуют доказательств и прозрачности." data-sf-evidence="A/B • ok">
            <td><b>Эко/устойчивость</b></td>
            <td>51</td>
            <td>важны материалы/прозрачность, нужен доказательный proof‑слой</td>
            <td><span class="sfTag">A/B</span> <span class="sfTag">ok</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_15" data-sf-name="Качество‑ориентированные" data-sf-mentions="48" data-sf-context="Платят за качество: ткань/швы/посадка; нужны детали и гарантии." data-sf-evidence="A/B • ok">
            <td><b>Качество‑ориентированные</b></td>
            <td>48</td>
            <td>нужны доказательства качества (материалы, отзывы, возвраты)</td>
            <td><span class="sfTag">A/B</span> <span class="sfTag">ok</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_16" data-sf-name="Лояльные бренду" data-sf-mentions="44" data-sf-context="Возвращаются за привычным опытом: важны персональные рекомендации и предсказуемость." data-sf-evidence="B • ok">
            <td><b>Лояльные бренду</b></td>
            <td>44</td>
            <td>ожидают “узнавание”, персональные подборки, стабильность размеров</td>
            <td><span class="sfTag">B</span> <span class="sfTag">ok</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_17" data-sf-name="Новые покупатели (нужно доверие)" data-sf-mentions="41" data-sf-context="Сомневаются в посадке/качестве: важны отзывы, гарантии, простые возвраты." data-sf-evidence="A/B • fresh">
            <td><b>Новые покупатели (нужно доверие)</b></td>
            <td>41</td>
            <td>низкое доверие → важны отзывы, гарантии, прозрачные правила</td>
            <td><span class="sfTag">A/B</span> <span class="sfTag">fresh</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_18" data-sf-name="Аксессуары / доп. покупки" data-sf-mentions="38" data-sf-context="Добирают образ: импульс и cross‑sell; важны рекомендации и комплекты." data-sf-evidence="B • ok">
            <td><b>Аксессуары / доп. покупки</b></td>
            <td>38</td>
            <td>cross‑sell “дособрать образ”, важны комплекты и подбор</td>
            <td><span class="sfTag">B</span> <span class="sfTag">ok</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_19" data-sf-name="Сезонные покупки" data-sf-mentions="36" data-sf-context="Пики спроса по сезонам: важны своевременные коллекции и логистика." data-sf-evidence="B • ok">
            <td><b>Сезонные покупки</b></td>
            <td>36</td>
            <td>“нужно к сезону”, важны сроки и наличие размеров</td>
            <td><span class="sfTag">B</span> <span class="sfTag">ok</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_20" data-sf-name="Millennials" data-sf-mentions="32" data-sf-context="Сегмент 25–40: “wellness‑driven” поведение, важны привычки и self‑improvement." data-sf-evidence="B • ok">
            <td><b>Millennials</b></td>
            <td>32</td>
            <td>“здоровые привычки”, self‑improvement, важны мотивация и понятные ритуалы</td>
            <td><span class="sfTag">B</span> <span class="sfTag">ok</span></td>
          </tr>
          <tr class="sfRowLink" data-sf-action="open_segment_detail" data-sf-payload="seg_21" data-sf-name="Офис / casual (dress‑code)" data-sf-mentions="29" data-sf-context="Нужны вещи под правила/дресс‑код: важны подборы и уверенность в стиле." data-sf-evidence="B • ok">
            <td><b>Офис / casual (dress‑code)</b></td>
            <td>29</td>
            <td>подбор “под правила”, важны комплекты и стиль‑подсказки</td>
            <td><span class="sfTag">B</span> <span class="sfTag">ok</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <!--
  <div class="chartCard">
    <div class="chartTitle">Блок 4 — Дифференциация сегментов: частота × доверие (<span data-sf-segment-matrix-count>—</span>)</div>
    <div class="chartNote">Ось X — <b>частота упоминаний</b> (редко → часто, по корпусу PDF). Ось Y — <b>доверие/evidence</b> (высокое → низкое, proxy). Наведи на точку → подсказка, клик → карточка сегмента.</div>

    <div class="matrix2x2 matrixLarge" data-sf-segment-matrix>
      <button class="matrixPoint" style="left:86%; top:18%;" data-label="Скидки" data-sf-action="open_segment_detail" data-sf-payload="seg_01" data-sf-name="Скидочные охотники" data-sf-mentions="162" data-sf-context="Покупают на скидках/распродажах, быстро реагируют на промо и ограниченность по времени." data-sf-evidence="A/B • fresh"></button>
      <button class="matrixPoint" style="left:80%; top:22%;" data-label="Импульс" data-sf-action="open_segment_detail" data-sf-payload="seg_02" data-sf-name="Импульсные покупки" data-sf-mentions="141" data-sf-context="Покупка “здесь и сейчас”: вдохновение, витрина/лента, быстрый checkout." data-sf-evidence="B • fresh"></button>
      <button class="matrixPoint" style="left:74%; top:28%;" data-label="База" data-sf-action="open_segment_detail" data-sf-payload="seg_03" data-sf-name="Базовый гардероб / essentials" data-sf-mentions="128" data-sf-context="Покупают базовые вещи регулярно: качество/посадка/размер важнее трендов." data-sf-evidence="A/B • ok"></button>
      <button class="matrixPoint" style="left:68%; top:26%;" data-label="Тренды" data-sf-action="open_segment_detail" data-sf-payload="seg_04" data-sf-name="Тренд‑ориентированные" data-sf-mentions="117" data-sf-context="Следят за трендами, важны новинки, вдохновение, быстрые поставки." data-sf-evidence="B • fresh"></button>
      <button class="matrixPoint" style="left:62%; top:32%;" data-label="Оффлайн" data-sf-action="open_segment_detail" data-sf-payload="seg_05" data-sf-name="Оффлайн‑first (примерка)" data-sf-mentions="109" data-sf-context="Предпочитают примерку и оффлайн‑опыт: комфорт, быстро понять размер/посадку." data-sf-evidence="A/B • ok"></button>
      <button class="matrixPoint" style="left:66%; top:22%;" data-label="Онлайн" data-sf-action="open_segment_detail" data-sf-payload="seg_06" data-sf-name="Онлайн‑first (доставка)" data-sf-mentions="101" data-sf-context="Покупают онлайн: доставка/возвраты/пункты выдачи решают; нужен быстрый и надёжный сервис." data-sf-evidence="A/B • fresh"></button>
      <button class="matrixPoint" style="left:58%; top:28%;" data-label="Дедлайн" data-sf-action="open_segment_detail" data-sf-payload="seg_07" data-sf-name="Покупка к событию (дедлайн)" data-sf-mentions="96" data-sf-context="Нужна вещь к событию: дедлайн → высокий intent, нужен предсказуемый результат." data-sf-evidence="B • fresh"></button>
      <button class="matrixPoint" style="left:55%; top:40%;" data-label="Мужчины" data-sf-action="open_segment_detail" data-sf-payload="seg_08" data-sf-name="Мужчины: быстро и без выбора" data-sf-mentions="88" data-sf-context="Минимизируют выбор: понятные наборы, быстрый checkout, повторяемость размеров." data-sf-evidence="B • ok"></button>
      <button class="matrixPoint" style="left:50%; top:56%;" data-label="Подарки" data-sf-action="open_segment_detail" data-sf-payload="seg_09" data-sf-name="Подарки" data-sf-mentions="79" data-sf-context="Покупают не себе: высокий риск ошибки по размеру/вкусу → нужны подсказки и возврат." data-sf-evidence="B/C • ok"></button>
      <button class="matrixPoint" style="left:44%; top:36%;" data-label="Размеры" data-sf-action="open_segment_detail" data-sf-payload="seg_10" data-sf-name="Нестандартные размеры (plus/рост)" data-sf-mentions="74" data-sf-context="Сложнее подобрать: нужна уверенность в размере/посадке, подробные замеры и отзывы." data-sf-evidence="A/B • ok"></button>
      <button class="matrixPoint" style="left:47%; top:30%;" data-label="Gen Z" data-sf-action="open_segment_detail" data-sf-payload="seg_11" data-sf-name="Gen Z (подростки/студенты)" data-sf-mentions="69" data-sf-context="Ограниченный бюджет + желание выглядеть “в тренде”: важны промо и социальное доказательство." data-sf-evidence="B • fresh"></button>
      <button class="matrixPoint" style="left:40%; top:44%;" data-label="Семья" data-sf-action="open_segment_detail" data-sf-payload="seg_12" data-sf-name="Семейные покупки" data-sf-mentions="62" data-sf-context="Покупают сразу для нескольких людей: важны фильтры, корзина, доставка, возвраты." data-sf-evidence="B • ok"></button>
      <button class="matrixPoint" style="left:38%; top:28%;" data-label="C&C" data-sf-action="open_segment_detail" data-sf-payload="seg_13" data-sf-name="Экономящие время (click&collect)" data-sf-mentions="58" data-sf-context="Минимизируют время на покупку: самовывоз/быстрый возврат, понятный статус заказа." data-sf-evidence="A/B • fresh"></button>
      <button class="matrixPoint" style="left:32%; top:38%;" data-label="Эко" data-sf-action="open_segment_detail" data-sf-payload="seg_14" data-sf-name="Эко/устойчивость" data-sf-mentions="51" data-sf-context="Важно происхождение материалов и “осознанность”: требуют доказательств и прозрачности." data-sf-evidence="A/B • ok"></button>
      <button class="matrixPoint" style="left:30%; top:34%;" data-label="Качество" data-sf-action="open_segment_detail" data-sf-payload="seg_15" data-sf-name="Качество‑ориентированные" data-sf-mentions="48" data-sf-context="Платят за качество: ткань/швы/посадка; нужны детали и гарантии." data-sf-evidence="A/B • ok"></button>
      <button class="matrixPoint" style="left:36%; top:52%;" data-label="Лояльные" data-sf-action="open_segment_detail" data-sf-payload="seg_16" data-sf-name="Лояльные бренду" data-sf-mentions="44" data-sf-context="Возвращаются за привычным опытом: важны персональные рекомендации и предсказуемость." data-sf-evidence="B • ok"></button>
      <button class="matrixPoint" style="left:28%; top:22%;" data-label="Новые" data-sf-action="open_segment_detail" data-sf-payload="seg_17" data-sf-name="Новые покупатели (нужно доверие)" data-sf-mentions="41" data-sf-context="Сомневаются в посадке/качестве: важны отзывы, гарантии, простые возвраты." data-sf-evidence="A/B • fresh"></button>
      <button class="matrixPoint" style="left:24%; top:46%;" data-label="Аксесс." data-sf-action="open_segment_detail" data-sf-payload="seg_18" data-sf-name="Аксессуары / доп. покупки" data-sf-mentions="38" data-sf-context="Добирают образ: импульс и cross‑sell; важны рекомендации и комплекты." data-sf-evidence="B • ok"></button>
      <button class="matrixPoint" style="left:22%; top:40%;" data-label="Сезон" data-sf-action="open_segment_detail" data-sf-payload="seg_19" data-sf-name="Сезонные покупки" data-sf-mentions="36" data-sf-context="Пики спроса по сезонам: важны своевременные коллекции и логистика." data-sf-evidence="B • ok"></button>
      <button class="matrixPoint" style="left:18%; top:60%;" data-label="Millennials" data-sf-action="open_segment_detail" data-sf-payload="seg_20" data-sf-name="Millennials" data-sf-mentions="32" data-sf-context="Сегмент 25–40: “wellness‑driven” поведение, важны привычки и self‑improvement." data-sf-evidence="B • ok"></button>
      <button class="matrixPoint" style="left:16%; top:48%;" data-label="Офис" data-sf-action="open_segment_detail" data-sf-payload="seg_21" data-sf-name="Офис / casual (dress‑code)" data-sf-mentions="29" data-sf-context="Нужны вещи под правила/дресс‑код: важны подборы и уверенность в стиле." data-sf-evidence="B • ok"></button>

      <div class="sfMatrixLegend">
        <span class="sfMatrixLegendItem sfQuadBest">Сильные (часто + доверие)</span>
        <span class="sfMatrixLegendItem sfQuadNoisy">Шум (часто + низк. доверие)</span>
        <span class="sfMatrixLegendItem sfQuadNiche">Ниша (редко + доверие)</span>
        <span class="sfMatrixLegendItem sfQuadLow">Слабые (редко + низк. доверие)</span>
      </div>
      <div class="matrixAxisX"><span>Редко (частота)</span><span>Часто (частота)</span></div>
      <div class="matrixAxisY"><span>Высокое (доверие)</span><span>Низкое (доверие)</span></div>
    </div>
  </div>
  -->

  <div class="chartCard">
    <div class="chartTitle">Блок 4 — Карта групп сегментов: частота × доверие (<span data-sf-seg-viz-count>—</span>)</div>
    <div class="chartNote">X = <b>Σ упоминаний</b> (по PDF‑корпусу), Y = <b>доверие/evidence</b> (proxy), размер = <b>кол‑во документов</b>. Наведи → подсказка, клик → карточка группы.</div>
    <div data-sf-seg-viz></div>
  </div>

  <div class="chartCard" style="display:none">
    <div class="chartTitle">Блок 4B — Confidence bands: доверие → частота (группы) (<span data-sf-seg-bands-count>—</span>)</div>
    <div class="chartNote">Группируем по <b>trust</b> (A/B/C proxy), внутри сортируем по <b>Σ упоминаний</b>. Bar = частота, клик → карточка группы.</div>
    <div data-sf-seg-bands></div>
  </div>

  <div class="chartCard" style="display:none">
    <div class="chartTitle">Блок 4C — Карточки сегментов: метрики + контекст (<span data-sf-seg-cards-count>—</span>)</div>
    <div class="chartNote">Быстрый обзор: в PDF / Σ, docs, trust (proxy). Клик по карточке → карточка сегмента.</div>
    <div data-sf-seg-cards></div>
  </div>
</div>
