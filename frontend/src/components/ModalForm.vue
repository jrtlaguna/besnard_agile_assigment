<template>
  <div class="modal-form">
    <button
      @click="$emit('hide-modal')"
      class="btn btn-outline-danger close-button"
    >
      x
    </button>
    <form @submit.prevent="" class="form-body">
      <h3 class="text-uppercase">Add {{ this.type }}</h3>
      <div class="form-group">
        <label>Title</label>
        <input
          id="titleInput"
          style="font-weight: bold;"
          type="text"
          class="form-control"
          v-model="title"
        />
      </div>
      <div class="form-group">
        <label>Content</label>
        <textarea
          class="form-control"
          name="content"
          v-model="content"
          rows="4"
        ></textarea>
      </div>
      <div class="mt-3">
        <div v-if="!this.id">
          <button @click.prevent="submit('create')" class="btn btn-success">
            Add <span class="text-capitalize">{{ this.type }}</span>
          </button>
        </div>
        <div class="button-group" v-else>
          <button
            class="btn btn-outline-primary"
            @click.prevent="submit('update')"
          >
            Update
          </button>
          <button
            id="deleteButton"
            class="btn btn-outline-danger"
            @click.prevent="deleteContent"
          >
            Delete
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ModalForm",
  data() {
    return {
      title: "",
      content: "",
      type: "",
      id: Number,
    };
  },
  methods: {
    async submit(action = "create") {
      let res = null;
      const content = {
        title: this.title,
        content: this.content,
      };
      try {
        if (action == "create") {
          res = await axios.post(
            `api/values_principles/${this.type}s/`,
            content
          );
          this.$emit("refresh-data", this.type, res.data, action);
        } else {
          res = await axios.put(
            `api/values_principles/${this.type}s/${this.id}/`,
            content
          );
          this.$emit("refresh-data", this.type, res.data, action);
        }
      } catch (err) {
        alert(err);
      }
    },
    async deleteContent() {
      try {
        const res = await axios.delete(
          `api/values_principles/${this.type}s/${this.id}/`
        );
        if (res.status === 204) {
          this.$emit("remove-data", this.type, this.id);
        }
      } catch (err) {
        alert(err);
      }
    },
    viewData(data, type) {
      this.content = data.content;
      this.title = data.title;
      this.id = data.id;
      this.type = type;
    },
    addData(type) {
      this.content = "";
      this.title = "";
      this.id = null;
      this.type = type;
    },
  },
};
</script>

<style scoped lang="scss">
.modal-form {
  width: 80%;
  height: 50%;
  border-radius: 24px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-left: auto;
  margin-right: auto;
  padding-top: 0px;
  button:first-child {
    margin-left: auto;
    margin-right: 2rem;
  }
  &.form-group {
    margin-bottom: 3em;
  }
  &label {
    text-align: left;
  }
  background-color: white;
}

.button-group {
  button + button {
    margin-left: 1em;
  }
}

.form-body {
  max-width: 200rem;
  width: inherit;
}
.form-label {
  width: 60%;
  text-align: left;
}
/* .close-button {
  position: absolute;
  top: 16rem;
  right: 10rem;
  margin-right: auto;
  @media only screen and (min-width: 900px) {
    right: 20rem;
  }
} */
/* .close-button {
  width: inherit;
  position: absolute;
  width: 100%;
  top: 16rem;
  right: 6rem;
} */
.form-group {
  margin-top: 1rem;
}

label {
  font-size: 20px;
}
</style>
