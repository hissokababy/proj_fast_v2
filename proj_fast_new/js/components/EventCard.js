export function EventCard(event) {
  const div = document.createElement('div');
  div.className = 'eventCard';

  const titleContent = event.title || `<span data-i18n="${event.titleKey}"></span>`;

  div.innerHTML = `
    <img src="${event.image}" alt="Event" data-i18n-attr="alt:${event.altKey}" />
    <strong>${titleContent}</strong>
    <span><span data-i18n="${event.descKey}"></span></span>
  `;

  return div;
}