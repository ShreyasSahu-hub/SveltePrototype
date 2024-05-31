

export const index = 4;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/mainpage/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/4.D3qSmzLl.js","_app/immutable/chunks/scheduler.CvSFXg4c.js","_app/immutable/chunks/index.ClWzMdZj.js","_app/immutable/chunks/entry.D9rars2n.js"];
export const stylesheets = ["_app/immutable/assets/6.DZ_T1SZp.css"];
export const fonts = [];
