---
title: Introduction to mobile development 
content_type: topic
ready: True
---

Now that you know a bit more about web development, you can more easily understand mobile development.

## Web apps versus mobile apps

Mobile apps and web apps are both applications that can run on a device such as a smartphone or a tablet. However, there are key differences between the two.

### Mobile Apps

Mobile apps are applications that are downloaded and installed on a mobile device rather than being rendered within a browser. They are platform-specific (e.g., Android apps, iOS apps), and need to be released separately for each platform. They can take full advantage of all the device features — they can use the camera, the GPS, the accelerometer, the compass, the list of contacts, and so on. They can also incorporate gestures (either standard operating-system gestures or new, app-defined gestures).

Mobile apps can use the device’s notification system and can work offline. Mobile apps have the advantage of being faster and more efficient, but they do require the user to download updates regularly.

Like web apps, mobile apps can interact with servers on the internet. Mobile apps can even interpret things like HTML and CSS if they are set up to do so. 

### Web Apps

Web apps, on the other hand, are accessed through the internet browser and will adapt to whichever device you’re viewing them on. They are not native to a particular system, and don't need to be downloaded or installed. Due to their responsive nature, they do indeed look and function a lot like mobile apps a lot of the time — and this is where the confusion arises.

In general, web apps might be a simpler and more economical option to reach a wide range of users across multiple platforms. However, for tasks that require more complexity and access to device capabilities, mobile apps can be the better choice.

## Web app advantages

Web apps have several advantages over mobile apps:

1. **Cross-platform Compatibility**:  Web apps can run on any platform with a web browser, so they are accessible from a variety of devices regardless of the operating system. This is an advantage over mobile apps which have to be developed separately for each platform (e.g., Android, iOS).
2. **Easy Updates**: Updates to a web app can be made quickly and easily, without requiring users to download and install updates. Any changes made to the web app are instantly available to users the next time they visit the app.
3. **No App Store Approval**: Web apps don't need to go through an app store approval process. This means they can be released on your own schedule and have fewer restrictions on content and functionality. There are many horror stories out there about people and businesses sinking a lot of resources into building apps, only to have the app-store shut them down.
4. **Cost-Effective Development**: Because web apps need only a single version developed for universal use, the cost of development and maintenance is often less than for equivalent native mobile apps.
5. **Easy to find dev talent**: Web development skills are much easier to find. Hiring specialized mobile developers tends to be harder and more expensive.
6. **No Installation Required**: Users do not need to download and install web apps on their devices, saving storage space.
7. **Easy to Find**: Web apps are easy to share and find because they can be linked to from anywhere on the web. Users can simply click a link to access the app, rather than having to search for it in an app store.
8. **SEO Friendly**: Web apps can be indexed by search engines, making it easier for people to find your app, whereas mobile apps are not typically indexed by search engines.
9. **Access to Most Native Features**: Even though web apps can't access ALL mobile native features, they can access quite a lot of them. Web apps are good for many use cases. 

## Reasons to develop a mobile app instead of a web app

Developing a mobile app instead of a web app can make sense in several situations:

1. **Access to Device Features**: Mobile apps can access and utilize more of a a device's built-in features than a web app can. Although web apps have quite a lot of capabilities, they can't do everything
2. **Offline Access**: Mobile apps can be used offline, which is important if you need to provide access to content or functionalities without an internet connection. That said, web apps do have some offline capabilities - do some reading up on PWAs to learn more
3. **Performance**: Mobile apps are generally faster and more efficient as they are designed for specific platforms and take advantage of the device's processing capabilities. This can lead to a smoother, more responsive user experience.
4. **User Experience**: Mobile apps allow for a more tailored user experience. They can be designed to take full advantage of the device's screen size and resolution, and can offer gestures like swiping, pinching, and tapping more easily than web apps can. Additionally, a mobile app stays in your device's app drawer, which could lead to more frequent usage due to better visibility.
5. **Branding**: Having a mobile app can enhance a brand's visibility as it is easier for users to remember and access. It also provides an opportunity to design a unique app icon that can stand out on the user's device.
6. **E-commerce and In-app Purchases**: Mobile platforms have built-in systems for handling transactions, which can be easier to use and more secure for users. This can be important for apps that rely on in-app purchases, subscriptions, or e-commerce.

Remember, whether a mobile app or a web app is more suitable largely depends on the specific needs, goals, and target audience of the project. It's also worth noting that many businesses opt for a hybrid approach, providing both a web app and a mobile app to reach the widest possible audience and provide the best user experience in different contexts.

## Platform decisions

When developing a mobile app you need to make a lot of decisions. The first one is, what platform(s) will you support?

Android and iOS are the big ones, but there are many more.

A good way to decide is by looking at stats about how common the different devices are. [Here](https://www.statista.com/statistics/1045247/share-of-mobile-operating-systems-in-africa-by-month/#:~:text=Google's%20Android%20is%20the%20leader,share%20in%20the%20same%20period.) is a good resource.

As you can see, Android is king in Africa. 

## Choosing a tool to build in

Mobile development tools can be categorized based on the approach they take to create apps. Here are the three major categories:

### 1. Native Mobile Development Tools 

These tools are used to develop apps for a specific mobile operating system. They allow developers to leverage the full capabilities of the hardware and the operating system's features. As a result, native apps typically provide the best performance and user experience. However, they require separate codebases for each operating system, which can increase development time and cost. Examples of native mobile development tools are:

- Android: Android Studio (with Java or Kotlin)
- iOS: Xcode (with Objective-C or Swift)

### 2. Hybrid Mobile Development Tools (Web Views) 

These tools allow developers to create apps using web technologies (HTML, CSS, and JavaScript), which are then run within a WebView (a native container that can display web content) inside a native app shell. This enables a single codebase to be used across multiple platforms, reducing development time and cost. However, these apps may not offer the same performance or access to operating system features as native apps. Examples of these tools are:

- Apache Cordova (formerly PhoneGap)
- Ionic

### 3. Cross-Platform Mobile Development Tools (Native Components)
 
These tools represent a middle ground between native and hybrid development. They allow developers to write code in a single language, which is then translated into native code for each operating system. This means that they can use a single codebase, while still providing a near-native user experience. Examples of these tools are:

- React Native: Write in JavaScript, render native components
- Flutter: Write in Dart, render native components
- Xamarin: Write in C#, render native components

### Summary 

Each of these categories has its own strengths and weaknesses, and the best choice depends on factors such as the project requirements, the team's expertise, the desired user experience, and the budget.