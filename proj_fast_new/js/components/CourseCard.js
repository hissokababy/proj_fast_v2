export function CourseCard(course) {
  const article = document.createElement('article');
  article.className = 'course';
  
  const featuresList = course.features 
    ? course.features.map(feature => `<li>${feature}</li>`).join('')
    : '';

  article.innerHTML = `
    <div class="courseIcon">${course.icon}</div>
    <h3>${course.title}</h3>
    <p>${course.description}</p>
    <ul>${featuresList}</ul>
    <a class="textLink" data-course="${course.title}" href="#contacts">
      <span>${course.ctaText}</span> <span>→</span>
    </a>
  `;
  
  return article;
}