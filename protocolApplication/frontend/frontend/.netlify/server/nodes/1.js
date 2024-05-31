

export const index = 1;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/fallbacks/error.svelte.js')).default;
export const imports = ["_app/immutable/nodes/1.C_u6ebAz.js","_app/immutable/chunks/scheduler.CvSFXg4c.js","_app/immutable/chunks/index.ClWzMdZj.js","_app/immutable/chunks/entry.D9rars2n.js"];
export const stylesheets = [];
export const fonts = [];
