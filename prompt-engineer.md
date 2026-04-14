# Prompt Engineering: Comparison Guide

Effective prompt engineering is the difference between a generic, low-quality response and a highly specific, professional output. Below are comparisons for three distinct tasks.

---

## 1. Resume Content Generation

### 🔴 Weak Prompt
> "Write a resume for a software engineer."

*   **Why it's weak:** No context on experience, skills, or target company. Result will be a generic template.

### 🟢 Strong Prompt
> "Act as a professional technical recruiter. Write a results-oriented 'Experience' section for a Software Engineer with 3 years of experience in React and Node.js. Focus on a project where they optimized database queries to reduce latency by 40%. Use action verbs like 'Architected', 'Spearheaded', and 'Optimized'. Format it in bullet points."

*   **Why it's strong:** Assigns a **Role**, provides **Specific Context**, defines **Quantifiable Results**, and sets **Formatting Rules**.

---

## 2. Business Idea Brainstorming

### 🔴 Weak Prompt
> "Give me an idea for a startup."

*   **Why it's weak:** Too broad. Will return clichés like "Uber for laundry" or "Social media for dogs."

### 🟢 Strong Prompt
> "Generate 3 innovative SaaS business ideas focused on the 'Sustainability' sector. Target audience should be small business owners in urban areas. Each idea should include a name, a unique value proposition, and a possible monetization strategy (e.g., subscription or transaction fees). Avoid generic carbon-credit apps."

*   **Why it's strong:** Sets **Constraints**, specifies **Quantity**, defines **Target Audience**, and uses **Negative Constraints** (what to avoid).

---

## 3. Study Plan Creation

### 🔴 Weak Prompt
> "How do I learn Python?"

*   **Why it's weak:** No timeframe, no starting level, no specific goal. 

### 🟢 Strong Prompt
> "Create a 4-week intensive study plan to learn Python for Data Analysis. I am an absolute beginner. I can dedicate 10 hours per week. Include specific topics for each week (like Pandas, NumPy, and Matplotlib) and suggest one hands-on project for the final week. Format this as a weekly schedule."

*   **Why it's strong:** Defines a **Timeline**, identifies **Student Level**, specifies **Time Commitment**, and requests a **Structured Deliverable**.

---

## Key Takeaways for Better Prompts
1.  **Context is King**: Always provide the 'Who, What, Where, and Why'.
2.  **Give Examples**: (Few-shot prompting) Showing the model a pattern helps it follow it.
3.  **Specify Format**: Tell the AI if you want a table, markdown, code, or a list.
4.  **Iterate**: If the first response is off, refine the prompt by adding instructions like "Be more concise" or "Use a more formal tone."
