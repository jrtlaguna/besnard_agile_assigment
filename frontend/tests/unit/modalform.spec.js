import ModalForm from "@/components/ModalForm.vue";
import flushPromises from "flush-promises";
import { mount } from "@vue/test-utils";
import axios from "axios";

jest.mock("axios", () => ({
  post: jest.fn(() => {}),
  put: jest.fn(() => {}),
  delete: jest.fn(() => {}),
}));

window.alert = jest.fn();

const mockData = {
  id: 1,
  title: "Test title",
  content: "Test content principle",
};

describe("ModalForm.vue without data", () => {
  const wrapper = mount(ModalForm, {
    data() {
      return {
        title: "",
        content: "",
        type: "principle",
        id: null,
      };
    },
    propsData: {
      data: mockData,
    },
  });

  it("shows empty title input", () => {
    expect(wrapper.find('input[type="text"]').text()).toBe("");
  });
  it("shows empty content input", () => {
    expect(wrapper.find("textarea").text()).toBe("");
  });
  it("shows close button", () => {
    expect(wrapper.find("button").classes()).toContain("close-button");
  });
  it("shows submit button", () => {
    expect(wrapper.find(".btn-success").text()).toBe("Add principle");
  });

  it("mocks axios post request by create", async () => {
    await wrapper.setData({
      title: "test Title",
      content: "Test content",
      type: "principle",
    });
    await wrapper.vm.submit("create");
    await flushPromises();
    window.alert.mockClear();
    expect(axios.post).toHaveBeenCalledTimes(1);
  });
});

describe("ModalForm.vue with data", () => {
  const wrapper = mount(ModalForm, {
    data() {
      return {
        title: "",
        content: "",
        type: "",
        id: Number,
      };
    },
  });
  it("test", async () => {
    await wrapper.setData({ id: 1 });
    expect(wrapper.vm.id).toBe(1);
  });

  it("shows current title inside input", async () => {
    await wrapper.find("input").setValue(mockData.title);
    expect(wrapper.find("input").element.value).toBe("Test title");
  });
  it("shows current content input", async () => {
    await wrapper.find("textarea").setValue(mockData.content);
    expect(wrapper.find("textarea").element.value).toBe(
      "Test content principle"
    );
  });

  it("shows update button", async () => {
    await wrapper.setData({
      id: 1,
    });
    expect(wrapper.find(".btn-outline-primary").text()).toBe("Update");
  });

  it("shows delete button", async () => {
    await wrapper.setData({
      id: 1,
    });
    expect(wrapper.find("#deleteButton").text()).toBe("Delete");
  });

  it("mocks axios delete request of a principle", async () => {
    await wrapper.setData({
      id: 1,
      title: "test Title",
      content: "Test content",
      type: "principle",
    });
    await wrapper.vm.deleteContent();
    await flushPromises();
    expect(axios.delete).toHaveBeenCalledTimes(1);
  });

  it("mocks axios put request of a principle", async () => {
    await wrapper.setData({
      id: 1,
      title: "test Title",
      content: "Test content",
      type: "principle",
    });
    await wrapper.vm.submit("update");
    await flushPromises();
    expect(axios.put).toHaveBeenCalledTimes(1);
  });
});
