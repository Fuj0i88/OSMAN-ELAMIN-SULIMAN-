# Movie Theater Admission System

## Scenario

A movie theater has the following admission policy:

- A person is allowed to enter if:
  - They are 13 years old or older, OR
  - They are accompanied by an adult.
- AND
- They must have a valid ticket.

Logical Expression:

((Age >= 13) OR AccompaniedByAdult) AND ValidTicket

---

# 1. Identify the Components

## 1.1 What are the inputs?

1. Age (13 or older?)
2. Accompanied by an adult? (Yes/No)
3. Has a valid ticket? (Yes/No)

## 1.2 What is the process?

1. Check if the user is 13 years old or older.
2. Check if the user is accompanied by an adult.
3. Check if the user has a valid ticket.
4. Allow entry only if:
   - The user is 13+ OR accompanied by an adult.
   - AND has a valid ticket.

## 1.3 What is the output?

- Entry Allowed
- Entry Denied

---

# 2. Design the Algorithm

## 2.1 Diagram

text
Start
  |
Input Age
Input Adult Status
Input Ticket Status
  |
(Age >= 13 OR Adult Present)?
  |
  No -----------> Entry Denied
  |
 Yes
  |
Valid Ticket?
  |
 +-----+-----+
 |           |
Yes          No
 |           |
Entry      Entry
Allowed    Denied
 |           |
 +-----+-----+
       |
      End


## 2.2 Truth Table

| Age >= 13 (A) | Adult Present (B) | Valid Ticket (C) | Entry ((A OR B) AND C) |
|--------------|-------------------|------------------|------------------------|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

---

## 2.3 Step-by-Step Solution

1. Start.
2. Input age.
3. Input whether an adult is accompanying the user.
4. Input whether the ticket is valid.
5. Check if the user is 13 or older OR accompanied by an adult.
6. Check if the user has a valid ticket.
7. If both conditions are satisfied, allow entry.
8. Otherwise, deny entry.
9. End.

---

## 2.4 Pseudocode

text
BEGIN

INPUT age
INPUT accompaniedByAdult
INPUT validTicket

IF ((age >= 13) OR accompaniedByAdult) AND validTicket THEN
    OUTPUT "Entry Allowed"
ELSE
    OUTPUT "Entry Denied"
END IF

END


---

# 3. Evaluate Expression

## Sample Test Cases

| Age | Adult Present | Valid Ticket | Result |
|------|--------------|--------------|---------|
| 15 | No | Yes | Entry Allowed |
| 10 | Yes | Yes | Entry Allowed |
| 10 | No | Yes | Entry Denied |
| 15 | No | No | Entry Denied |
| 10 | Yes | No | Entry Denied |

---

# 4. Git Commands

bash
git add .
git commit -m "Complete Tutorial 2 Movie Theater Admission Activity"
git push origin main
