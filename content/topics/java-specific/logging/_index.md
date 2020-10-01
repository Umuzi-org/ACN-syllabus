---
_db_id: 101
content_type: topic
ready: true
title: Java Logging with Log4j
---

Please make sure you read and understand this before moving forward: {{% contentlink path="/topics/logging" %}}

Ok, so now you know about what logging is and why we do it, we're going to dig a bit more into some specific details about how to do this stuff in Java.

## Installing Log4j

We are using IntelliJ and Gradle. This means we have a specific way of including Log4j in our projects.

The first thing you need to do is make sure you have added Log4j as a dependency on your project. Take a look [here](https://docs.gradle.org/current/userguide/declaring_dependencies.html) and [here](https://logging.apache.org/log4j/2.x/maven-artifacts.html) to see how to add Log4j to your project.

Now make a new project and log some stuff:

```
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class MainProgram {
    private static final Logger logger = LogManager.getLogger(MainProgram.class.getName());

    public static void main(String[] args){
        logger.debug("Hello this is a debug message");
        logger.info("Hello this is an info message");
        logger.warn("Hello this is a warning message");
        logger.error("Hello this is an error message");
        logger.fatal("Hello this is a fatal message"); // some languages call this level "critical"
    }
}
```

If you run this then you'll see some of the messages get logged to the standard output. But you'll also see an error message.

IntlliJ will show you an error message that says "ERROR StatusLogger No Log4j 2 configuration file found. Using default configuration (logging only errors to the console), ..."

Now make a new file in the resources firectory and name it `log4j2-test.properties`. Here's what it should look like:

```
appender.console.name = STDOUT
appender.console.type = Console
appender.console.layout.type = PatternLayout
appender.console.layout.pattern = %d | %c: %m%n

rootLogger.level = debug
rootLogger.appenderRef.stdout.ref = STDOUT
```

Save it and run your program again. Now all the logs should show up with some fancy formatting.

## Conclusion

We just scratched the surface here. Try use logging for now on instead of just `System.out.println`. In industry you'll have to get used to logging things in a thoughtful way.

## Resources

- [The official docs](https://logging.apache.org/log4j/2.x/manual/api.html)
- [Info on log layout patterns](https://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/PatternLayout.html)
- [Config properties syntax](https://logging.apache.org/log4j/2.x/manual/configuration.html#Properties)