

export const index = 2;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/mainpage/_layout.svelte.js')).default;
export const imports = ["_app/immutable/nodes/2.CPTOHc9_.js","_app/immutable/chunks/scheduler.CvSFXg4c.js","_app/immutable/chunks/index.ClWzMdZj.js"];
export const stylesheets = [];
export const fonts = [];
