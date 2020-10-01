var jsdom = require("jsdom");

function winning() {
  // This is the function under test. Put it somewhere that makes sense and "require" it here
  document.getElementById("booya").innerHTML = "so cool";
}

describe("FooFighters", function() {
  beforeEach(function() {
    // make a fake DOM to interact with
    const dom = new jsdom.JSDOM('<html><body id="booya">initial</body></html>');
    global.document = dom.window.document;
    global.window = dom.window;
    global.navigator = dom.window.navigator;
  });

  it("updates dom", function() {
    expect(global.document.getElementById("booya").innerHTML).toBe("initial");
    winning(); // call the function that updates the dom
    expect(global.document.getElementById("booya").innerHTML).toBe("so cool");
  });
});
