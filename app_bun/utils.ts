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

async function getVisits() {
  const filename = process.env.VISITS_FILE;
  if (!filename) {
    throw new Error("VISITS_FILE environment variable is not set");
  }
  const file = Bun.file(filename);
  if (!(await file.exists())) {
    await Bun.write(filename, "0");
    return 0;
  }
  let visits = await file.text();
  if (visits === "") {
    await Bun.write(filename, "0");
    visits = "0";
  }
  return parseInt(visits);
}

export async function incrementVisits() {
  const visits = await getVisits();
  const filename = process.env.VISITS_FILE;
  if (!filename) {
    throw new Error("VISITS_FILE environment variable is not set");
  }
  await Bun.write(filename, String(visits + 1));
}

export async function returnVisitCounts() {
  const visits = await getVisits();
  return `<h1>Number of visits: ${visits}</h1>`;
}