function updateMoscowTime() {
    const moscowTimezone = 'Europe/Moscow';
    const moscowTime = new Date().toLocaleString('en-US', { timeZone: moscowTimezone });

    document.getElementById('time').textContent = `Current Time in Moscow: ${moscowTime}`;
}

// Update the time every second
setInterval(updateMoscowTime, 1000);

// Initial update
updateMoscowTime();
