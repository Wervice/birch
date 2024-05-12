# Birch
## Birch is a simple logging library with the everything you need
### Current state of the project
The project is not done yet.   
Added support for:
- JavaScript

Planning to add support for:
- TypeScript
- Python
- C
- C++
- C#
- Rust
- Go
- Some more languages

## Using Birch
To use birch, please copy or include the birch file for your language into your code.
From there you need to set two constants:
- birch_path: Location where birch is supposed to write the log messages to
- birch_verbose: Enable verbose messages

Now, you can call the function `birch(level, message)`. It takes two parameters, level and message. Level can be
- verb / verbose / 0 / V
- succ / success / 1 / S
- warn / warning / 2 / W
- erro / error / 3 / E
- fata / fatal / 4 / F
