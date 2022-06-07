# Challenge Summary
Using a standard queue interface, create a new class, PseudoQueue. Utilize 2 `Stack` instances to create and manage the
queue that uses the FIFO approach.

## Whiteboard Process


## Approach & Efficiency
* Create 2 Stacks: inbox and outbox
* Enqueue values to the inbox using the push method.
* If the outbox, is empty:
  * Dequeue values from the inbox using the pop method and retaining the value in a temp variable.
  * Push the temp variable onto the 2<sup>nd<sup/> Stack, the outbox.
  * Dequeue from the outbox using the pop method which then returns the first value pushed onto the inbox Stack.
* The BigO for time is O(n) and space is O(n) as well.

## Solution
* `enqueue(value)`: will push the value onto the stack
* `dequeue()`: will remove the top element from the stack and return the value

Examples:
```text
enqueue(value)
Input	           Args	 Output
[10]->[15]->[20]	5	   [5]->[10]->[15]->[20]
 	                5	   [5]

dequeue()
Input	                    Internal State       Output
[5]->[10]->[15]->[20]	    [5]->[10]->[15])     20
[5]->[10]->[15]	            [5]->[10]            15
```
