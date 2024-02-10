// Purpose: This file contains the utility functions that are used in the app_bun.

import { DateTimeFormat } from "intl";
import type { DateTimeFormatOptions } from "intl";

// Purpose: This function returns the current time in the specified timezone.
export function returnTime(timezone: string = "Europe/Moscow") {
  const currentTime = returnTzTime(timezone);

  return `<div>
            <h1>Current time in Moscow: ${currentTime}</h1>
         </div>
    `;
}

// Purpose: This function returns the current time in the specified timezone.
export function returnTzTime(timezone: string) {
  const date = new Date();
  const options: DateTimeFormatOptions = {
    timeZone: timezone,
    hour: "numeric",
    minute: "numeric",
  };
  return new DateTimeFormat("en-US", options).format(date);
}
