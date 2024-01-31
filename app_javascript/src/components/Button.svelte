<script>
  export let disabled = false;
</script>

<button class="root" {disabled} on:click>
  <slot/>
</button>

<style lang="scss">
  .root {
    font-family: monospace;
    font-size: 1.25rem;
    outline: none;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 12px;
    color: #fff;
    background: var(--primary);
    transition: background-color 0.1s;
    text-transform: uppercase;
    letter-spacing: 0.1rem;
    cursor: pointer;

    &:hover {
      background: var(--primary-light);
    }

    &:active {
      background: var(--primary-dark);
    }

    &:disabled {
      cursor: default;
      background: #aaa;
    }
  }
</style>
