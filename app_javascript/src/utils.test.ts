import { expect, test } from 'vitest'
import { shuffle, generateArray } from "./utils"

test("shuffle changes elements position", () => {
  const arr = [0, 1, 2, 3, 4, 5]
  for (let i = 0; i < 10; i++) {
    shuffle(arr)
    let changed = false
    for (let i = 0; i <= 5; i++) {
      if (arr[i] !== i) {
        changed = true
        break
      }
    }
    if (changed) {
      expect(arr.length).toBe(6)
      return
    }
  }
  throw new Error("Was not shuffled.")
})

test("generateArray correctly generates arrays", () => {
  const mins = [-100, 0, 200, 1]
  const maxs = [-10, 5, 1000, 2]
  const counts = [100, 20, 300, 20]
  expect(mins.length).toBe(maxs.length)
  expect(mins.length).toBe(counts.length)

  for (let i = 0; i < mins.length; i++) {
    const min = mins[i]
    const max = maxs[i]
    const count = counts[i]
    const array = generateArray(count, min, max)
    expect(array.length).toBe(count)
    for (let j = 0; j < count; j++) {
      expect(array[j]).toBeGreaterThanOrEqual(min)
      expect(array[j]).toBeLessThanOrEqual(max)
    }
  }
})
