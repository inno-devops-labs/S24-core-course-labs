interface SortingFuncArgs {
  array: number[];
  compare: (indexA: number, indexB: number) => Promise<-1 | 0 | 1>;
  swap: (indexA: number, indexB: number) => Promise<void>;
  select: (index: number) => void;
  unSelect: (index: number) => void;
}

type SortingFunc = (args: SortingFuncArgs) => Promise<void>

export interface ArrayElement {
  index: number;
  value: number;
  selected: boolean;
  isComparing: boolean;
  isSwapping: boolean;
}

const sleep = (ms: number) => (new Promise(r => setTimeout(r, ms)));

const bubbleSort: SortingFunc = async ({
  array,
  compare,
  swap,
}) => {
  const size = array.length;
  let complete = 0;
  let swapped = true;
  while (swapped) {
    swapped = false;
    for (let i = 0; i < size - 1 - complete; i++) {
      if (await compare(i, i + 1) === 1) {
        await swap(i, i + 1);
        swapped = true;
      }
    }
    complete++;
  }
};

const selectionSort: SortingFunc = async ({
  array,
  compare,
  swap,
  select,
  unSelect,
}) => {
  const size = array.length;

  for (let i = 0; i < size - 1; i++) {
    await select(i);
    let jMin = i;

    for (let j = i + 1; j < size; j++) {
      if (await compare(j, jMin) === -1) {
        if (jMin !== i) {
          await unSelect(jMin);
        }
        jMin = j;
        await select(jMin);
      }
    }

    if (jMin !== i) {
      await swap(i, jMin);
    }
    await unSelect(i);
    await unSelect(jMin);
  }
};

export const algorithms: { name: string, func: SortingFunc }[] = [
  {name: "Bubble Sort", func: bubbleSort},
  {name: "Selection Sort", func: selectionSort},
];

export function generateSortMethods(
  elements: ArrayElement[],
  updateTrigger: () => void,
  delayGetter: () => number,
) {
  // Map between number indecies and elements indecies
  const elementsIndecies: { [key: number]: number } = {};

  // Generate array of numbers from the elements array
  const numbers: number[] = Array(elements.length);
  elements.forEach((el, i) => {
    numbers[el.index] = el.value;
    elementsIndecies[el.index] = i;
  });

  const swap = async (indexA: number, indexB: number) => {
    // Swap numbers
    [numbers[indexA], numbers[indexB]] = [numbers[indexB], numbers[indexA]];

    // Swap elements indecies
    [
      elements[elementsIndecies[indexA]].index,
      elements[elementsIndecies[indexB]].index,
    ] = [
      elements[elementsIndecies[indexB]].index,
      elements[elementsIndecies[indexA]].index,
    ];
    [
      elementsIndecies[indexA],
      elementsIndecies[indexB],
    ] = [
      elementsIndecies[indexB],
      elementsIndecies[indexA],
    ];

    elements[elementsIndecies[indexA]].isSwapping = true;
    elements[elementsIndecies[indexB]].isSwapping = true;

    updateTrigger();
    await sleep(delayGetter());

    elements[elementsIndecies[indexA]].isSwapping = false;
    elements[elementsIndecies[indexB]].isSwapping = false;
    updateTrigger();
    await sleep(delayGetter());
  };

  const compare = async (indexA: number, indexB: number) => {
    elements[elementsIndecies[indexA]].isComparing = true;
    elements[elementsIndecies[indexB]].isComparing = true;
    updateTrigger();
    await sleep(delayGetter());
    elements[elementsIndecies[indexA]].isComparing = false;
    elements[elementsIndecies[indexB]].isComparing = false;
    updateTrigger();
    await sleep(delayGetter());

    if (numbers[indexA] > numbers[indexB]) {
      return 1;
    } else {
      return numbers[indexA] === numbers[indexB] ? 0 : -1;
    }
  };

  const select = async (index: number) => {
    elements[elementsIndecies[index]].selected = true;
    updateTrigger();
  };

  const unSelect = async (index: number) => {
    elements[elementsIndecies[index]].selected = false;
    updateTrigger();
  };

  return {
    compare,
    swap,
    select,
    unSelect,
    array: numbers,
  };
}
