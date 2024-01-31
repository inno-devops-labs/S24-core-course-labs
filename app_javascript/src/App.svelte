<script lang="ts">
  import Button from "./components/Button.svelte";
  import Item from "./components/Item.svelte";
  import ItemsContainer from "./components/ItemsContainer.svelte";
  import {shuffle, generateArray} from "./utils";
  import {generateSortMethods, algorithms} from "./sortings";
  import type {ArrayElement} from "./sortings";

  let currentAlgorithm: number = 0;
  let speed: number = 200;
  $: delay = 500 - speed;

  let updatesCounter = 0;
  const triggerUpdate = () => {
    updatesCounter++;
  };

  let shouldSort = false;
  let isSorting = false;

  let containerWidth = 0;
  let maxElements = 0;
  let lastWidth: number = 0;
  let elements: ArrayElement[] = [];
  let indices: number[] = [];

  $:{
    elements = elements;
    updatesCounter = updatesCounter;
  }

  $:{
    if (shouldSort && !isSorting) {
      shouldSort = false;
      isSorting = true;
      algorithms[currentAlgorithm].func(
        generateSortMethods(
          elements,
          triggerUpdate,
          () => delay,
        )).finally(() => {
          isSorting = false;
        },
      );
    }
  }

  $: if (elements.length === 0 || containerWidth !== lastWidth) {
    // Elements array should be regenerated

    // Calculate how many elements can fit into the container
    const width = containerWidth;
    maxElements = Math.floor(width / 14);
    if (width % 14 >= 12) {
      ++maxElements;
    }

    // Generate array of elements with random values
    elements = [];
    indices = [];
    const values = generateArray(maxElements, 2, 50);
    for (let i = 0; i < maxElements; ++i) {
      indices.push(i);
      elements.push({
        index: i,
        value: values[i],
        selected: false,
        isComparing: false,
        isSwapping: false,
      });
    }

    lastWidth = containerWidth;
  }

  const handleShuffle = () => {
    shuffle(indices);
    for (let i = 0; i < indices.length; ++i) {
      elements[i].index = indices[i];
    }
  };

  const handleSort = () => {
    shouldSort = true;
  };
</script>

<main class="root">
  <div class="wrapper">
    <div class="control-panel">
      <Button
        disabled={isSorting}
        on:click={handleShuffle}
      >Shuffle
      </Button>
      <Button disabled={isSorting} on:click={handleSort}>Sort</Button>
      <input bind:value={speed} max="500" min="10" step="10" type="range">
    </div>
    <div class="array-wrapper" style={`--animation-speed: ${delay}ms;`}>
      <div class="array">
        <ItemsContainer bind:width={containerWidth}>
          {#each elements as element, i (i)}
            <Item {...element}/>
          {/each}
        </ItemsContainer>
      </div>
      <select bind:value={currentAlgorithm} class="algorithm-select" disabled={isSorting}>
        {#each algorithms as algorithm, i (algorithm.name)}
          <option value={i}>
            {algorithm.name}
          </option>
        {/each}
      </select>
    </div>
  </div>
</main>

<style lang="scss">
  .root {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin: auto;
    padding-left: 12px;
    padding-right: 12px;
    width: 100%;
    height: 100%;

    @media screen and (min-width: 768px) {
      max-width: 768px;
    }

    @media screen and (min-width: 1024px) {
      max-width: 1024px;
    }
  }

  .wrapper {
    display: flex;
    gap: 12px;
    align-items: center;
    justify-content: space-between;
    width: 100%;
  }

  .control-panel {
    display: inline-flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 12px;
  }

  .array-wrapper {
    flex: 1 0 auto;
    display: flex;
    flex-direction: column;
  }

  .array {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    border: 2px solid rgba(0, 0, 0, 0.1);
    border-bottom: none;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    padding: 0 1rem;
  }

  .algorithm-select {
    color: #000;
    text-align: center;
    outline: none;
    border: none;
    font-size: 1rem;
    letter-spacing: 0.1rem;
    background-color: rgba(0, 0, 0, 0.1);
    cursor: pointer;
    padding: 0.5rem 1rem;
    border-bottom-left-radius: 6px;
    border-bottom-right-radius: 6px;
    -webkit-appearance: none;
    transition-property: letter-spacing, background-color, color;
    transition-duration: 200ms;

    &::-ms-expand {
      display: none;
    }

    &:hover:not(:disabled) {
      letter-spacing: 0.2rem;
      background-color: #2d7eda;
      color: #fff;
    }

    &:disabled {
      color: #444;
    }
  }

  input[type="range"] {
    cursor: pointer;
  }
</style>
