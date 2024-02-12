document.addEventListener("DOMContentLoaded", function () {
    const updateTime = () => {
        const now = new Date();
        const moscowTime = now.toLocaleTimeString('en-US',
            {
                timeZone: "Europe/Moscow",
                hour: 'numeric',
                minute: 'numeric',
                second: 'numeric'
            }
        );
        document.getElementById('time').innerText = `Current time in Moscow: ${moscowTime}`;
    };

    updateTime();
    setInterval(updateTime, 1000);
});

