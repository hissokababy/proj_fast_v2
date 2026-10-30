// script.js
import { initApp } from './js/i18n.js';
import { initLeadForm } from './js/lead.js';
import { 
  fetchAndRenderTeachers, 
  fetchAndRenderCertificates, 
  fetchAndRenderEvents,
  fetchAndRenderPhotoByKey // Импортируем функцию для картинок по ключу
} from './js/api.js';

import { CourseCard } from './js/components/CourseCard.js';
import { coursesData } from './js/data/coursesData.js';

import { StepCard } from './js/components/StepCard.js';
import { stepsData } from './js/data/stepsData.js';

function renderCourses() {
  const grid = document.getElementById('coursesGrid');
  if (!grid) return;
  grid.innerHTML = '';
  coursesData.forEach(course => grid.appendChild(CourseCard(course)));
}

function renderSteps() {
  const container = document.getElementById('stepsGrid');
  if (!container) return;
  container.innerHTML = '';
  stepsData.forEach(step => container.appendChild(StepCard(step)));
}

document.addEventListener('DOMContentLoaded', () => {
  // 1. Отрисовываем локальные статические блоки
  renderCourses();
  renderSteps();

  // 2. Инициализируем интерфейс, переводы и форму
  initApp();
  initLeadForm();
  
  // 3. Подтягиваем динамические данные из Django API
  fetchAndRenderTeachers();
  fetchAndRenderCertificates();
  fetchAndRenderEvents();

  // 4. Подтягиваем логотип и фото для блока "О нас" с бэка по их ключам (slug)
  // Замени 'main-logo' и 'why-photo' на те слова, которые у тебя записаны в базе данных в поле slug
  fetchAndRenderPhotoByKey('main-logo', '.brand img');
  fetchAndRenderPhotoByKey('why-photo', '.whyPhoto img');
}); 