

export const index = 5;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/mainpage/calorieHistory/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/5.BXAickni.js","_app/immutable/chunks/scheduler.CvSFXg4c.js","_app/immutable/chunks/index.ClWzMdZj.js"];
export const stylesheets = [];
export const fonts = [];
