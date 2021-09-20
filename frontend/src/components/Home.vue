<template>
  <div class="justify-content-around">
    <h3 class="mb-3">Values and Principles of Agile Development</h3>
    <div
      v-show="showModal"
      class="formModal"
      @keydown.esc="hideModal"
      tabindex="0"
    >
      <ModalForm
        @refresh-data="refreshData"
        @hide-modal="hideModal"
        @remove-data="removeData"
        ref="modal"
      />
    </div>
    <div class="content-list">
      <div class="d-flex justify-content-between mx-4">
        <h3>Values</h3>
        <button
          class="btn btn-outline-primary"
          id="add-value"
          @click="addContent('value')"
        >
          <i class="bi bi-plus-circle" /> Add Value
        </button>
      </div>
      <ContentList
        @view-content="viewContent"
        :contents="values"
        type="value"
        :key="values"
      />
    </div>
    <hr />
    <div class="content-list mt-4">
      <div class="d-flex justify-content-between mx-4">
        <h3>Principles</h3>
        <button
          class="btn btn-outline-primary"
          id="add-principle"
          @click="addContent('principle')"
        >
          <i class="bi bi-plus-circle" /> Add Principle
        </button>
      </div>
      <ContentList
        @view-content="viewContent"
        :contents="principles"
        type="principle"
        :key="principles"
      />
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import axios from "axios";
import ContentList from "@/components/ContentList.vue";
import ModalForm from "@/components/ModalForm";

export default {
  setup() {
    const modal = ref(null);
    return { modal };
  },
  components: {
    ModalForm,
    ContentList,
  },
  data() {
    return {
      principles: [],
      values: [],
      data: Object,
      type: String,
      showModal: false,
    };
  },
  methods: {
    async fetchPrinciples() {
      try {
        const res = await axios.get("api/values_principles/principles/");

        return res.data;
      } catch (e) {
        alert(e);
      }
    },
    async fetchValues() {
      try {
        const res = await axios.get("/api/values_principles/values/");
        return res.data;
      } catch (e) {
        alert(e);
      }
    },
    async viewContent(content, type) {
      this.showModal = !this.showModal;

      this.$refs.modal.viewData(content, type);
    },
    hideModal() {
      if (this.showModal) {
        this.data = null;
        this.showModal = false;
      }
    },
    addContent(type) {
      this.$refs.modal.addData(type);
      this.showModal = true;
    },
    refreshData(type, data, action) {
      this.hideModal();
      console.log();

      if (action == "create") {
        if (type == "value") {
          this.values = [...this.values, data];
          console.log(this.values);
        } else {
          this.principles = [...this.principles, data];
        }
      } else {
        if (type === "principle") {
          this.principles = this.principles.map((principle) =>
            principle.id === data.id ? { ...data } : principle
          );
        } else {
          this.values = this.values.map((value) =>
            value.id === data.id ? { ...data } : value
          );
        }
      }
    },
    removeData(type, id) {
      this.hideModal();
      console.log(type);
      if (type == "value") {
        this.values = this.values.filter((value) => value.id != id);
      } else {
        this.principles = this.principles.filter(
          (principle) => principle.id != id
        );
      }
    },
  },
  name: "Home",
  async created() {
    this.principles = await this.fetchPrinciples();
    this.values = await this.fetchValues();
  },
};
</script>

<style scoped>
.container {
  box-shadow: 0px 3px 3px 1.5px #888888;
}

.content-list > h3 {
  margin-left: 5rem;
  text-align: left;
}

hr {
  width: 80%;
  margin-left: auto;
  margin-right: auto;
}

.container > * {
  margin-block: 1rem;
}

.formModal {
  position: fixed; /* Sit on top of the page content */
  width: 100%; /* Full width (cover the whole page) */
  height: 100%; /* Full height (cover the whole page) */
  display: flex;
  align-items: center;
  justify-content: center;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5); /* Black background with opacity */
  z-index: 2;
}
</style>
