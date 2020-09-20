<template>
  <div id="app">
    <Stepper></Stepper>
  </div>
</template>

<script>
import Stepper from "./components/Stepper";
export default {
  name: "App",
  components: {
    Stepper,
  },
};
</script>

<style>
#app {
  display: flex;
  justify-content: center;
  flex-direction: column;
}
</style>
