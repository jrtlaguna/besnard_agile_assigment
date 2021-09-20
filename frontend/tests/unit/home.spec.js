import Home from "@/components/Home.vue";
import ModalForm from "@/components/ModalForm.vue";
import { shallowMount } from "@vue/test-utils";
import flushPromises from "flush-promises";

jest.mock("axios", () => ({
  get: () =>
    Promise.resolve({
      data: [
        { id: 1, title: "Mocked title", description: "Mocked description" },
      ],
    }),
}));

describe("home.vue", () => {
  const wrapper = shallowMount(Home);

  wrapper.find("button");

  it("shows app header", () => {
    expect(wrapper.find("h3").text()).toBe(
      "Values and Principles of Agile Development"
    );
  });

  it("mocking the axios call to get data", async () => {
    await flushPromises();
    expect(wrapper.vm.values.length).toBe(1);
  });

  it("does not show ModalForm", () => {
    expect(wrapper.findComponent(ModalForm).isVisible()).toBe(false);
  });
  it("shows content list", () => {
    const contentList = wrapper.find("div .content-list");
    expect(contentList.classes()).toContain("content-list");
  });
});
