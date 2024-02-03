// Purpose: This is the main logic section for the app. It handles the request and response logic.

import { returnTime } from "./utils.js";

export function index() {
  return new Response(returnTime(), {
    headers: { "content-type": "text/html" },
  });
}
