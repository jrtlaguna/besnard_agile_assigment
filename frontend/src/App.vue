<template>
  <div>
    <Home />
  </div>
</template>

<script>
import Home from "./components/Home.vue";
export default {
  name: "App",
  components: { Home },
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-height: 100%;
  height: auto !important;
  height: 100%;
  box-shadow: 10px 10px 8px 10px #888888;
  padding-top: 5rem;
  margin-left: 6rem;
  margin-right: 6rem;
}
</style>
