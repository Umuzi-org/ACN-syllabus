---
content_type: topic
ready: true
title: Understanding Effective Comments in Coding
---

## Introduction

In programming, comments play a crucial role in code documentation. They provide explanations, clarifications, and additional context to make the code more understandable for developers. However, not all comments are created equal. It is important to distinguish between good comments and bad comments to ensure effective code communication. Let's explore what makes a comment good or bad.

### Characteristics of a Good Comment

- Purposeful Explanation: A good comment serves the purpose of explaining complex logic, algorithms, or business rules. It provides insights into the code's functionality and helps other developers understand the intentions behind certain decisions.

  ```python
  # Function to calculate the factorial of a number using recursion
  # This approach utilizes the mathematical definition of factorial
  # and may cause a stack overflow for large input values.
  def factorial_recursive(n):
      if n == 0:
          return 1
      else:
          return n * factorial_recursive(n - 1)

  ```

  > In this example, the comment above the function provides a purposeful explanation of what the function does, clarifies the approach used (recursion), and warns about the potential issue of stack overflow for large input values.

- Clarity and Readability: A good comment is clear, concise, and easy to read. It uses proper grammar, punctuation, and formatting conventions. Well-structured comments make it easier for developers to follow the code and comprehend its meaning.

- Relevant Information: A good comment provides relevant information that is not immediately apparent from the code itself. It adds value by offering insights, reasoning, or describing the intention behind a particular approach or solution.

  ```python
  # Calculate the total price of items in the shopping cart
  total_price = 0

  for item in shopping_cart:
      subtotal = item.price * item.quantity
      total_price += subtotal

  # Apply a discount if the total price exceeds the spending_limit
  if total_price > spending_limit:
      discount = total_price * 0.1  # 10% discount for exceeding the spending_limit
      total_price -= discount

  ```

  > In this example, the comment explains the purpose of the code, which is to calculate the total price of items in a shopping cart and apply a discount if the total price exceeds the spending limit. It clarifies the logic behind the code and provides insight into the discount calculation, which might not be immediately obvious from the code itself. The comment adds relevant information that helps other developers understand the intention and behaviour of the code segment.

- Updates with Code Changes: A good comment is maintained and updated alongside the code. If the code undergoes modifications, the corresponding comments should be reviewed and revised to ensure they accurately reflect the updated logic.

- Avoidance of Redundancy: A good comment avoids repeating what is already evident from the code. It focuses on explaining aspects that may not be immediately obvious, such as complex algorithms or non-standard approaches.

### Characteristics of a Bad Comment

- Irrelevance: A bad comment lacks relevance to the code or provides information that is obvious from reading the code itself. Irrelevant comments clutter the codebase and can confuse or mislead developers.

  ```java
  int x = 10; // Initialize the variable x with a value of 10
  ```

  > In this example, the comment adds little value since the code itself is self-explanatory. The comment is redundant and does not provide any additional insight or explanation.

- Outdated or Inaccurate Information: A bad comment contains outdated or incorrect information. If a comment no longer aligns with the current code logic or behaviour, it becomes misleading and should be removed or updated accordingly.

  ```javascript
  // Function to calculate the square of a number
  // (Note: We are using the old approach for squaring, use the new one instead)
  function square(number) {
    return number * number;
  }
  ```

  > In this example, the comment contains outdated information, suggesting there's a newer approach for squaring numbers. However, the code remains unchanged, making the comment misleading. It's important to keep comments up-to-date with the code logic.

- Vague or Ambiguous Descriptions: A bad comment fails to provide clear explanations or uses ambiguous language. Unclear comments can cause confusion and hinder code comprehension instead of enhancing it.

- Excessive or Unnecessary Comments: A bad comment includes excessive or unnecessary explanations that only add noise to the code. Comments should be used sparingly, focusing on areas that genuinely require clarification or insight.

- Sarcasm, Insults, or Personal Opinions: A bad comment contains sarcasm, insults, or personal opinions that are unprofessional and create a negative work environment. Comments should maintain a respectful and collaborative tone.

  ```csharp
  // This brilliant piece of code magically fixes the bug!
  int result = Divide(10, 0);
  ```

  > In this example, the comment uses sarcasm and an unprofessional tone, which can create a negative work environment and undermine effective collaboration.

### Self-Documenting Code

 An essential aspect of effective code communication is self-documenting code. Good code makes its intentions clear through various means:

- Clear Algorithms: Well-organized and logically structured algorithms help developers understand the flow and purpose of the code without relying heavily on comments.

- Well-Chosen Names: Thoughtfully selected variable and function names that convey their purpose can significantly improve code readability. Meaningful names reduce the need for excessive comments by expressing the code's intent directly.

A common problem is something like this:
  
  ```javascript
  // Calculate the temperature in Fahrenheit given the temperature in Celsius
  function calculate(temp) {
      return .... 
  }
  ```

  > In this example, the comment is redundant since the function name already conveys its purpose. A better approach would be to use a more descriptive function name, such as `calculateFahrenheitFromCelcius`.

Comments as Needed: While striving for self-documenting code, there will still be instances where comments are necessary to provide critical context or explain intricate details that may not be immediately obvious.

### Common Problems Encountered by New Programmers

- Paraphrasing Code in Comments: New programmers often fall into the trap of paraphrasing code in comments, leading to redundant and unhelpful comments. For instance: `sum = 0 // initialize the sum variable to 0`. Comments like these add no real value and clutter the codebase.

- Omitting Comments Completely: Some new programmers may receive feedback discouraging them from making useless comments, which can result in the omission of comments altogether. While overly verbose or redundant comments should be avoided, omitting all comments can make the code harder to understand, especially for others who may work on the codebase in the future.

### Conclusion

Understanding the difference between good comments and bad comments is essential for effective code communication and collaboration. Good comments provide purposeful explanations, relevant information, and clarity, while avoiding redundancy and outdated content. By following these principles, developers can create comments that enhance code comprehension, facilitate maintenance, and promote a positive coding environment.
