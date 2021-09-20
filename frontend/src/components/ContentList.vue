<template>
  <div class="title">
    <div
      @click="$emit('view-content', content, type)"
      class="content-card"
      v-bind:class="[this.type == 'principle' ? 'principle' : '']"
      :key="content.id"
      v-for="content in contents"
    >
      <div>
        <h3>{{ content.title }}</h3>
      </div>
      <div>
        <p class="content">{{ content.content }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ContentList",
  props: {
    contents: Array,
    type: String,
  },
  emits: ["view-content"],
};
</script>

<style scoped lang="scss">
h3 {
  text-align: left;
}
.skeleton {
  opacity: 0.7;
  animation: skeleton-loading 1s linear infinite alternate;
}
.title {
  border-radius: 25px;
  padding: 10px 20px;
}
.content {
  text-align: justify;
}

.content-card {
  display: block;
  top: 0px;
  position: relative;
  background-color: #f2f8f9;
  border-radius: 4px;
  padding: 32px 24px;
  margin: 12px;
  text-decoration: none;
  z-index: 0;
  overflow: hidden;
  border: 1px solid #f2f8f9;

  &.principle {
    background-color: #cdf5ff;
  }

  &:hover {
    transition: all 0.2s ease-out;
    box-shadow: 0px 4px 8px rgba(38, 38, 38, 0.2);
    top: -4px;
    border: 1px solid #cccccc;
    background-color: white;
    cursor: pointer;
  }

  &:before {
    padding-top: 10px;
    width: 5em;
    font-size: 10px;
    content: "";
    position: absolute;
    z-index: -1;
    top: 0px;
    right: 1em;
    background: #00838d;
    transform: scale(2);
    transform-origin: 50% 50%;
    transition: transform 1s ease-out;
  }
}
</style>
