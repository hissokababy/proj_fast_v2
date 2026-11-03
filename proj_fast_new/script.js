import { initApp } from './js/i18n.js';
import { initLeadForm } from './js/lead.js';
import { 
  fetchAndRenderTeachers, 
  fetchAndRenderCertificates, 
  fetchAndRenderEvents,
  fetchAndRenderPhotoByKey, // 1. Импортируем функцию
  fetchAndRenderCenterCarousel // <--- Импортируем функцию карусели
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

  // 2. Инициализируем интерфейс и форму
  initApp();
  initLeadForm();

  // 3. Загружаем динамические данные с бэкенда
  fetchAndRenderTeachers();
  fetchAndRenderCertificates();
  fetchAndRenderEvents();
  fetchAndRenderCenterCarousel(); // <--- Запускаем загрузку карусели

  // 4. Подтягиваем логотип и фото "О нас" по их ключам (slug) из админки Django
  // Замени 'logo' и 'why-photo' на те значения slug, которые ты прописал на бэкенде
  fetchAndRenderPhotoByKey('logo', '.brand img');
  fetchAndRenderPhotoByKey('why-photo', '.whyPhoto img');
});