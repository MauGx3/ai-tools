---
applyTo: "**/*.py, **/*.ipynb"
---

EXTREMELY IMPORTANT: THESE INSTRUCTIONS MUST BE FOLLOWED WHENEVER PERFORMANCE IS TO BE IMPROVED IN PYTHON CODE. THE MAIN FOCUS OF THIS DOCUMENT IS TO HELP YOU REFACTOR AND IMPROVE THE PERFORMANCE OF PYTHON CODE.

## General Instructions for Python Performance
* Don't optimize what isn't slow – premature optimization wastes time and can make code more complex.

### Profiler usage
* Use a deterministic profiler when you need precise, complete timing data for every function call and can tolerate the significant overhead—ideal for profiling short scripts or specific code sections. Use a statistical profiler when you need minimal performance impact on long-running applications or production systems, as it samples the call stack at intervals rather than tracking every call.
<!-- TODO -->
* You can only know what makes your program slow after first getting the program to give correct results, then running it to see if the correct program is slow. When found to be slow, profiling can show what parts of the program are consuming most of the time. A comprehensive but quick-to-run test suite can then ensure that future optimizations don't change the correctness of your program. In short:
    - Get it right.
    - Test it's right.
    - Profile if slow.
    - Optimise.
    - Repeat from 2.
<!-- TODO -->

## Packages to be used
* Packages like `Cython` can dramatically improve the application's performance by making it easier to push performance-critical code into C or machine language.
* Learn what are the bottlenecks of the code using profile and trace.
    - Deterministic profile modules are: `cProfile` and `profile`. `pstats` can be used to analyze the results.
    - Statistical profiler modules are `py-spy` and `Pyinstrument`.
    - Trace modules are: `trace` and `tracemalloc`.
* Use Just-In-Time compilation (JIT) with `Numba` or `Pypy` to speed up execution of Python code.
* Use `multiprocessing` or `concurrent.futures` to parallelize CPU-bound tasks.
* Use `asyncio` to handle I/O-bound tasks concurrently.

## Profiling and Tracing
Follow these steps to find bottlenecks in your code:
    1. Use `time` to measure execution time of the entire program.
    2. Use `timeit` module to measure execution time of functions, to give a quick overview of what needs optimization.
    3. Use `cProfile` to see where the time is being spent in your program, function by function. It will tell the number of calls and show what is the call hierarchy. If `cProfile` is not available, use `profile`.
    4. Use `pstats` to read the output of `cProfile` or `profile` and perform various sorts and filters on the data. Focus on the most time-consuming functions. Save the output for persistence.
    5. Use `trace` to trace program execution, generate annotated statement coverage listings, print caller/callee relationships, and more.
