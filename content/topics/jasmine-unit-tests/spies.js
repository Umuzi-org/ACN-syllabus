class Thing {
  constructor() {
    this.a = "some initial value";
  }

  setA(newA) {
    this.a = newA;
  }
}


describe("Spies", function() {

    it("doesn't do surprising things", function() {
        var o = new.Thing();
        expect(o.a).toBe("some initial value");
    
        o.setA("x");
    
        expect(o.a).toBe("x");
      });

    it("mocks", function() {
      var o = new Thing();
      spyOn(o, "setA");    // spy on the function
      expect(o.a).toBe("some initial value");
  
      o.setA("x"); // o.setA has been replaced with a spy
      o.setA("x");
      o.setA("x");
      o.setA("x");
  
      expect(o.setA).toHaveBeenCalledTimes(4);  
      // we can check how many times it was called. 
      // we can even check what arguments were passed to this function

      // setA now has no side effect
      expect(o.a).toBe(1);
    });
  });
  
