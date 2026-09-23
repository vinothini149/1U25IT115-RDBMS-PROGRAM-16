# Assignment 16: Display Numbers 1 to 10 Using FOR LOOP

## Objective
Write a PL/SQL program using a `FOR` loop to display numbers from 1 to 10.

## Requirements
1. **Loop Construct:** Use a PL/SQL `FOR` loop (`FOR counter IN 1..10 LOOP`).
2. **Output:** Print each number using `DBMS_OUTPUT.PUT_LINE()`.
3. **Dynamic Value:** Output the loop index variable dynamically rather than hardcoding static numbers.
4. **File Name:** Complete your code inside `student_code.sql`.

## Scoring Criteria
Your submission will be evaluated automatically using the following test cases:
- `TC01`: `FOR` loop construct is present.
- `TC02`: Loop lower bound starts at `1`.
- `TC03`: Loop upper bound ends at `10`.
- `TC04`: `DBMS_OUTPUT.PUT_LINE` is used inside the loop.
- `TC05`: Valid PL/SQL `BEGIN ... END;` block structure.
- `TC06`: Numbers are printed dynamically using loop variables rather than hardcoded string outputs.
