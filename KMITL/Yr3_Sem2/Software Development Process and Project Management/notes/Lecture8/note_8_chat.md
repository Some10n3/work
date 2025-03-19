### **Summary of Lecture 8: Kanban & Scrumban**  

This lecture covers **Kanban**, a workflow management method for improving efficiency, and **Scrumban**, a hybrid approach combining Scrum and Kanban.  

---

## **What is Kanban?**  

🔹 **Definition**  
- **Kanban** is a **process management framework** that helps teams **visualize work, limit tasks in progress, and optimize workflow**.  
- The word **"Kanban" (看板)** is Japanese, meaning **"signal card."**  
- **Developed by Toyota in the 1940s** to improve manufacturing efficiency.  

---

## **How Kanban Works**  

### **1️⃣ Kanban in Manufacturing (Toyota System)**  
- Factory teams use **Kanban cards** to **signal the next step** in production.  
- The process follows a **Pull System**:  
  ✅ Work is **only done when needed** (prevents overproduction).  
  ✅ **Kanban cards** control the number of active tasks.  

### **2️⃣ Kanban in Software Engineering**  
- **Kanban boards** track the progress of **user stories or features**.  
- **Each column** represents a **stage of development** (e.g., Design → Code → Test → Deploy).  

✅ **Example Kanban Board:**  
| **Backlog** | **Design** | **Code** | **Review** | **Test** | **Deploy** | **Done** |
|------------|----------|--------|--------|------|--------|------|
| Feature A  | Feature B | Feature C | Feature D | Feature E | Feature F | Feature G |

- Tasks move **from left to right** as work progresses.  
- Helps teams **see bottlenecks** and **track task flow** in real time.  

---

## **Key Kanban Concepts**  

### **1️⃣ WIP Limit (Work-In-Progress Limit)**  
- Restricts the **maximum number of tasks** in each stage.  
- Prevents teams from **taking on too much at once**.  
- Encourages **focus and task completion**.  

✅ **Example:**  
| **Stage** | **WIP Limit** |
|---------|-----------|
| **Design** | 5 |
| **Coding** | 3 |
| **Testing** | 2 |
| **Deployment** | 3 |

If the **Testing** stage is full (2 tasks in progress), no new tasks can enter until one is completed.  

### **2️⃣ Cycle Time**  
- Measures **how long it takes** to complete a work item.  
- Teams should **optimize their process** to reduce cycle time.  
- Helps **predict delivery times** for new tasks.  

---

## **Kanban vs. Scrum**  

| **Feature** | **Kanban** | **Scrum** |
|------------|----------|-------|
| **Iterations** | No fixed sprints | Fixed-length Sprints (1-4 weeks) |
| **Workflow** | Continuous flow | Sprint backlog (fixed work items per sprint) |
| **Work Selection** | Pull new tasks as needed | Select tasks at Sprint Planning |
| **WIP Control** | WIP Limits | Sprint backlog limits work |
| **Meetings** | No mandatory meetings | Daily Stand-ups, Sprint Planning, Retrospective |
| **Delivery** | Continuous release | At the end of each Sprint |
| **Best for** | **Support teams, bug fixes, feature requests** | **New product development** |

📌 **Kanban is better for ongoing maintenance & support work, while Scrum is better for structured product development.**  

---

## **Scrumban: The Best of Both Worlds**  

🔹 **What is Scrumban?**  
- A hybrid of **Scrum + Kanban**, combining structured planning from Scrum with the **flexibility of Kanban**.  
- **Best for long-term projects** with **unclear goals**.  

🔹 **Scrumban Features**  
✅ **Fixed timeboxed iterations (Scrum)**.  
✅ **Pull-based workflow & WIP limits (Kanban)**.  
✅ **Continuous task prioritization** – Tasks are **pulled** from backlog as capacity allows.  
✅ **Cycle time optimization instead of burndown charts**.  

✅ **Scrumban Board Example:**  
| **Backlog** | **Sprint Backlog** | **Design** | **Code** | **Review** | **Test** | **Done** |
|------------|----------------|--------|--------|--------|------|------|
| Feature A  | Feature B | Feature C | Feature D | Feature E | Feature F | Feature G |

---

## **Final Takeaways**  

✅ **Kanban focuses on continuous workflow & efficiency**.  
✅ **WIP Limits prevent overload and improve delivery speed**.  
✅ **Scrumban balances structure (Scrum) with flexibility (Kanban)**.  
✅ **Cycle time is key to process improvement** (reduce delays, increase efficiency).  

---

## **Keywords**  
- **Kanban**  
- **Kanban Board**  
- **WIP Limit (Work-In-Progress Limit)**  
- **Cycle Time**  
- **Pull System**  
- **Scrum vs Kanban**  
- **Scrumban**  
- **Continuous Improvement (Kaizen)**