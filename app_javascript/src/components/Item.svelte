<script lang="ts">
  export let value: number = 10
  export let selected: boolean = false
  export let index: number = 0
  export let isSwapping: boolean
  export let isComparing: boolean
</script>


<span
  class="item"
  class:comparing={isComparing}
  class:selected
  class:swapping={isSwapping}
  style={`
    height: calc(${value + 1}em / 5);
    left: calc(${index}0px + ${index * 4}px);
  `}
></span>

<style lang="scss">
  .item {
    position: absolute;
    left: 0;
    display: block;
    width: 10px;
    transition-timing-function: ease, cubic-bezier(0.210, 0.095, 0.000, 0.980);
    transition-duration: var(--animation-speed);
    transition-property: left, background-color;
    border: 1px solid #dadada;
    border-radius: 2px;
    background-color: #eee;

    &.selected::after {
      content: "⬆";
      position: absolute;
      bottom: -20px;
      left: 50%;
      transform: translateX(-50%);
    }

    &.comparing {
      background-color: #89d37c;
    }

    &.swapping {
      transition-timing-function: ease, cubic-bezier(0.210, 0.095, 0.000, 0.980);
      transition-duration: 0.25s, 50ms;
      background-color: #e6af7c;
    }
  }
</style>
