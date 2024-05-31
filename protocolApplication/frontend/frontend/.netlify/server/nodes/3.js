

export const index = 3;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/3._IzL8vZV.js","_app/immutable/chunks/scheduler.CvSFXg4c.js","_app/immutable/chunks/index.ClWzMdZj.js"];
export const stylesheets = [];
export const fonts = [];
