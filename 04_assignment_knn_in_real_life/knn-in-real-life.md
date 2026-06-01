# Real-World K-Nearest Neighbors (KNN)

This report outlines the conceptual framework and mathematical logic behind one of the most popular recommendation algorithms used by platforms like Netflix and Spotify.

---

## 1. The Core Concept: "Data Twins"

Netflix doesn’t just guess what I want to watch; it looks for my **"Data Twins."** In K-Nearest Neighbors (KNN), **"K"** represents the number of similar people or items the algorithm analyzes to make a decision.

[Image of K-Nearest Neighbors algorithm showing data points clustered by similarity]

If I am **User A**, and I have watched the same five Sci-Fi movies as **User B**, the algorithm assumes we are "neighbors" in a multi-dimensional interest space. If User B then watches a sixth movie and loves it, KNN recommends it to me because my data profile is physically "close" to User B's.

---

## 2. A Similarity Example: Movie Classification

Imagine I define movies using only two features (on a scale of 1 to 10): **Action Level** and **Comedy Level**.

| Movie | Action ($X_1$) | Comedy ($X_2$) | Category |
| :--- | :--- | :--- | :--- |
| *The Terminator* | 9 | 2 | Action |
| *Die Hard* | 8 | 3 | Action |
| *Superbad* | 2 | 9 | Comedy |
| *Step Brothers* | 1 | 10 | Comedy |
| **New Movie (Mystery)** | **8** | **4** | **?** |

**The KNN Logic ($K=3$):**
To classify the "Mystery" movie, the algorithm finds the three closest neighbors. In this case, they are *The Terminator*, *Die Hard*, and *Superbad*. Since two out of the three are "Action," the Mystery movie is classified as **Action**.

---

## 3. The Math: Euclidean Distance

In KNN, "Similarity" is calculated as the straight-line distance between two points ($p$ and $q$) using the **Euclidean Distance** formula:

$$d(p, q) = \sqrt{\sum_{i=1}^{n} (p_i - q_i)^2}$$

* **Small Distance:** High similarity (Neighbors).
* **Large Distance:** Low similarity (Strangers).