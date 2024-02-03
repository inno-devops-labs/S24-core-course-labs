import {} from "intl";

export function returnTime(timezone = "Europe/Moscow") {
  const currentTime = returnTzTime(timezone);

  return `<div>
            <h1>Current time in Moscow: ${currentTime}</h1>
         </div>
    `;
}

export function returnTzTime(timezone = "Europe/Moscow") {
  const date = new Date();
  const options: Intl.DateTimeFormatOptions = {
    timeZone: timezone,
    hour: "numeric",
    minute: "numeric",
  };
  return new Intl.DateTimeFormat("en-US", options).format(date);
}
