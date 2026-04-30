# Архитектура Мода (AI-Native Mapping)
Этот документ содержит точные названия файлов, `namespaces`, `переменных (variables)`, `модификаторов` и `флагов (flags)` мода "HOI4+ War Fatigue Surrender". Использовать как Ground Truth для предотвращения галлюцинаций LLM и экономии токенов на `grep` поиске.

---

## 1. Точная Карта Файлов (File-by-File Mapping)

**`common/decisions/` (Файлы Решений Игрока/ИИ):**
- `plus_cp_conditional_surrender.txt` — Предложение своей сдачи с сохранением правительства.
- `plus_cp_debug_decisions.txt` — Читы/Дебаг инструменты для теста.
- `plus_cp_propose_peace.txt` — Стандартные решения предложений мира.
- `plus_cp_reparation_decisions.txt` — Финансовые контрибуции и штрафы фабриками.
- `plus_cp_subject_decisions.txt` — Действия над марионетками во время мира (освободить/сделать вассалом).
- `plus_cp_submission_offers.txt` — Опции принуждения нейтралов к вхождению в сферу.
- `plus_cp_territory_decisions.txt` — Требования передачи конкретных регионов (states).
- `plus_cp_white_peace.txt` — Решения статуса-кво (белый мир).
- `plus_cs_crisis_decisions.txt` — Решения на подавление бунтов и забастовок политической властью.
- `plus_cs_pp_decisions.txt` — Выдача экономических стимулов.
- `categories/plus_cs_decision_categories.txt` — Регистрация GUI-вкладок (например, `peace_options`, `peace_take_state`).

**`common/dynamic_modifiers/` (Масштабируемые Штрафы):**
- `plus_cs_crisis_modifiers.txt` — Кризисные штрафы (`war_inflation_crisis`, потери рекрутов).
- `plus_cs_dynamic_modifiers.txt` — Базовые множители усталости (`homefront_collapse`, `total_exhaustion`).

**`common/ideas/` и `common/modifiers/`:**
- `plus_cs_ideas.txt` — Нац. духи политического паралича (`internal_crisis_medium` и т.д.).
- `plus_cs_modifiers.txt` — State-модификаторы на рост сопротивления (`plus_cs_partisan_activity`).

**`common/on_actions/` (Точки Входа):**
- `plus_cf_on_action.txt` / `plus_cs_on_actions.txt` — Вызов стартовых ивентов при начале войны / капитуляции / загрузке игры.

**`common/opinion_modifiers/` (Мнения Ботов):**
- `plus_cs_opinion.txt` — Значения падения/роста мнения (`faction_betrayal`, `peace_territory_preserved`).
- `plus_cs_opinion_modifiers.txt` — Связка модификаторов отношений.

**`common/scripted_diplomatic_actions/`:**
- `plus_cs_diplomatic_actions.txt` — Кастомное окно ПКМ по дипломатии страны.

**`common/scripted_effects/` (Ядро Математики и Скриптов):**
- `plus_cs_ai_weights.txt` — Веса (weight) для ИИ решений.
- `plus_cs_chance_calculator.txt` — Главный калькулятор шансов ИИ по итогу его весов.
- `plus_cs_crisis_checks.txt` — Скрипт проверки, превышает ли страна предел прочности.
- `plus_cs_dynamic_penalties.txt` — Наложение штрафов на призыв/фабрики.
- `plus_cs_economic_effects.txt` — Оценка закона об экономике и его перегрева `economy_overheat_counter`.
- `plus_cs_peace_effects.txt` — Исполнительный скрипт (перекрас карты, передача стейтов: `is_peace_state_target`).
- `plus_cs_score_calculations.txt` — Вычисление боевых успехов (`plus_cs_hidden_resolve`).
- `plus_cs_spirit_effects.txt` — Выставление духа при старте лидера/войны.
- `plus_cs_tooltip_effects.txt` — Сборка текстовых всплывающих подсказок для удобства игрока.
- `plus_cs_truce_effects.txt` — Наложение перемирия и демилитаризации после войны.
- `plus_cs_war_exhaustion.txt` — Скрипт подсчета потерь и давления (`plus_cs_pressure_ratio`).

**`events/`:** (Строгая привязка всех 16 файлов к логике и `namespaces`)
- `plus_cs_ai_peace_pulse.txt` (`plus_cs_pulse`) — Цикл ИИ "рулетки" генерации мирных предложений для снижения спама.
- `plus_cs_capitulation_peace.txt` (`plus_cs`) — Капитулировавшая страна просит у лидера своего альянса разрешения сдаться (`plus_cs.430-432`).
- `plus_cs_conference_events.txt` (`plus_cs`) — Конференции и распределение стейтов при капитуляции минора/мажора (`plus_cs.2`, `plus_cs.3`).
- `plus_cs_diplomacy.txt` (`plus_cs_diplomacy`) — Смарт-дипломатия: откуп территориями до войны и распад империй (`plus_cs_diplomacy.1`, `.10`, `.20`).
- `plus_cs_faction_peace.txt` (`plus_cs`) — Запрос члена альянса на выход из фракции для сепаратного мира (`plus_cs.420-422`).
- `plus_cs_faction_veto.txt` (`plus_cs`) — Механика запрета/вето лидером альянса на мирные договоры союзников (`plus_cs.20-23`).
- `plus_cs_internal.txt` (`plus_cs_internal`) — Подавление бунтов, военные ультиматумы генералитета и политический коллапс (`plus_cs_internal.1-15`).
- `plus_cs_military.txt` (`plus_cs`) — Ивенты на ранения генералов при сильном истощении (`plus_cs.1001-1002`).
- `plus_cs_optimization_loop.txt` (`plus_cs_opt`) — Главный хаб и движок мода (`plus_cs.999`), размазывающий лаги на разные дни тика.
- `plus_cs_outcome_events.txt` (`plus_cs`) — Новостные вывески и окна уведомлений при исходах мирного договора (`plus_cs.5`, `.6`, `.410`).
- `plus_cs_peace_offer_event.txt` (`plus_cs`) — Запуск окна переговоров при получении предложения мира, расчет контрибуций (`plus_cs.1`).
- `plus_cs_puppet_events.txt` (`plus_cs`) — Переход марионеток между оверлордами при гражданках/мире (`plus_cs.210`, `.300-305`).
- `plus_cs_submission_events.txt` (`plus_cs`) — Механика капитуляции через вассализацию и передачу клаймов (`plus_cs.201-205`).
- `plus_cs_surrender_logic.txt` (`plus_cs_logic`) — Внутренний ивент "совет", высчитывающий, решит ли бот сдаться или драться дальше (`plus_cs.surrender_debate`).
- `plus_cs_territory_demands.txt` (`plus_cs_demands`) — Ультиматумы на возврат национальных провинций (core demands) (`plus_cs_demands.1-3`).
- `plus_cs_white_peace_event.txt` (`plus_cs`) — Окно и скрипт заключения Белого мира и перемирия со всем альянсом (`plus_cs.4`).

---

## 2. Глобальные Переменные (Variables Math)
Точные ключи, используемые в `set_variable` / `check_variable`:

- `plus_cs_hidden_resolve` (от -50 до +50, зависит от трейтов лидера).
- `plus_cs_current_pressure` (текущее военное давление/урон от войны).
- `plus_cs_pressure_ratio` (множитель давления на основе экономики/потерь).
- `plus_cs_crisis_multiplier` (используется для увеличения шансов кризиса).
- `plus_cs_ai_score` -> `plus_cs_final_calc_score` (финальный вес ИИ при принятии решения о мире/войне).
- `plus_cs_prev_battalions` / `plus_cs_prev_casualties` (отслеживание скачков потерь).
- `core_pop_calc` (расчет резервов населения).
- `economy_overheat_counter` (счетчик перегрева экономики от тотальной мобилизации).
- `plus_cs_prev_econ_law` (сохраняет предыдущий закон экономики до перегрева/кризиса).
- `plus_cs_peace_target` (ID цели переговоров).
- `cnt_og_vp` / `og_vp` (подсчет победных очков).
- `is_peace_state_target` (флаг для стейта при передаче территорий).
- `plus_cs_reparation_bonus` (капитуляционный вес для расчета репараций).

---

## 3. Трекинг Состояний (Country Flags)
Ключи для `has_country_flag` / `set_country_flag`:

- `plus_cs_peace_cooldown` (стандартный КД на отправку предложения).
- `plus_cs_collapse_cooldown` (КД на внутренний коллапс).
- `plus_cs_signed_separate_peace` (штраф за сепаратный мир, 360 дней).
- `plus_cs_offered_peace_before` / `plus_cs_offered_peace_twice` (как долго ИИ отказывается/спамит).
- `plus_cs_refused_surrender` (отказ от сдачи).
- `plus_cs_is_surrendering` / `plus_cs_seeking_peace` / `plus_cs_peace_type_negotiation` (текущий процесс переговоров).
- `plus_cs_waiting_response` (ожидание ответа по ивенту).
- `plus_cs_chance_high`, `plus_cs_chance_medium`, `plus_cs_chance_low` (вероятностный флаг по итогам калькуляции).
- `plus_cs_war_strain` -> `plus_cs_exhausted` -> `plus_cs_total_exhaustion` (фазы давления, навешивают штрафы).
- `civil_war_risk_active` / `plus_cs_had_civil_war` (состояния кризиса).
- `plus_cs_loop_active`, `plus_cs_revolter_processed` (для контроля двойных срабатываний оптим. скрипта).
- `plus_cs_resolve_initialized`, `plus_cs_scores_fresh` (свежесть кэшированных переменных).

---


