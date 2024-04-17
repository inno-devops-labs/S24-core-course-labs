// Purpose: This file contains the utility functions that are used in the app_bun.

import { } from "intl";

// Purpose: This function returns the current time in the specified timezone.
export function returnTime(timezone: string = "Europe/Moscow") {
  const currentTime = returnTzTime(timezone);

  return `<div>
            <h1>Current time in ${timezone}: ${currentTime}</h1>
         </div>
    `;
}

// Purpose: This function returns the current time in the specified timezone.
export function returnTzTime(timezone: string) {
  const date = new Date();
  const options: Intl.DateTimeFormatOptions = {
    timeZone: timezone,
    hour: "numeric",
    minute: "numeric",
  };
  return new Intl.DateTimeFormat("en-US", options).format(date);
}
