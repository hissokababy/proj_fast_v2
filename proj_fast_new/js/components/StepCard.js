export function StepCard(step) {
  const article = document.createElement('article');
  article.className = 'step';

  article.innerHTML = `
    <div class="stepNo"><span data-i18n="${step.numberKey}"></span></div>
    <h3><span data-i18n="${step.titleKey}"></span></h3>
    <p><span data-i18n="${step.descKey}"></span></p>
  `;

  return article;
}