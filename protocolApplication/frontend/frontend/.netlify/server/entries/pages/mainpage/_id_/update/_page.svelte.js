import { c as create_ssr_component, d as add_attribute } from "../../../../../chunks/ssr.js";
import "../../../../../chunks/client.js";
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let name = "";
  let date = "";
  let startTime = "";
  let amountOfTime = "";
  let descriptionOfTheTask = "";
  let { data } = $$props;
  if ($$props.data === void 0 && $$bindings.data && data !== void 0)
    $$bindings.data(data);
  return `<div><h2 class="my-4" data-svelte-h="svelte-15zh35r">Update a Task</h2> <div class="col-12 col-md-6"><form><div class="mb-3"><legend for="name" data-svelte-h="svelte-2ll0t4">Enter the name of the task</legend><br> <input class="form-control" type="text" id="name1" placeholder="name"${add_attribute("value", name, 0)}></div> <div class="mb-3"><legend for="date" data-svelte-h="svelte-ismxqo">Enter the date to start the task</legend><br> <input class="form-control" type="date" id="date1" placeholder="date"${add_attribute("value", date, 0)}></div> <div class="mb-3"><legend for="time" data-svelte-h="svelte-whjzws">Enter the time to start the task</legend><br> <input class="form-control" type="time" id="startTime1" placeholder="start Time"${add_attribute("value", startTime, 0)}></div> <div class="mb-3"><legend for="amountOfTime" data-svelte-h="svelte-4o6d26">Enter the amount of time to spend the task</legend><br> <input class="form-control" type="time" id="amountOfTime1" placeholder="Amount of to spend"${add_attribute("value", amountOfTime, 0)}></div> <div class="mb-3"><legend for="descriptionOfTheTask" data-svelte-h="svelte-4q5tui">Write the description of the task</legend><br> <input class="form-control" type="text" id="descriptionOfTheTask1" placeholder="description of the task"${add_attribute("value", descriptionOfTheTask, 0)}></div> <div class="mb-3"><legend for="uploadingTheImage" data-svelte-h="svelte-ykcx6a">Upload the image</legend><br> <input class="form-control" id="image" type="file"></div> <button class="btn btn-primary" type="submit" data-svelte-h="svelte-1b10frf">Submit</button></form></div></div>`;
});
export {
  Page as default
};
