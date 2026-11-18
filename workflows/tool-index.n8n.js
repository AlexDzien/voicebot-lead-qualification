// JavaScript for an n8n Code node. Runtime input: items from the Vapi tool list.
const tools = items.map(item => item.json);
const output = {};

tools.forEach((tool, index) => {
  output[`id${index + 1}`] = tool.id;
});

return [{ json: output }];
