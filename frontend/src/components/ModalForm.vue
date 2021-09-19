<template>
  <div class="modal-form">
    <button
      @click="$emit('hide-modal')"
      class="btn btn-outline-danger close-button"
    >
      x
    </button>
    <form class="form-body">
      <h3 class="text-uppercase">Add {{ this.type }}</h3>
      <div class="form-group">
        <label>Title</label>
        <input
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
          <button class="btn btn-outline-danger" @click.prevent="deleteContent">
            Delete
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "ModalForm",
  data() {
    return {
      title: String,
      content: String,
      type: String,
      id: Number,
    };
  },
  props: {
    data: Object,
  },
  methods: {
    async submit(action) {
      let res = null;
      const content = {
        title: this.title,
        content: this.content,
      };
      try {
        if (action == "create") {
          res = await fetch(`api/values_principles/${this.type}s/`, {
            method: "POST",
            headers: {
              "Content-type": "application/json",
            },
            body: JSON.stringify(content),
          });
        } else {
          res = await fetch(`api/values_principles/${this.type}s/${this.id}/`, {
            method: "PUT",
            headers: {
              "Content-type": "application/json",
            },
            body: JSON.stringify(content),
          });
        }
      } catch (e) {
        alert(e);
      }
      const data = await res.json();
      alert(`Successfully ${action}d ${this.type}.`);
      this.$emit("refresh-data", this.type, data, action);
    },
    async deleteContent() {
      try {
        const res = await fetch(
          `api/values_principles/${this.type}s/${this.id}/`,
          {
            method: "DELETE",
          }
        );
        if (res.status === 204) {
          this.$emit("remove-data", this.type, this.id);
        }
      } catch (e) {
        alert(e);
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
  margin-left: auto;
  margin-right: auto;
  padding-top: 0px;
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
  min-width: 50rem;
}
.form-label {
  width: 60%;
  text-align: left;
}
.close-button {
  position: fixed;
  top: 18rem;
  right: 10rem;
  margin-right: auto;
}
.form-group {
  margin-top: 1rem;
}

label {
  font-size: 20px;
}
</style>
