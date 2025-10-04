[15 Prompting Techniques Every Developer Should Know for Code Generation](https://medium.com/@dnagasuresh1992?source=post_page---byline--0ddadd2be8f2---------------------------------------)

## Introduction

Prompt engineering has become crucial for effective code generation. By crafting well-structured prompts, you can guide Large Language Models (LLMs) to generate, refine, and optimize your application’s code. In this post, we’ll walk through 15 proven prompting techniques — classified into **root**, **refinement-based**, **decomposition-based**, **reasoning-based**, and **priming**. Each technique will be exemplified through the process of creating and improving a simple Flask web application.

## Get nagasuresh’s stories in your inbox

Join Medium for free to get updates from this writer.

We will begin with a basic “Hello World” Flask app, then enhance it step-by-step — showing how each technique can systematically refine or expand the capabilities of the generated code.

## 1\. Root Techniques

Root techniques are basic prompting methods that provide a clear, direct path to obtaining simple code outputs.

## 1.1. Direct Instruction Prompting

**Overview**

- You give a straightforward command without additional details or context.

**Prompt Example**

> _“Generate a minimal Flask app in Python that displays ‘Hello World!’ at the root endpoint.”_

**Generated Code (Conceptual)**

```
from flask import Flask
```

```
app = Flask(__name__)@app.route('/')def hello_world():    return "Hello World!"if __name__ == '__main__':    app.run(debug=True)
```

**Why It Works**

- A direct, concise instruction is often enough for smaller tasks.
- **How It Improves**: This sets the **foundation** for further enhancements in subsequent techniques.

## 1.2. Query-Based Prompting

**Overview**

- You pose a request as a question, encouraging an explanatory answer or code snippet.

**Prompt Example**

> _“How can I create a minimal Flask app that returns ‘Hello World!’ on the home page?”_

**Generated Response (Conceptual)**

- The model might return not only the code snippet but also an explanation of each step involved in creating the Flask app.

**Why It Works**

- Asking a question can encourage LLMs to be more informative.
- **How It Improves**: Compared to direct instruction, you get additional **context** or **justification** for the code.

## 1.3. Example-Based Prompting

**Overview**

- You provide an example of the desired style or format, so the model understands the structure you expect.

**Prompt Example**

> _“Here is a simple Node.js Express ‘Hello World’ server:_

```
const express = require('express');const app = express();app.get('/', (req, res) => res.send('Hello World!'));app.listen(3000, () => console.log('Example app listening on port 3000!'));
```

> _Create a similar ‘Hello World’ server in Flask.”_

**How It Improves**

- The model can **mirror** the structure and coding style from your example, ensuring consistency across frameworks.
- This approach is more precise than a direct instruction because it anchors the output in a known pattern or style.

## 2\. Refinement-Based Techniques

Refinement-based techniques revolve around iterating over, improving, or polishing existing code.

## 2.1. Iterative Refinement Prompting

**Overview**

- You start with an initial solution (e.g., a minimal Flask app), then instruct the model to refine or enhance the code further.

**Sequence of Prompts**

1. _“Generate a minimal Flask app that returns ‘Hello World!’”_
2. _“Now, modify this Flask app to include a_ `_/hello/<name>_` _endpoint that greets the user by name."_

**Refined Code Snippet (Conceptual)**

```
from flask import Flask
```

```
app = Flask(__name__)@app.route('/')def hello_world():    return "Hello World!"@app.route('/hello/<name>')def hello_name(name):    return f"Hello, {name}!"if __name__ == '__main__':    app.run(debug=True)
```

**Why It Works**

- You build on top of existing code, guiding the model to **incrementally improve** it.
- **How It Improves**: This technique fosters an **iterative workflow**, enabling you to adapt and expand functionality in smaller steps.

## 2.2. Extension Prompting

**Overview**

- You specifically ask the model to add new features or sections to existing code.

**Prompt Example**

> _“Add an endpoint to the existing Flask app that returns a JSON response containing a list of sample users.”_

**Refined Code Snippet (Conceptual)**

```
@app.route('/users')def get_users():    users = [        {"id": 1, "name": "Alice"},        {"id": 2, "name": "Bob"}    ]    return {"users": users}
```

**Why It Works**

- Targets a single new feature, making it easy for the model to focus.
- **How It Improves**: More **granular control** than iterative refinement — perfect for **feature-based expansions**.

## 2.3. Style/Formatting Transformation

**Overview**

- You request modifications in style, such as PEP 8 compliance, naming conventions, or architectural patterns.

**Prompt Example**

> _“Take the current Flask app code and convert function names to follow PEP 8 naming (e.g.,_ `_hello_world_` _→_ `_hello_world_`_). Also, ensure line lengths do not exceed 79 characters.”_

**Why It Works**

- The model systematically applies your coding style preferences.
- **How It Improves**: After functionality is established, you can ensure the code meets **style guidelines** or other best practices — an essential step in production environments.

## 3\. Decomposition-Based Techniques

Decomposition-based prompts break large tasks into smaller steps, enhancing clarity and accuracy.

## 3.1. Function-by-Function Decomposition

**Overview**

- You separate complex tasks into multiple sub-functions or modules.

**Prompt Example**

1. _“Create a function_ `_init_db()_` _that initializes a SQLite database for the Flask app."_
2. _“Create a function_ `_insert_user(name)_` _that adds a user to the database."_
3. _“Create a function_ `_get_all_users()_` _that retrieves all users from the database."_

**Result (Conceptual)**

```
import sqlite3
```

```python
def init_db():    conn = sqlite3.connect('mydatabase.db')    c = conn.cursor()    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')    conn.commit()    conn.close()def insert_user(name):    conn = sqlite3.connect('mydatabase.db')    c = conn.cursor()    c.execute('INSERT INTO users (name) VALUES (?)', (name,))    conn.commit()    conn.close()def get_all_users():    conn = sqlite3.connect('mydatabase.db')    c = conn.cursor()    c.execute('SELECT id, name FROM users')    results = c.fetchall()    conn.close()    return results
```

**How It Improves**

- Organizes large tasks into **modular** pieces, making them **easier to maintain**.
- Encourages systematic code generation.

## 3.2. Chunk-Based Prompting

**Overview**

- You provide partial code and ask the model to fill in specific missing sections.

**Prompt Example**

> _“Below is the start of a Flask app. Fill in the missing routes for adding a user and retrieving all users from the database.”_

```
from flask import Flask, requestfrom db_utils import init_db, insert_user, get_all_users
```

```
app = Flask(__name__)init_db()# TODO: Add routes hereif __name__ == '__main__':    app.run(debug=True)
```

**Why It Works**

- Focuses the model on just the missing segments, ensuring **cohesion** with provided code.
- **How It Improves**: More **targeted** than broad prompts — useful for incremental building in a real project setting.

## 3.3. Step-by-Step Instructions

**Overview**

- Enumerate each sub-task or logical step you want in your code.

**Prompt Example**

1. _“Import necessary libraries.”_
2. _“Set up database initialization.”_
3. _“Create a route to add a new user using_ `_insert_user()_`_."_
4. _“Create a route to list all users using_ `_get_all_users()_`_."_

**Why It Works**

- Makes the code generation process more **transparent**.
- **How It Improves**: By specifying a **clear order of operations**, the model can more reliably produce the correct sequence of functionality.

## 4\. Reasoning-Based Techniques

Reasoning-based prompts encourage the model to articulate (or at least simulate) its thought process before providing code.

## 4.1. Chain-of-Thought Prompting

**Overview**

- You ask the model to break down its reasoning or logic step by step before presenting the code solution.

**Prompt Example**

> _“Explain how to add authentication to a Flask app, step by step, then provide the final code snippet.”_

**Why It Works**

- Encourages the model to generate an **explanatory path** to the solution, leading to more coherent or correct code.
- **How It Improves**: In addition to the code, you get **rationale** that can help with debugging or further refinement.

## 4.2. Zero-Shot Chain-of-Thought

**Overview**

- Ask the model to reason through a problem in steps without providing explicit examples of the reasoning format.

**Prompt Example**

> _“Explain how you decide which library to use for password hashing in Flask, then show the code that integrates this library for user registration.”_

**How It Improves**

- Similar to chain-of-thought but requires the model to come up with the reasoning steps **spontaneously**.
- In code generation context, it often leads to a thorough approach to library choice and usage instructions.

## 4.3. Few-Shot Chain-of-Thought

**Overview**

- Provide one or more short examples illustrating how to reason about a problem. Then ask the model to replicate this process on a new problem.

**Prompt Example**

1. **_“Example_**_: To create a login system, we identify the user table, check user credentials, and validate them. Code snippet follows. Let’s replicate this approach for user registration.”_
2. _“Using the step-by-step reasoning approach shown above, add a ‘/register’ route and store new user credentials securely in the database.”_

**Why It Works**

- Blends the clarity of step-by-step instructions with an **example demonstration**.
- **How It Improves**: Provides a **framework** for the model to apply consistent, methodical logic to new requests.

## 5\. Priming Techniques

Priming-based prompts use added context (persona, references, or templates) to influence the style and domain knowledge of generated code.

## 5.1. Persona-Based Prompting

**Overview**

- The model is instructed to adopt the viewpoint or role of a specific domain expert.

**Prompt Example**

> _“You are a senior Python backend developer specializing in security. Generate a Flask route to handle user registration securely.”_

**Why It Works**

- The model tailors the solution to the persona’s domain knowledge, often including security best practices.
- **How It Improves**: Helps produce code that aligns with **expert-level** patterns and potential pitfalls.

## 5.2. Skeleton (Template) Priming

**Overview**

- You provide a skeleton or outline with placeholders for the model to fill in.

**Prompt Example**

> _“Fill in the placeholders in this Flask app template to implement a user login form:_

```
from flask import Flask, request, render_template
```

```
app = Flask(__name__)@app.route('/login', methods=['GET', 'POST'])def login():    if request.method == 'POST':        # Step 1: ______        # Step 2: ______        # Step 3: return ______    return render_template('login.html')if __name__ == '__main__':    app.run(debug=True)```”
```

**Why It Works**

- Constrains the model to fill out a **specific framework**.
- **How It Improves**: Ensures the code seamlessly **integrates** into a predetermined structure — useful in large teams or pre-defined architecture.

## 5.3. Reference-Heavy Priming

**Overview**

- Provide extended reference material such as documentation or data schemas, then prompt the model to use it in the generated code.

**Prompt Example**

> _“Based on the following SQLAlchemy documentation \[link or snippet\], update the Flask app routes to use SQLAlchemy models for user data instead of raw SQL calls.”_

**Why It Works**

- The LLM can adapt to domain-specific references, generating solutions that align with **best practices** or **documentation**.
- **How It Improves**: Allows for **specialized** knowledge integration, ensuring the generated code is accurate and up-to-date with the referenced materials.

## Conclusion

By leveraging these 15 prompting techniques, you can systematically develop, expand, and optimize a Flask application — or any codebase — using Large Language Models. Each new technique either **builds upon** earlier ones or offers **new approaches** to refine, decompose, reason about, or prime the code generation process:

1. **Root Techniques** lay the groundwork, enabling initial code generation with minimal friction.
2. **Refinement Techniques** polish and extend the generated code.
3. **Decomposition Techniques** break down complex tasks into manageable chunks.
4. **Reasoning Techniques** encourage the model to provide (or simulate) a step-by-step thought process, improving clarity and correctness.
5. **Priming Techniques** add context, persona, or references that influence the style and domain relevance of the code.

As LLMs continue to evolve, so do prompting strategies. Keep experimenting with variations of these methods, watch for new best practices (e.g., at [aixrv.org](http://aixrv.org/) or similar forums), and tailor prompts to your specific domain and workflow needs.

## Ready to take your Flask app further?

Try combining multiple techniques in a single workflow. For example, begin with an **Example-Based** or **Persona-Based** prompt, refine the output using **Iterative Refinement**, and conclude with a **Reference-Heavy** approach to ensure your code meets specific library or organizational standards.

**Happy Prompting, and may your Flask apps (and all your code) flourish!**
