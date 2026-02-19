module.exports = {
  name: 'searchSkills',
  execute: async (query) => {
    // TODO: call Kaspa on-chain query
    console.log(`Searching skills for: ${query}`);
    return ['example-skill-1', 'example-skill-2'];
  }
};