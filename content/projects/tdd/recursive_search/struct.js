const DIR = "dir";
const FILE = "file";

const root = {
  name: "home",
  type: DIR,
  children: [
    {
      name: "house_cats.mov",
      type: FILE
    },
    {
      name: "movies",
      type: DIR,
      children: [
        {
          name: "horror",
          type: DIR,
          children: [
            {
              name: "really_awful_cats.mp4",
              type: FILE
            }
          ]
        },
        {
          name: "adventure",
          type: DIR,
          children: [
            {
              name: "adventure_cats.mov",
              type: FILE
            },
            {
              name: "adventure_dogs.mov",
              type: FILE
            }
          ]
        },
        {
          name: "tragedy",
          type: DIR,
          children: [{ name: "a sad story about cats.md", type: FILE }]
        }
      ]
    },
    {
      name: "workspace",
      type: DIR,
      children: [
        {
          name: "grumpy_cats.mp4",
          type: FILE
        }
      ]
    }
  ]
};
