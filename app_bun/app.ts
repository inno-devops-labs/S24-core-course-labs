import { returnTime } from "./utils.js";

export function index() {
  return new Response(returnTime(), {
    headers: { "content-type": "text/html" },
  });
}
