import { initApp } from './js/i18n.js';
import { initLeadForm } from './js/lead.js';
import { fetchAndRenderTeachers, fetchAndRenderCertificates } from './js/api.js';

// Импортируем наш компонент и данные курсов
import { CourseCard } from './js/components/CourseCard.js';
import { coursesData } from './js/data/coursesData.js';

import { StepCard } from './js/components/StepCard.js';
import { stepsData } from './js/data/stepsData.js';

function renderSteps() {
  const container = document.getElementById('stepsGrid');
  if (!container) return;
  container.innerHTML = '';
  stepsData.forEach(step => container.appendChild(StepCard(step)));
}

// Функция для отрисовки курсов
function renderCourses() {
  const grid = document.getElementById('coursesGrid');
  if (!grid) return;

  grid.innerHTML = '';
  coursesData.forEach(course => {
    grid.appendChild(CourseCard(course));
  });
}

document.addEventListener('DOMContentLoaded', () => {
  // 1. Отрисовываем курсы
  renderCourses();

  // 2. Запускаем переводы и интерфейс
  initApp();
  
  // 3. Запускаем отправку формы
  initLeadForm();
  
  // 4. Подтягиваем данные с бэкенда Django
  fetchAndRenderTeachers();
  fetchAndRenderCertificates();

  renderSteps()
});