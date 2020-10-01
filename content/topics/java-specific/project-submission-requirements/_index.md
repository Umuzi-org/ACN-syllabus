---
_db_id: 123
content_type: topic
title: Java project submission requirements
---

As a junior developer working on a team of professionas, your code will always have to conform to a certain shape. You will always need to write code that plays nicely with the code and mechanisms that are in place.

For all your Java projects you will need to make sure that your code conforms to the following:

## Build.Gradle

We are using JUnit 5. And some of our automations depend on how JUnit 5 logs its successes.

Please open up your `build.gradle`. Make sure that you have the JUnit5 dependencies listed below.

```
dependencies {
    testImplementation 'org.junit.jupiter:junit-jupiter-api:5.3.1'
    testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine:5.3.1'
    // your project dependencies
}
```

Then paste this into your build.gradle file.

```
test {
    useJUnitPlatform(
        testLogging {
		events "passed", "skipped", "failed"
	}
    )
}
```

Now if you run your unit tests and everything passes (which they should before you submit your work) then you will get a bit of extra output about your passing tests.

## Directory structure

Please see this: {{% contentlink path="topics/java-specific/gradle-and-intellij-project-structure" %}}