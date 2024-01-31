<script>
  export let width = 0
</script>

<div bind:clientWidth={width} class="root">
  <slot/>
</div>

<style lang="scss">
  .root {
    position: relative;
    display: flex;
    overflow: hidden;
    align-items: flex-end;
    flex-wrap: nowrap;
    width: 100%;
    height: 200px;
    padding-bottom: 20px;

    &::after {
      content: "";
      position: absolute;
      z-index: -1;
      bottom: 20px;
      left: 2px;
      width: calc(100% - 4px);
      border-top: 1px dashed rgba(0, 0, 0, 0.1);
    }
  }
</style>
