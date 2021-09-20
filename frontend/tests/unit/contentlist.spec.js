import ContentList from "@/components/ContentList.vue";
import { mount } from "@vue/test-utils";

describe("ContentList", () => {
  const wrapper = mount(ContentList);

  wrapper.setProps({
    contents: [{ id: 1, title: "test title", content: "test content" }],
    type: "values",
  });

  it("shows title class", () => {
    expect(wrapper.classes()).toContain("title");
  });

  it("shows content title", () => {
    expect(wrapper.find("h3").text()).toBe("test title");
  });

  it("shows content contains", () => {
    expect(wrapper.find("p").text()).toBe("test content");
  });
});
