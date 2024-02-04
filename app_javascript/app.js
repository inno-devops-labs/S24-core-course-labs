const moscowOffset = 3;
const moscowDate = new Date();
moscowDate.setHours(moscowDate.getHours() + moscowOffset);
function formatMoscowTime(date) {
  return date.toLocaleString("en-US", {
    hour: "numeric",
    minute: "numeric",
    second: "numeric",
    hour12: false,
    timeZone: "Europe/Moscow",
  });
}
const moscowTimeElement = document.getElementById("moscow-time");
setInterval(() => {
  const now = new Date();
  moscowTimeElement.textContent = formatMoscowTime(now);
}, 1000);
