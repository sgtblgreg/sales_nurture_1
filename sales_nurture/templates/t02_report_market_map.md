<div class="reportHeader">
  <div>
    <div class="reportTitle">Touch 02 — Карта спроса (importance): <span data-sf-t02-seg-count>—</span> сегментов × <span data-sf-t02-need-count>—</span> потребностей</div>
    <div class="reportSub">День 10 • цель: показать структуру спроса по сегментам/потребностям и собрать связки Segment → Need → Functions</div>
  </div>
</div>

<div class="callout">
  <div class="calloutTitle">Summary с прошлого касания (Touch 01)</div>
  <div class="calloutBody">
    <ul>
      <li>Мы собрали и обработали <b>420</b> источников (из <b>8 563</b> найденных) и оценили качество корпуса (B / 72 из 100).</li>
      <li>Собрали каталоги (первый срез): <b><span data-sf-t02-seg-count>—</span> сегментов</b> и <b><span data-sf-t02-need-count>—</span> потребностей</b> + функции/каналы/триггеры (в teaser часть скрыта).</li>
      <li>В этом касании показываем <b>importance‑карту Segment×Need</b> (включая группировки) и “общие vs специфичные” потребности — чтобы перейти от списка к стратегии.</li>
    </ul>
  </div>
</div>

<div class="kpiGrid">
  <div class="kpiCard">
    <div class="kpiLabel">Корпус (короткий срез)</div>
    <div class="kpiValue">420 обработано • 8 563 найдено</div>
    <div class="kpiNote">В очереди (найдено, но не обработано): <b>8 143</b>. В полном проекте корпус обновляется и расширяется мониторингом.</div>
    <div class="sfKpiLinks">
      <a class="sfInlineLink" href="https://example.com/source_repository" target="_blank" rel="noopener noreferrer">Хранилище</a>
      <button class="sfInlineBtn" data-sf-action="open_sources_registry">Открыть таблицу источников</button>
    </div>
  </div>
  <div class="kpiCard">
    <div class="kpiLabel">Каталоги (извлечено)</div>
    <div class="kpiValue">Segments <span data-sf-t02-seg-count>—</span> • Needs <span data-sf-t02-need-count>—</span></div>
    <div class="kpiNote">Functions 126 • Channels 21 • Competitors 18 • Barriers 16 • Triggers 12 (часть скрыта в teaser‑версии).</div>
  </div>
  <div class="kpiCard">
    <div class="kpiLabel">Карта спроса (в отчёте)</div>
    <div class="kpiValue">Segments × Needs + importance</div>
    <div class="kpiNote">Цель: увидеть пересечения и “общие vs специфичные” потребности, чтобы собрать связки Segment → Need → Functions.</div>
  </div>
</div>

<div class="vizGrid">
    <div class="chartCard">
      <div class="chartTitle">Блок 0 — Сегменты (каталог → кластеры)</div>
      <div class="chartNote">Список собран из Touch 01: берём все найденные сегменты из PDF‑корпуса и кластеризуем формулировки в группы. Клик по строке → где встречается в PDF + trust (proxy).</div>
      <div class="sfScrollY">
        <table class="sfTable" data-sf-t02-segments-table>
        <thead>
          <tr>
            <th>№</th>
            <th>Сегмент (группа)</th>
            <th>Σ упоминаний</th>
            <th>Типичный контекст</th>
            <th>Evidence</th>
          </tr>
        </thead>
        <tbody data-sf-t02-segments-tbody></tbody>
      </table>
    </div>
  </div>

  <div class="chartCard">
    <div class="chartTitle">Блок 0 — Потребности (каталог → кластеры)</div>
    <div class="chartNote">Собираем потребности из всех источников Touch 01 и объединяем близкие формулировки в группы (как и сегменты). N‑коды используются в матрице Segment×Need и в блоке 2.</div>
    <div class="sfScrollY">
      <table class="sfTable" data-sf-t02-needs-table>
        <thead>
          <tr>
            <th>№</th>
            <th>Потребность (группа)</th>
            <th>Σ упоминаний</th>
            <th>Что это значит</th>
          </tr>
        </thead>
        <tbody data-sf-t02-needs-tbody></tbody>
      </table>
    </div>
  </div>
</div>

<div class="chartCard">
  <div class="chartTitle">Блок 1 — Карта спроса: Segment × Need (importance + группы)</div>
  <div class="chartNote">Сегменты по горизонтали, потребности по вертикали. Вверху/слева идут агрегированные <b>группы</b> (чтобы убрать лингвистический шум). Ячейка = <b>importance 0–100</b> + класс (Core/Secondary/Niche/Irrelevant). В демо матрица ограничивается top‑trust (proxy) для читабельности.</div>
  <div class="heatTableWrap heatTableWrapLimited" data-sf-matrix="segment_need_v1" data-sf-seg-max="12" data-sf-need-max="16" data-sf-rows="21" data-sf-cols="52"></div>
  <div class="chartNote">В полном проекте каждая ячейка связывается с evidence (источники) и используется для сборки messaging и функций.</div>
</div>

<div class="expertOnly">
<div class="chartCard">
  <div class="chartTitle">Блок 1 — Карта спроса: Segment × Need (важность + “как закрывается”)</div>
  <div class="heatTableWrap">
    <table class="heatTable">
      <thead>
        <tr>
          <th class="heatRowHeader">Группа потребностей</th>
          <th>Новички<br><span style="opacity:.75">(после перерыва)</span></th>
          <th>Занятые<br><span style="opacity:.75">(10–20 мин)</span></th>
          <th>После родов<br><span style="opacity:.75">(безопасно)</span></th>
          <th>35+ здоровье<br><span style="opacity:.75">(спина)</span></th>
          <th>К лету<br><span style="opacity:.75">(срок)</span></th>
          <th>Срывы/скепсис<br><span style="opacity:.75">(proof)</span></th>
          <th>Итого по группе</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th class="heatRowHeader">1) Простой старт + план</th>
          <td class="heatCell heat5">
            <div class="heatTop"><span class="heatValue">94%</span><span class="heatTag">план 8 недель</span></div>
            <div class="heatNote">“С нуля” → нужен понятный старт и ощущение контроля.</div>
          </td>
          <td class="heatCell heat4">
            <div class="heatTop"><span class="heatValue">82%</span><span class="heatTag">10–20 мин</span></div>
            <div class="heatNote">Короткие “слоты” + заранее готовые сценарии.</div>
          </td>
          <td class="heatCell heat4">
            <div class="heatTop"><span class="heatValue">79%</span><span class="heatTag">программы</span></div>
            <div class="heatNote">План должен учитывать ограничения и темп.</div>
          </td>
          <td class="heatCell heat3">
            <div class="heatTop"><span class="heatValue">68%</span><span class="heatTag">лёгкий режим</span></div>
            <div class="heatNote">Старт “без травм” и без перегруза.</div>
          </td>
          <td class="heatCell heat4">
            <div class="heatTop"><span class="heatValue">86%</span><span class="heatTag">челлендж</span></div>
            <div class="heatNote">План “до даты” + видимые вехи.</div>
          </td>
          <td class="heatCell heat3">
            <div class="heatTop"><span class="heatValue">71%</span><span class="heatTag">первые победы</span></div>
            <div class="heatNote">Нужны быстрые “wins” и понятная траектория.</div>
          </td>
          <td class="heatCell heat5">
            <div class="heatTop"><span class="heatValue">80%</span><span class="heatTag">avg</span></div>
            <div class="heatNote"><b>Общая потребность.</b> Почти у всех сегментов.</div>
          </td>
        </tr>

        <tr>
          <th class="heatRowHeader">2) Быстрый прогресс</th>
          <td class="heatCell heat3">
            <div class="heatTop"><span class="heatValue">66%</span><span class="heatTag">замеры</span></div>
            <div class="heatNote">Важно видеть изменения “раньше зеркала”.</div>
          </td>
          <td class="heatCell heat4">
            <div class="heatTop"><span class="heatValue">84%</span><span class="heatTag">трекер</span></div>
            <div class="heatNote">Прогресс = мотиватор, иначе “не окупается время”.</div>
          </td>
          <td class="heatCell heat2">
            <div class="heatTop"><span class="heatValue">55%</span><span class="heatTag">мягко</span></div>
            <div class="heatNote">Результат важен, но безопасность выше.</div>
          </td>
          <td class="heatCell heat3">
            <div class="heatTop"><span class="heatValue">63%</span><span class="heatTag">сила/осанка</span></div>
            <div class="heatNote">Прогресс часто про самочувствие, а не вес.</div>
          </td>
          <td class="heatCell heat5">
            <div class="heatTop"><span class="heatValue">92%</span><span class="heatTag">“к дате”</span></div>
            <div class="heatNote">Время‑ограниченный мотиватор усиливает спрос.</div>
          </td>
          <td class="heatCell heat4">
            <div class="heatTop"><span class="heatValue">83%</span><span class="heatTag">доказать</span></div>
            <div class="heatNote">Нужен “объективный прогресс”, иначе скепсис.</div>
          </td>
          <td class="heatCell heat4">
            <div class="heatTop"><span class="heatValue">74%</span><span class="heatTag">avg</span></div>
            <div class="heatNote">Сильная общая потребность, но разная форма доказательств.</div>
          </td>
        </tr>

        <tr>
          <th class="heatRowHeader">3) Дисциплина + поддержка</th>
          <td class="heatCell heat5">
            <div class="heatTop"><span class="heatValue">91%</span><span class="heatTag">сообщества</span></div>
            <div class="heatNote">Нужен внешний “держатель” привычки.</div>
          </td>
          <td class="heatCell heat3">
            <div class="heatTop"><span class="heatValue">64%</span><span class="heatTag">push</span></div>
            <div class="heatNote">Авто‑пинги + короткие ритуалы.</div>
          </td>
          <td class="heatCell heat3">
            <div class="heatTop"><span class="heatValue">61%</span><span class="heatTag">support</span></div>
            <div class="heatNote">Поддержка снижает риск “сойти с дистанции”.</div>
          </td>
          <td class="heatCell heat2">
            <div class="heatTop"><span class="heatValue">52%</span><span class="heatTag">осторожно</span></div>
            <div class="heatNote">Здоровье важнее “геймификации”.</div>
          </td>
          <td class="heatCell heat4">
            <div class="heatTop"><span class="heatValue">79%</span><span class="heatTag">челлендж‑группа</span></div>
            <div class="heatNote">Дедлайн + группа = сильная механика.</div>
          </td>
          <td class="heatCell heat5">
            <div class="heatTop"><span class="heatValue">95%</span><span class="heatTag">proof+coach</span></div>
            <div class="heatNote">Поддержка = доверие, иначе сегмент “не верит”.</div>
          </td>
          <td class="heatCell heat4">
            <div class="heatTop"><span class="heatValue">74%</span><span class="heatTag">avg</span></div>
            <div class="heatNote"><b>Общая потребность</b> с разной “упаковкой” по сегментам.</div>
          </td>
        </tr>

        <tr>
          <th class="heatRowHeader">4) Безопасность / здоровье</th>
          <td class="heatCell heat1">
            <div class="heatTop"><span class="heatValue">28%</span><span class="heatTag">low</span></div>
            <div class="heatNote">Для новичков важнее простота, чем медицина.</div>
          </td>
          <td class="heatCell heat1">
            <div class="heatTop"><span class="heatValue">22%</span><span class="heatTag">low</span></div>
            <div class="heatNote">Занятым важнее “экономия времени”.</div>
          </td>
          <td class="heatCell heat5">
            <div class="heatTop"><span class="heatValue">94%</span><span class="heatTag">ограничения</span></div>
            <div class="heatNote">Критично: противопоказания, темп, экспертность.</div>
          </td>
          <td class="heatCell heat5">
            <div class="heatTop"><span class="heatValue">92%</span><span class="heatTag">спина/суставы</span></div>
            <div class="heatNote">Чёткий value: “не навредит”, улучшит самочувствие.</div>
          </td>
          <td class="heatCell heat2">
            <div class="heatTop"><span class="heatValue">41%</span><span class="heatTag">умеренно</span></div>
            <div class="heatNote">Если дедлайн — могут игнорировать осторожность.</div>
          </td>
          <td class="heatCell heat3">
            <div class="heatTop"><span class="heatValue">62%</span><span class="heatTag">доверие</span></div>
            <div class="heatNote">Скепсис усиливает требования к доказательствам.</div>
          </td>
          <td class="heatCell heat3">
            <div class="heatTop"><span class="heatValue">56%</span><span class="heatTag">avg</span></div>
            <div class="heatNote">Сильно “выскакивает” в 2 сегментах → <b>специфичная</b>.</div>
          </td>
        </tr>

        <tr>
          <th class="heatRowHeader">5) Локальные ограничения (режим/послеродовое)</th>
          <td class="heatCell heat0">
            <div class="heatTop"><span class="heatValue">—</span><span class="heatTag">n/a</span></div>
            <div class="heatNote">Не актуально как отдельный драйвер.</div>
          </td>
          <td class="heatCell heat0">
            <div class="heatTop"><span class="heatValue">—</span><span class="heatTag">n/a</span></div>
            <div class="heatNote">Не актуально как отдельный драйвер.</div>
          </td>
          <td class="heatCell heat5">
            <div class="heatTop"><span class="heatValue">98%</span><span class="heatTag">после родов</span></div>
            <div class="heatNote">Сегмент требует специализированного продукта.</div>
          </td>
          <td class="heatCell heat1">
            <div class="heatTop"><span class="heatValue">36%</span><span class="heatTag">ограничения</span></div>
            <div class="heatNote">Есть ограничения, но они другие (здоровье).</div>
          </td>
          <td class="heatCell heat1">
            <div class="heatTop"><span class="heatValue">19%</span><span class="heatTag">low</span></div>
            <div class="heatNote">Дедлайн важнее ограничений.</div>
          </td>
          <td class="heatCell heat1">
            <div class="heatTop"><span class="heatValue">33%</span><span class="heatTag">low</span></div>
            <div class="heatNote">Скепсис — это не про режим.</div>
          </td>
          <td class="heatCell heat2">
            <div class="heatTop"><span class="heatValue">31%</span><span class="heatTag">avg</span></div>
            <div class="heatNote"><b>Специфичная потребность</b> (сильно “в одном сегменте”).</div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <div class="chartNote">В “полной” версии: больше сегментов/потребностей + кликабельные источники на уровне ячеек.</div>
</div>
</div>

<details class="sfDisclosure">
  <summary class="sfDisclosureSummary">Показать доп. аналитику (Block 2 + Summary)</summary>
  <div class="vizGrid" style="margin-top:12px;">
    <div class="chartCard">
      <div class="chartTitle">Блок 2 — Однородность потребностей по сегментам</div>
      <div class="chartNote">Для каждой потребности считаем важность по всем сегментам из блока 1 и смотрим <b>coverage</b>: сколько сегментов дают ≥ Secondary (score ≥ 60). Это помогает отличать “общие” нужды от специфичных.</div>
      <div data-sf-t02-need-homogeneity></div>
    </div>

    <div class="chartCard">
      <div class="chartTitle">Summary — общие vs специфичные потребности</div>
      <div data-sf-t02-need-summary></div>
    </div>
  </div>
</details>

<div class="chartCard">
  <div class="chartTitle">Блок 3 — Креативы конкурентов (fitness apps) по потребностям (примеры)</div>
  <div class="chartNote">Библиотека реальных креативов из ad libraries / стора / лендингов. В демо — заглушки. Чтобы подставить скриншот, добавьте <code>data-sf-img</code> (и опционально <code>data-sf-img-alt</code>) на карточку/кнопку.</div>
  <div class="sfCardGrid">
    <a class="sfSourceCard" href="#" data-sf-action="open_creative_example" data-sf-title="Nike Training Club — быстрый старт" data-sf-kicker="Nike Training Club • Quick start" data-sf-headline="Начните план на 4 недели сегодня" data-sf-body="Тренировки под цель, уровень и время. Первый результат — уже на этой неделе." data-sf-cta="Начать бесплатно" data-sf-need="Быстрый старт (онбординг)" data-sf-segment="Новички / возвращающиеся" data-sf-functions="Опрос цели и уровня|Готовые планы|Первый workout за 2 минуты">
      <div class="sfSourceShot">CREATIVE</div>
      <div class="sfSourceCardBody">
        <div class="sfSourceTitle">Nike Training Club: “План на 4 недели”</div>
        <div class="sfTagRow"><span class="sfTag">need: quick start</span><span class="sfTag">onboarding</span></div>
      </div>
    </a>

    <a class="sfSourceCard" href="#" data-sf-action="open_creative_example" data-sf-title="Freeletics — персональный план" data-sf-kicker="Freeletics • Personalization" data-sf-headline="AI‑коуч подстраивает план под вас" data-sf-body="Сложность и нагрузка адаптируются по фидбеку и прогрессу." data-sf-cta="Собрать план" data-sf-need="Персонализация (план под цель)" data-sf-segment="Goal‑driven / self‑optimizers" data-sf-functions="Адаптивная программа|Фидбек после тренировки|Автопрогрессия нагрузки">
      <div class="sfSourceShot">CREATIVE</div>
      <div class="sfSourceCardBody">
        <div class="sfSourceTitle">Freeletics: “AI‑Coach”</div>
        <div class="sfTagRow"><span class="sfTag">need: personalization</span><span class="sfTag">plan</span></div>
      </div>
    </a>

    <a class="sfSourceCard" href="#" data-sf-action="open_creative_example" data-sf-title="7 Minute Workout — нет времени" data-sf-kicker="7 Minute • Time efficiency" data-sf-headline="7 минут в день — и вы в форме" data-sf-body="Короткие тренировки без оборудования: дома, в любом месте." data-sf-cta="Попробовать" data-sf-need="Быстро и без времени" data-sf-segment="Занятые / “нет времени”" data-sf-functions="7‑мин программы|Фильтр по времени|Без оборудования">
      <div class="sfSourceShot">CREATIVE</div>
      <div class="sfSourceCardBody">
        <div class="sfSourceTitle">7 Minute: “7 минут в день”</div>
        <div class="sfTagRow"><span class="sfTag">need: time</span><span class="sfTag">home</span></div>
      </div>
    </a>

    <a class="sfSourceCard" href="#" data-sf-action="open_creative_example" data-sf-title="FitOn — мотивация/комьюнити" data-sf-kicker="FitOn • Motivation" data-sf-headline="Челлендж на 14 дней — вместе проще" data-sf-body="Ставьте цели, отмечайте прогресс и тренируйтесь с друзьями." data-sf-cta="Присоединиться" data-sf-need="Мотивация и привычка" data-sf-segment="Социальные / “нужен толчок”" data-sf-functions="Челленджи|Streak/бейджи|Друзья/группы">
      <div class="sfSourceShot">CREATIVE</div>
      <div class="sfSourceCardBody">
        <div class="sfSourceTitle">FitOn: “14‑day challenge”</div>
        <div class="sfTagRow"><span class="sfTag">need: motivation</span><span class="sfTag">community</span></div>
      </div>
    </a>
  </div>
</div>

<div class="chartCard">
  <div class="chartTitle">Блок 4 — Потребности → функции продукта → креативы конкурентов</div>
  <div class="chartNote">Фокус: показать, как <b>потребность</b> превращается в <b>функции продукта</b> и в конкретный <b>креатив</b> (обычно под самый “яркий” сегмент внутри нужды). Ниже — пример под кейс подписочного фитнес‑приложения.</div>

  <div class="sfHScroll">
    <div class="sfNeedCard">
      <div class="sfNeedTitle">Быстрый старт (ярко у новичков)</div>
      <div class="sfNeedDesc">Человек согласен попробовать — но не готов разбираться. Нужно довести до первой тренировки за 2–3 минуты.</div>
      <div class="sfTagRow"><span class="sfTag">segment: beginners</span><span class="sfTag">functions: 4</span></div>
      <ul>
        <li>Опрос: цель/уровень/время/ограничения</li>
        <li>Готовые планы (8 недель / 4 недели)</li>
        <li>Первый workout за 2–3 минуты (минимум трения)</li>
        <li>Expectations: “как работает план”</li>
      </ul>
      <div class="sfCreativeMock">
        <div class="sfCreativeKicker">Nike Training Club • Quick start</div>
        <div class="sfCreativeHeadline">Начните сегодня: план на 4 недели</div>
        <div class="sfCreativeBody">Подберите цель и уровень — и получите тренировки на каждый день.</div>
        <div class="sfCreativeCta">Начать бесплатно</div>
      </div>
      <button class="sfInlineBtn" data-sf-action="open_creative_example" data-sf-title="Креатив — Быстрый старт" data-sf-kicker="Nike Training Club • Quick start" data-sf-headline="Начните сегодня: план на 4 недели" data-sf-body="Подберите цель и уровень — и получите тренировки на каждый день." data-sf-cta="Начать бесплатно" data-sf-need="Быстрый старт (онбординг)" data-sf-segment="Новички / возвращающиеся" data-sf-functions="Опрос цели и уровня|Готовые планы|Первый workout|Expectations">Открыть креатив</button>
    </div>

    <div class="sfNeedCard">
      <div class="sfNeedTitle">«Нет времени» (ярко у занятых)</div>
      <div class="sfNeedDesc">Порог входа = длительность. Если нет быстрых форматов — пользователь откладывает “на потом”.</div>
      <div class="sfTagRow"><span class="sfTag">segment: busy</span><span class="sfTag">functions: 4</span></div>
      <ul>
        <li>Фильтры по времени (7/10/15/20 минут)</li>
        <li>Тренировки без оборудования (дома)</li>
        <li>План “минимум” (2–3 раза в неделю) без чувства вины</li>
        <li>Офлайн/скачивание (если актуально)</li>
      </ul>
      <div class="sfCreativeMock">
        <div class="sfCreativeKicker">7 Minute Workout • Time</div>
        <div class="sfCreativeHeadline">7 минут в день — и вы не “выпадаете”</div>
        <div class="sfCreativeBody">Короткие тренировки без оборудования: дома, в любом месте.</div>
        <div class="sfCreativeCta">Попробовать</div>
      </div>
      <button class="sfInlineBtn" data-sf-action="open_creative_example" data-sf-title="Креатив — Нет времени" data-sf-kicker="7 Minute Workout • Time" data-sf-headline="7 минут в день — и вы не “выпадаете”" data-sf-body="Короткие тренировки без оборудования: дома, в любом месте." data-sf-cta="Попробовать" data-sf-need="Быстро и без времени" data-sf-segment="Занятые / “нет времени”" data-sf-functions="Фильтр по времени|7‑мин программы|Без оборудования|Офлайн">Открыть креатив</button>
    </div>

    <div class="sfNeedCard">
      <div class="sfNeedTitle">Персональный план (ярко у goal‑driven)</div>
      <div class="sfNeedDesc">Пользователь хочет “как будто персональный тренер” — без ручной настройки и сомнений, что “я делаю не то”.</div>
      <div class="sfTagRow"><span class="sfTag">segment: goal‑driven</span><span class="sfTag">functions: 4</span></div>
      <ul>
        <li>Адаптивная программа под цель и прогресс</li>
        <li>Фидбек после тренировки (RPE/сложно/болит/устал)</li>
        <li>План B: замены упражнений при ограничениях</li>
        <li>Автопрогрессия нагрузки</li>
      </ul>
      <div class="sfCreativeMock">
        <div class="sfCreativeKicker">Freeletics • Personalization</div>
        <div class="sfCreativeHeadline">AI‑коуч подстраивает план под вас</div>
        <div class="sfCreativeBody">Сложность меняется по фидбеку и прогрессу — без ручной настройки.</div>
        <div class="sfCreativeCta">Собрать план</div>
      </div>
      <button class="sfInlineBtn" data-sf-action="open_creative_example" data-sf-title="Креатив — Персональный план" data-sf-kicker="Freeletics • Personalization" data-sf-headline="AI‑коуч подстраивает план под вас" data-sf-body="Сложность меняется по фидбеку и прогрессу — без ручной настройки." data-sf-cta="Собрать план" data-sf-need="Персонализация (план под цель)" data-sf-segment="Goal‑driven / self‑optimizers" data-sf-functions="Адаптивный план|Фидбек после тренировки|Замены упражнений|Автопрогрессия">Открыть креатив</button>
    </div>

    <div class="sfNeedCard">
      <div class="sfNeedTitle">Мотивация и привычка (ярко у “нужен толчок”)</div>
      <div class="sfNeedDesc">Ключевая причина churn: “пару раз позанимался — бросил”. Нужны триггеры, простые победы и социальное подкрепление.</div>
      <div class="sfTagRow"><span class="sfTag">segment: motivation</span><span class="sfTag">functions: 4</span></div>
      <ul>
        <li>Streak / бейджи / микро‑награды</li>
        <li>Челленджи на 7/14 дней</li>
        <li>Умные напоминания (по расписанию/контексту)</li>
        <li>Друзья/группы (опционально)</li>
      </ul>
      <div class="sfCreativeMock">
        <div class="sfCreativeKicker">FitOn • Motivation</div>
        <div class="sfCreativeHeadline">Челлендж на 14 дней — вместе проще</div>
        <div class="sfCreativeBody">Ставьте цель, отмечайте прогресс и не выпадайте из режима.</div>
        <div class="sfCreativeCta">Присоединиться</div>
      </div>
      <button class="sfInlineBtn" data-sf-action="open_creative_example" data-sf-title="Креатив — Мотивация" data-sf-kicker="FitOn • Motivation" data-sf-headline="Челлендж на 14 дней — вместе проще" data-sf-body="Ставьте цель, отмечайте прогресс и не выпадайте из режима." data-sf-cta="Присоединиться" data-sf-need="Мотивация и привычка" data-sf-segment="Социальные / “нужен толчок”" data-sf-functions="Streak/бейджи|Челленджи|Умные напоминания|Группы">Открыть креатив</button>
    </div>

	    <div class="sfNeedCard">
	      <div class="sfNeedTitle">Прогресс и измеримость (ярко у “цифр”)</div>
	      <div class="sfNeedDesc">Если прогресс “не виден” — ценность подписки падает. Нужны метрики, milestones и отчёты.</div>
	      <div class="sfTagRow"><span class="sfTag">segment: tracking</span><span class="sfTag">functions: 4</span></div>
	      <ul>
	        <li>Цели (вес/объёмы/сила/частота)</li>
	        <li>Отчёты недели и milestones</li>
	        <li>Графики тренировок и прогрессии</li>
	        <li>“До/после” (опционально) + журнал самочувствия</li>
	      </ul>
	      <div class="sfCreativeMock">
	        <div class="sfCreativeKicker">Adidas Training • Progress</div>
	        <div class="sfCreativeHeadline">Смотрите прогресс каждую неделю</div>
	        <div class="sfCreativeBody">Статистика тренировок и понятные отчёты — чтобы не сливаться.</div>
	        <div class="sfCreativeCta">Открыть прогресс</div>
	      </div>
	      <button class="sfInlineBtn" data-sf-action="open_creative_example" data-sf-title="Креатив — Прогресс" data-sf-kicker="Adidas Training • Progress" data-sf-headline="Смотрите прогресс каждую неделю" data-sf-body="Статистика тренировок и понятные отчёты — чтобы не сливаться." data-sf-cta="Открыть прогресс" data-sf-need="Прогресс и измеримость" data-sf-segment="Goal‑driven / цифры" data-sf-functions="Цели|Weekly отчёты|Графики прогрессии|Журнал">Открыть креатив</button>
	    </div>

	    <div class="sfNeedCard">
	      <div class="sfNeedTitle">Безопасность и доверие (ярко у “скептиков”)</div>
	      <div class="sfNeedDesc">Пользователь боится “травм/неправильно делаю” и не верит обещаниям. Нужны доказательства и забота.</div>
	      <div class="sfTagRow"><span class="sfTag">segment: skeptics</span><span class="sfTag">functions: 4</span></div>
	      <ul>
	        <li>Короткие видео‑инструкции по технике</li>
	        <li>Модификации упражнений (колени/спина/новички)</li>
	        <li>Профили тренеров (сертификаты/опыт)</li>
	        <li>Честные ожидания (без “‑10 кг за 7 дней”)</li>
	      </ul>
	      <div class="sfCreativeMock">
	        <div class="sfCreativeKicker">Nike Training Club • Trust</div>
	        <div class="sfCreativeHeadline">Техника важнее скорости</div>
	        <div class="sfCreativeBody">Покажем выполнение, дадим модификации и уберём риск “сделал неправильно”.</div>
	        <div class="sfCreativeCta">Смотреть урок</div>
	      </div>
	      <button class="sfInlineBtn" data-sf-action="open_creative_example" data-sf-title="Креатив — Безопасность" data-sf-kicker="Nike Training Club • Trust" data-sf-headline="Техника важнее скорости" data-sf-body="Покажем выполнение, дадим модификации и уберём риск “сделал неправильно”." data-sf-cta="Смотреть урок" data-sf-need="Безопасность и доверие" data-sf-segment="Скептики / травмы / новички" data-sf-functions="Видео‑техника|Модификации|Профили тренеров|Честные ожидания">Открыть креатив</button>
	    </div>

	    <div class="sfNeedCard">
	      <div class="sfNeedTitle">Разнообразие и “не надоело” (ярко у тех, кто быстро бросает)</div>
	      <div class="sfNeedDesc">Если тренировки повторяются и скучно — мотивация падает. Нужны подборки, рекомендации и “новое каждую неделю”.</div>
	      <div class="sfTagRow"><span class="sfTag">segment: variety</span><span class="sfTag">functions: 4</span></div>
      <ul>
        <li>Подборки по цели/настроению/времени</li>
        <li>Рекомендации “что дальше”</li>
        <li>Новые программы каждую неделю</li>
        <li>Избранное и плейлисты тренировок</li>
      </ul>
      <div class="sfCreativeMock">
        <div class="sfCreativeKicker">FitOn • Variety</div>
        <div class="sfCreativeHeadline">Новые тренировки каждую неделю</div>
        <div class="sfCreativeBody">Подборки по цели и времени — чтобы не скучать и не выпадать.</div>
        <div class="sfCreativeCta">Открыть подборку</div>
      </div>
      <button class="sfInlineBtn" data-sf-action="open_creative_example" data-sf-title="Креатив — Variety" data-sf-kicker="FitOn • Variety" data-sf-headline="Новые тренировки каждую неделю" data-sf-body="Подборки по цели и времени — чтобы не скучать и не выпадать." data-sf-cta="Открыть подборку" data-sf-need="Разнообразие / чтобы не надоело" data-sf-segment="Быстро бросающие / скука" data-sf-functions="Подборки|Рекомендации|Новые программы|Избранное">Открыть креатив</button>
	    </div>

    <div class="sfNeedCard">
      <div class="sfNeedTitle">Питание как часть системы (ярко у “хочу результат”)</div>
      <div class="sfNeedDesc">Для похудения/тонуса тренировки без питания часто дают слабый эффект → пользователь “не видит результата”.</div>
      <div class="sfTagRow"><span class="sfTag">segment: weight loss</span><span class="sfTag">functions: 4</span></div>
      <ul>
        <li>План питания / рекомендации</li>
        <li>Рецепты и список покупок</li>
        <li>Трекер калорий/БЖУ (если нужно)</li>
        <li>Связка “питание + тренировка” в одном плане</li>
      </ul>
      <div class="sfCreativeMock">
        <div class="sfCreativeKicker">Category • Nutrition</div>
        <div class="sfCreativeHeadline">План питания + тренировки</div>
        <div class="sfCreativeBody">Система, а не разрозненные советы: питание под вашу цель.</div>
        <div class="sfCreativeCta">Открыть план</div>
      </div>
      <button class="sfInlineBtn" data-sf-action="open_creative_example" data-sf-title="Креатив — Питание" data-sf-kicker="Category • Nutrition" data-sf-headline="План питания + тренировки" data-sf-body="Система, а не разрозненные советы: питание под вашу цель." data-sf-cta="Открыть план" data-sf-need="Питание / рацион" data-sf-segment="Похудение / результат" data-sf-functions="План питания|Рецепты|Список покупок|Трекер">Открыть креатив</button>
    </div>

    <div class="sfNeedCard">
      <div class="sfNeedTitle">Сообщество и совместные челленджи (ярко у “социальных”)</div>
      <div class="sfNeedDesc">Подкрепление “я не один” удерживает в режиме: совместные цели, сравнение прогресса, поддержка.</div>
      <div class="sfTagRow"><span class="sfTag">segment: community</span><span class="sfTag">functions: 3</span></div>
      <ul>
        <li>Группы/друзья и приглашения</li>
        <li>Челленджи + лидерборд</li>
        <li>Шеринг прогресса (опционально)</li>
      </ul>
      <div class="sfCreativeMock">
        <div class="sfCreativeKicker">FitOn • Community</div>
        <div class="sfCreativeHeadline">Тренируйтесь вместе с друзьями</div>
        <div class="sfCreativeBody">Челленджи и лидерборды — чтобы держать темп.</div>
        <div class="sfCreativeCta">Пригласить друзей</div>
      </div>
      <button class="sfInlineBtn" data-sf-action="open_creative_example" data-sf-title="Креатив — Community" data-sf-kicker="FitOn • Community" data-sf-headline="Тренируйтесь вместе с друзьями" data-sf-body="Челленджи и лидерборды — чтобы держать темп." data-sf-cta="Пригласить друзей" data-sf-need="Сообщество / челленджи" data-sf-segment="Социальные / поддержка" data-sf-functions="Группы/друзья|Челленджи+лидерборд|Шеринг прогресса">Открыть креатив</button>
    </div>

    <div class="sfNeedCard">
      <div class="sfNeedTitle">Порог цены / trial (ярко у сомневающихся)</div>
      <div class="sfNeedDesc">Если человек не верит, что “зайдёт”, он не купит подписку. Нужны триал, прозрачные условия и простой cancel.</div>
      <div class="sfTagRow"><span class="sfTag">segment: skeptics</span><span class="sfTag">functions: 4</span></div>
      <ul>
        <li>Free trial 7–14 дней</li>
        <li>Прозрачные условия подписки</li>
        <li>Простой cancel в 1–2 клика</li>
        <li>Пакеты (месяц/квартал) + скидка за длинный план</li>
      </ul>
      <div class="sfCreativeMock">
        <div class="sfCreativeKicker">Category • Trial</div>
        <div class="sfCreativeHeadline">Попробуйте 7 дней бесплатно</div>
        <div class="sfCreativeBody">Поймите, подходит ли вам формат — и отключите в один клик, если нет.</div>
        <div class="sfCreativeCta">Начать trial</div>
      </div>
      <button class="sfInlineBtn" data-sf-action="open_creative_example" data-sf-title="Креатив — Trial" data-sf-kicker="Category • Trial" data-sf-headline="Попробуйте 7 дней бесплатно" data-sf-body="Поймите, подходит ли вам формат — и отключите в один клик, если нет." data-sf-cta="Начать trial" data-sf-need="Цена / trial" data-sf-segment="Сомневающиеся / новые" data-sf-functions="Free trial|Прозрачные условия|Cancel в 1–2 клика|Пакеты">Открыть креатив</button>
    </div>
  </div>

  <div class="chartNote">Скролл вправо → больше связок. В проекте карточки собираются из Segment×Need (block 1) + evidence и дополняются реальными конкурентными креативами (скриншоты/ссылки).</div>
</div>

<div class="chartNote">Методология: источники → каталоги сегментов/потребностей → карта спроса (Segment×Need) → декомпозиция Need→Functions → сборка креативов/сообщений → (дальше) выбор связок и сравнение по экономике.</div>
