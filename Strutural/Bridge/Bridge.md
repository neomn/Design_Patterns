# Bridge Design Pattern

## Overview

The Bridge design pattern is a structural pattern that separates an abstraction from its implementation, allowing them to vary independently. This pattern is especially useful when you want to avoid a permanent binding between an abstraction and its implementation, enabling the two to be developed and modified independently.

## Structure

The Bridge pattern consists of four main components:

1. Abstraction: Defines the abstract interface and maintains a reference to the Implementor.
2. RefinedAbstraction: Extends the Abstraction interface.
3. Implementor: Defines the interface for implementation classes.
4. ConcreteImplementor: Implements the Implementor interface.

## Pros

1. Decoupling: Separates the interface from the implementation, allowing them to evolve independently.
2. Improved extensibility: New abstractions and implementations can be added easily without modifying existing code.
3. Platform independence: Enables the same abstraction to work with different implementations on various platforms.
4. Better organization: Helps in organizing code by separating concerns.

## Cons

1. Increased complexity: Can make the overall system more complex, especially for simple scenarios.
2. Performance overhead: May introduce a slight performance cost due to the additional indirection.
3. Initial design effort: Requires more upfront design and planning.

## Comparison with Other Structural Patterns

1. Adapter Pattern:
   - Bridge is designed upfront to let abstraction and implementation vary independently.
   - Adapter is used to make unrelated classes work together after they're designed.

2. Decorator Pattern:
   - Bridge focuses on separating abstraction from implementation.
   - Decorator focuses on adding responsibilities to objects dynamically.

3. Composite Pattern:
   - Bridge deals with two orthogonal dimensions (abstraction and implementation).
   - Composite deals with part-whole hierarchies.

4. Facade Pattern:
   - Bridge provides a clean separation between abstraction and implementation.
   - Facade provides a simplified interface to a complex subsystem.

## Use Cases

- When you want to avoid a permanent binding between an abstraction and its implementation.
- When both the abstraction and its implementation need to be extended independently.
- When changes in the implementation should not affect the client code.
- When you want to share an implementation among multiple objects.

## Python Example

See the accompanying `bridge_pattern.py` file for a Python implementation of the Bridge design pattern.

In this example, we demonstrate the Bridge pattern using a simple drawing application that can draw different shapes (Circle, Square) using different rendering methods (VectorRenderer, RasterRenderer).

The Abstraction (Shape) is separated from its Implementation (Renderer), allowing them to vary independently. This separation enables us to add new shapes or rendering methods without modifying existing code.
