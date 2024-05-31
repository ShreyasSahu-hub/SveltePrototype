import { c as create_ssr_component } from "../../../chunks/ssr.js";
const Layout = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<nav class="navbar navbar-expand-lg navbar-light bg-light" data-svelte-h="svelte-1i4we8s"><div class="container-fluid"><a class="navbar-brand" href="/mainpage">Navbar</a> <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button> <div class="collapse navbar-collapse" id="navbarNav"><ul class="navbar-nav"><li class="nav-item"><a class="nav-link" href="/mainpage/CalorieTracker">Calorie Tracker</a></li> <li class="nav-item"><a class="nav-link" href="/mainpage/FetchingExercisingVideos">Fetching exercise videos</a></li></ul></div></div></nav> <div class="container">${slots.default ? slots.default({}) : ``}</div>`;
});
export {
  Layout as default
};
