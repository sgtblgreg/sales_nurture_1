<div class="reportHeader">
  <div>
    <div class="reportTitle">Touch 03 — Спрос, триггеры и доверие (market signals)</div>
    <div class="reportSub">DEMO • Day 24 • цель: показать, “что люди реально ищут” и где чаще всего ломается конверсия до оплаты</div>
  </div>
  <div class="metaChips">
    <span class="chip"><span class="chipLabel">Company</span>{{company}}</span>
    <span class="chip"><span class="chipLabel">Geo</span>{{geo}}</span>
    <span class="chip"><span class="chipLabel">Category</span>{{industry}}</span>
  </div>
</div>

<div class="kpiGrid">
  <div class="kpiCard">
    <div class="kpiLabel">Триггеры спроса</div>
    <div class="kpiValue">Дедлайн + эмоция</div>
    <div class="kpiNote">“К лету / к событию / к фото” — самый частый драйвер “сейчас или никогда”.</div>
  </div>
  <div class="kpiCard">
    <div class="kpiLabel">Главный барьер</div>
    <div class="kpiValue">Скепсис</div>
    <div class="kpiNote">Рынок перегрет обещаниями → доказательства становятся обязательными.</div>
  </div>
  <div class="kpiCard">
    <div class="kpiLabel">Быстрый тест</div>
    <div class="kpiValue">Proof‑слой + “первая победа”</div>
    <div class="kpiNote">Улучшает C1 чаще, чем добавление новых тренировок.</div>
  </div>
</div>

<div class="vizGrid">
  <div class="chartCard">
    <div class="chartTitle">Exhibit 1 — Темы спроса (поиск) • индекс</div>
    <div class="barChart">
      <div class="barItem">
        <div class="barLabel">“похудеть дома без зала”</div>
        <div class="barTrack"><div class="barFill" style="width: 92%"></div></div>
        <div class="barValue">very high</div>
      </div>
      <div class="barItem">
        <div class="barLabel">“к лету / к событию”</div>
        <div class="barTrack"><div class="barFill" style="width: 78%"></div></div>
        <div class="barValue">high</div>
      </div>
      <div class="barItem">
        <div class="barLabel">“как не сорваться”</div>
        <div class="barTrack"><div class="barFill" style="width: 66%"></div></div>
        <div class="barValue">med</div>
      </div>
      <div class="barItem">
        <div class="barLabel">“питание + тренировки”</div>
        <div class="barTrack"><div class="barFill" style="width: 58%"></div></div>
        <div class="barValue">med</div>
      </div>
      <div class="barItem">
        <div class="barLabel">“мотивация / привычка”</div>
        <div class="barTrack"><div class="barFill" style="width: 53%"></div></div>
        <div class="barValue">med</div>
      </div>
    </div>
    <div class="chartNote">Задача: понять, какие “темы” формируют спрос и как упаковать оффер под контекст (а не под абстрактную демографию).</div>
  </div>
  <div class="chartCard">
    <div class="chartTitle">Exhibit 2 — Что ломает доверие (UGC/отзывы)</div>
    <ul>
      <li><b>Слишком рекламно</b> → “обещают чудо” → рост скепсиса.</li>
      <li><b>Сложный старт</b> → “не понимаю что делать” → ранние отказы.</li>
      <li><b>Нет поддержки</b> → “сорвался на 3‑й день” → падение retention.</li>
    </ul>
    <div class="chartNote"><span class="redact">██████████████████████████████████████████</span> В полном проекте добавляем `evidence` (цитаты/скрины/цифры) и валидируем по актуальности.</div>
  </div>
</div>

<div class="chartCard">
  <div class="chartTitle">Exhibit 3 — 7‑дневный эксперимент‑пакет (без тяжёлой разработки)</div>
  <ul>
    <li><b>Экран 1</b>: обещание + proof (кто, какой результат, за сколько, с оговорками).</li>
    <li><b>Онбординг</b>: “первая победа” за 7–10 минут (микро‑прогресс).</li>
    <li><b>Креативы</b>: 3 угла — “к дедлайну” vs “без срывов” vs “без зала”.</li>
  </ul>
  <div class="chartNote">Методология (dependency map): `analysis_search_demand_coverage`, `analysis_seasonality_and_demand_cycles`, `analysis_claims_and_skepticism`.</div>
</div>
