---
_db_id: 297
content_type: topic
prerequisites:
  hard:
  - topics/kotlin/nested-classes
  soft: []
ready: true
title: Enum Classes
---

The most basic usage of enum classes is implementing type-safe enums
````
enum class Direction {
    NORTH, SOUTH, WEST, EAST
    }
````
Each enum constant is an object. Enum constants are separated with commas.

## Initialization
Since each enum is an instance of the enum class, they can be initialized
````
 enum class Color(val rgb: Int) {
    RED(0xFF0000),
    GREEN(0x00FF00),
    BLUE(0x0000FF)
    }
````
## Anonymous Classes
Enum constants can also declare their own anonymous classes
````
enum class ProtocolState {
    WAITING {
    override fun signal() = TALKING
    },

    TALKING {
    override fun signal() = WAITING
    };

    abstract fun signal(): ProtocolState
    }
````
with their corresponding methods, as well as overriding base methods. Note that if the enum class defines any members, you need to separate the enum constant definitions from the member definitions with a semicolon, just like in Java.