export function shuffle(array: any[]) {
  let currentIndex: number = array.length;
  let randomIndex: number;

  // While there remain elements to shuffle...
  while (currentIndex != 0) {
    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    // And swap it with the current element.
    [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
  }
}

/**
 * @param min [minimum value
 * @param max maximum value]
 * @returns Randomly generated integer
 */
export function randint(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

export function generateArray(count, min: number = 0, max: number = 100) {
  const array = [];
  for (let i = 0; i < count; ++i) {
    array.push(randint(min, max));
  }
  return array;
}
